from datetime import datetime

def hrs_since_init(year_0,month_0,day_0,hr_0,year_1,month_1,day_1,hr_1):
    # Calculates time since model initialisation in hrs
    # format is dd/mm/yyyy hh
    start = str(day_0) + '/' + str(month_0) + '/' + str(year_0) + ' ' +str(hr_0) +':00'
    end = str(day_1) + '/' + str(month_1) + '/' + str(year_1) + ' ' + str(hr_1) +':00'
    FMT = '%d/%m/%Y %H:%M'
    tdelta = datetime.strptime(end, FMT) - datetime.strptime(start, FMT)
    day_hours = tdelta.days * 24
    second_hours = tdelta.seconds / 60 / 60
    return(int(day_hours+second_hours))
