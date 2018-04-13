from utils.VET import datetimeVen
from utils.VET import datetimeVen
from utils.getDT import getDT


def updateDT(bot, job):
    DatePrice = SaveLoadObj.load_obj("DTlist")
    DatePrice.append({"date": datetimeVen(), "DolarToday": getDT()})
    SaveLoadObj.save_obj(DatePrice, "DTlist")
