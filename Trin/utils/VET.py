import datetime
import os
import time

# Only available in UNIX

os.environ['TZ'] = 'America/Caracas'
time.tzset()



def horaVen():
    return time.strftime('%d/%m/%y - %I:%M %p VET')

def datetimeVen():
    return datetime.date.today()


def timeVen():
    timeObj = time.localtime()
    # example
    # time.struct_time(tm_year=2018, tm_mon=4, tm_mday=13, tm_hour=1, tm_min=49, tm_sec=2, tm_wday=4, tm_yday=103, tm_isdst=1)
    return datetime.datetime(timeObj[0], timeObj[1], timeObj[2], timeObj[3], timeObj[4], timeObj[5])
