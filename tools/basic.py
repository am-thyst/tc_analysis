from datetime import datetime
import iris

def hrs_since_init(month_1,day_1,hr_1,month_0=9,day_0=22,hr_0=0,year_0=2017,year_1=2017):
    # Calculates time since model initialisation in hrs
    # format is dd/mm/yyyy hh
    start = str(day_0) + '/' + str(month_0) + '/' + str(year_0) + ' ' +str(hr_0) +':00'
    end = str(day_1) + '/' + str(month_1) + '/' + str(year_1) + ' ' + str(hr_1) +':00'
    FMT = '%d/%m/%Y %H:%M'
    tdelta = datetime.strptime(end, FMT) - datetime.strptime(start, FMT)
    day_hours = tdelta.days * 24
    second_hours = tdelta.seconds / 60 / 60
    return(int(day_hours+second_hours))

def CFL(ws,ts=120,res=4400,Iris=False):
    # Calculates CFL number. > 1 indicates smaller ts needed.
    # Can be used on xarray, numpy array, iris, int or float
    # Units must be in m or s (or ms)
    if iris == False:
        cfl = ws * (ts / res)
    if Iris == True:
        tr = ts / res
        cfl = iris.analysis.maths.multiply(ws,tr)    
    return(cfl)
