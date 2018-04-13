import requests


def getDT():
    request = requests.get('https://s3.amazonaws.com/dolartoday/data.json').json()
    return request["USD"]["dolartoday"]
