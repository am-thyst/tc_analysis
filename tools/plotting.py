def rem_ax(ax):
    # Removes the axes, useful for when you make another
    # subplot to add a colorbar
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    ax.get_xaxis().set_ticks([])
    ax.get_yaxis().set_ticks([])

def map_formatter(ax,tick_base_x=15.0, tick_base_y=15.0, labelsize=15,top_label=False, bottom_label=True, right_label=False,left_label=True,central_longitude=0.0,res='10m'):
    gl = ax.gridlines(crs=ccrs.PlateCarree(), draw_labels=True,linewidth=0.75, color='gray',linestyle=":")
    gl.xlabels_top = top_label
    gl.ylabels_right = right_label
    gl.ylabels_left = left_label
    gl.xlabels_bottom = bottom_label
    gl.xlocator = mticker.MultipleLocator(base=tick_base_x)
    gl.ylocator = mticker.MultipleLocator(base=tick_base_y)
    ax.coastlines(resolution=res, color='k', linewidth=1)
    gl.xlabel_style= {'size':labelsize}
    gl.ylabel_style= {'size':labelsize}
    gl.xformatter = LONGITUDE_FORMATTER
    gl.yformatter = LATITUDE_FORMATTER


