from utils import SaveLoadObj
from utils.VET import datetimeVen
from utils.getDT import getDT
import datetime


def updateDT(bot, job):
    DatePrice = SaveLoadObj.load_obj("DTlist")
    DatePrice.append({"date": datetimeVen() - datetime.timedelta(days=1), "DolarToday": getDT()})
    SaveLoadObj.save_obj(DatePrice, "DTlist")
