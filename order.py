import requests
import json
from pprint import pprint

class OrderManager():
    def __init__(self, *args, **kwargs):

    
    def sum_offer_prizes(self, json):
        sum = 0
        for i in range(0, len(json["article"])):
        sum += json["article"][i]["price"] * json["article"][i]["count"]
        return sum
    
    def sum_sold_cards_prizes(self, json):
        sum = 0
        return sum
        
   