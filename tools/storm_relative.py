# Scripts to adjust things to make them storm relative
# e.g. slightly adjust the storm wind speeds relative to the storm motion

def storm_position(df,hr,day,mth=9,yr=2017):
    # future_lat and future_lon are 1 hr ahead, or whatever your dt is
    track = np.load(df,allow_pickle=True)
    J_track_time = track[2].tolist().index(cftime.DatetimeGregorian(2017, 9, int(day), int(hr), 0, 0, 0))
    model_lat, model_lon = track[3][J_track_time], track[4][J_track_time]
    future_lat, future_lon = track[3][J_track_time+1], track[4][J_track_time+1]
    return(model_lat,model_lon,future_lat,future_lon)

def storm_relative_cubes(u_cube,v_cube,df,hr,day,mth=9,yr=2017,dt=3600):
    # Based on a dt of 1 hr, can be adjusted
    # First find the storm position
    model_lat, model_lon, future_lat, future_lon = storm_position(df,hr,day,mth,yr)
    # for storm relative
    Dx = storm_relative_tools.haversine_d(model_lat,model_lat,model_lon,future_lon)
    Dy = storm_relative_tools.haversine_d(model_lat,future_lat,model_lon,model_lon)
    u_speed = (Dx) / (dt*2) * np.sign(future_lon - model_lon)
    v_speed = (Dy) / (dt*2) * np.sign(future_lat - model_lat)

    u_cube = iris.analysis.maths.subtract(u_cube,u_speed)
    new_u = u_cube.interpolate([('latitude', v_cube.coord('latitude').points),('longitude',v_cube.coord('longitude').points)], iris.analysis.Linear())
    v_cube = iris.analysis.maths.subtract(v_cube,v_speed)
    model_ws = uradvazitools.ws_ifunc(new_u, v_cube, new_name='wind speed')
    return(model_ws, model_lat, model_lon)
