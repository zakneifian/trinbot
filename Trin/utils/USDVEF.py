import requests
import time

# Amount of seconds between updates of the 'cache' value of the dollar
span = 300
# Dictionary containing the average values of the rate between USD and VEF and also the time
dollarDic = {
  "timer": 0,
  "1": 0,
  "6": 0,
  "12": 0,
  "24": 0,
  "all": [0, 0, 0, 0]}

# This function requests the json data from LocalBitcoins, calculates the rate between
# USD and VEF and returns an array with the averages
def setDollar():
    r = requests.get('https://localbitcoins.com//bitcoinaverage/ticker-all-currencies/').json()
    USD = r["USD"]
    VEF = r["VEF"]
    avg_1h =  float(VEF["avg_1h"])  / float(USD["avg_1h"])
    avg_6h =  float(VEF["avg_6h"])  / float(USD["avg_6h"])
    avg_12h = float(VEF["avg_12h"]) / float(USD["avg_12h"])
    avg_24h = float(VEF["avg_24h"]) / float(USD["avg_24h"])
    avg_all = [avg_1h, avg_6h, avg_12h, avg_24h]
    return avg_all

# This function checks the actual UNIX time and compares it to the dollarDic.
# If the difference is bigger than span (300 secs at the moment of writing this),
# set the new time and values for dollarDic.
def secondsSinceLastUse():
    if time.time() - dollarDic["timer"] > span:
        dollarDic["timer"] = time.time()
        dollarDic["all"] = setDollar()
        dollarDic["1"] = dollarDic["all"][0]
        dollarDic["6"] = dollarDic["all"][1]
        dollarDic["12"] = dollarDic["all"][2]
        dollarDic["24"] = dollarDic["all"][3]

# Checks for new value with secondsSinceLastUse() and then return the dictionary value
def getDollar(arg):
    secondsSinceLastUse()
    return dollarDic[arg]
