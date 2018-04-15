import requests

# Dictionary containing the average values of the rate between USD and VEF and also the time
dollarDic = {}

# This function requests the json data from LocalBitcoins, calculates the rate between
# USD and VEF and returns an array with the averages
def calcDollar():
    r = requests.get('https://localbitcoins.com/bitcoinaverage/ticker-all-currencies/').json()
    USD = r["USD"]
    VEF = r["VEF"]
    avg_1h =  float(VEF["avg_1h"])  / float(USD["avg_1h"])
    avg_6h =  float(VEF["avg_6h"])  / float(USD["avg_6h"])
    avg_12h = float(VEF["avg_12h"]) / float(USD["avg_12h"])
    avg_24h = float(VEF["avg_24h"]) / float(USD["avg_24h"])
    avg_all = [avg_1h, avg_6h, avg_12h, avg_24h]
    return avg_all

# Sets the dollar price when called
def setDollar(bot, job):
    try:
        dollarDic["all"] = calcDollar()
        dollarDic["1"] = dollarDic["all"][0]
        dollarDic["6"] = dollarDic["all"][1]
        dollarDic["12"] = dollarDic["all"][2]
        dollarDic["24"] = dollarDic["all"][3]
    except:
        print(calcDollar())