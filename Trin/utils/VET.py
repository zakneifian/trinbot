import time
import os

# Only avaible in UNIX
os.environ['TZ'] = 'America/Caracas'
time.tzset()



def horaVen():
    return time.strftime('%d/%m/%y - %I:%M %p VET')