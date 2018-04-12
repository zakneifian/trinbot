import time
import datetime
import os

# Only avaible in UNIX
 os.environ['TZ'] = 'America/Caracas'
 time.tzset()



def horaVen():
    return time.strftime('%d/%m/%y - %I:%M %p VET')

def datetimeVen():
    return datetime.date.today()