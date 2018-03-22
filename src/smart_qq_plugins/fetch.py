# -*- coding: utf-8 -*-
import requests
import json


def fetchdata():
    res = requests.get('https://api.coinmarketcap.com/v1/ticker/?convert=cny&limit=100')
    mystr = res.content.decode('utf-8')
    ret = json.loads(mystr)

    for Price in ret:
        if Price["id"] == 'nem':
            print(Price["price_usd"])
            return float(Price["price_usd"])
