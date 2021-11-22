import os
from toolbox import storm_relative_tools
import glob
from datetime import datetime

def labels(datastr):
    # converts date strings in .avp files to an int (format hhmm)
    drop_time = (datastr[datastr.find("(y,m,d,h,m,s):")+35:datastr.find("(y,m,d,h,m,s):")+43])
    time = drop_time[:5] # format time to xx:xx
    time = time[0:2] + time[3:5]
    return(int(time))

def extract_files(file_path,yr,mth,day,start,end):
    # extracts all .avp files within a directory within a certain date and time range
    # start and end must be in hmm format, like 1200 for 12:00 or 100 for 1:00 
    os.chdir(file_path)
    files = glob.glob("*.avp")    
    date_sel = datetime(yr,mth,day); start_end = [start,end]
    file_list = []; date_list = []
    
    for x in range(len(files)):
        dates = open(files[x], 'r').read()
        if storm_relative_tools.handle_date(dates) == date_sel: # if date is date_sel 
            if start_end[0] <= labels(dates) <= start_end[1]: # if time within this range 
               date_list.append(int(labels(dates)))
               file_list.append(files[x])	
    return(file_list)
