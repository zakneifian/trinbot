import requests
from utils.VET import datetimeVen
from utils import SaveLoadObj

def updateDT(bot, job):
    DatePrice = SaveLoadObj.load_obj("DTlist")
    request = requests.get('https://s3.amazonaws.com/dolartoday/data.json').json()
    DatePrice.append({"date": datetimeVen(), "price": request["USD"]["dolartoday"]})
    SaveLoadObj.save_obj(DatePrice, "DTlist")
