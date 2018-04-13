from utils import SaveLoadObj
from utils.USDVEF import getDollar
from utils.VET import datetimeVen, timeVen


def updateLBTC(bot, job):
    if job.context == "24":
        DatePrice = SaveLoadObj.load_obj("LBTClist")
        DatePrice.append({"date": datetimeVen(), "LocalBitcoins": getDollar('24')})
        SaveLoadObj.save_obj(DatePrice, "LBTClist")
    elif job.context == "1":
        if timeVen().hour == 0:
            hourly = []
            SaveLoadObj.save_obj(hourly, "LBTChourly")
        hourly = SaveLoadObj.load_obj("LBTChourly")
        hourly.append({'date': timeVen(), "LocalBitcoins": getDollar('1')})
