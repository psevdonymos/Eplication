import requests
import json
from pprint import pprint

from requests_oauthlib import OAuth1Session

auth_file = open("app_details", "r")
auth_str = auth_file.readline().split(";")
print(auth_str[1])

def print_names(json):
    for i in range(0, len(json["article"])):
        print( i, json["article"][i]["product"]["enName"])

def sum_offer_prizes(json):
    sum = 0
    for i in range(0, len(json["article"])):
        sum += json["article"][i]["price"] * json["article"][i]["count"]
    return sum

def sum_sold_cards_prizes(json):
    sum = 0
    return sum

url = 'https://api.cardmarket.com/ws/v2.0/output.json/'
stock_url = 'https://api.cardmarket.com/ws/v2.0/output.json/stock'
# TODO fix error 206
order_url = 'https://api.cardmarket.com/ws/v2.0/output.json/orders/seller/received/80'

stock_session = OAuth1Session(auth_str[0],
                         client_secret=auth_str[1],
                         resource_owner_key=auth_str[2],
                         resource_owner_secret=auth_str[3],
                         realm = stock_url)

stock_resp = stock_session.get(stock_url)
if (stock_resp.status_code != 200):
    # This means something went wrong.
    #raise ApiError('GET /tasks/ {}'.format(resp.status_code))
    print('ERROR Stock', stock_resp.status_code)
    #exit()

order_session = OAuth1Session(auth_str[0],
                         client_secret=auth_str[1],
                         resource_owner_key=auth_str[2],
                         resource_owner_secret=auth_str[3],
                         realm = order_url)

order_resp = order_session.get(order_url)
if (order_resp.status_code != 200):
    # This means something went wrong.
    #raise ApiError('GET /tasks/ {}'.format(resp.status_code))
    print('ERROR Order', order_resp.status_code)
else:
    with open('/data/orders/all.txt', 'w') as outfile:
        json.dump(order_resp, outfile)

#pprint (order_resp.json()) #["article"][0]["product"]

#print_names(resp.json())
print ("Current Stock value: ", sum_offer_prizes(stock_resp.json()))
