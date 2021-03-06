from utils import SaveLoadObj
from utils.USDVEF import getDollar
from utils.VET import datetimeVen, timeVen
import datetime


def updateLBTC(bot, job):
    if job.context == "24":
        DatePrice = SaveLoadObj.load_obj("LBTClist")
        DatePrice.append({"date": datetimeVen() - datetime.timedelta(days=1), "LocalBitcoins": getDollar('24')})
        SaveLoadObj.save_obj(DatePrice, "LBTClist")
    elif job.context == "1":
        hourly = SaveLoadObj.load_obj("LBTChourly")
        hourly.append({'date': datetime.time(hour=timeVen().hour, minute=0, second=0), "LocalBitcoins": getDollar('1')})
        SaveLoadObj.save_obj(hourly, "LBTChourly")
