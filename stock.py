import requests
import json
from pprint import pprint

class StockManager():
    def __init__(self, *args, **kwargs):
        self.stock_session
        self.stock_resp
        #self.stock_url = 'https://api.cardmarket.com/ws/v2.0/output.json/stock'

        self.call_mkm_rest_api()

    def print_names(self, json):
        for i in range(0, len(json['article'])):
            print( i, json['article'][i]['product']['enName'])
