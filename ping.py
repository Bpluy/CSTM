import requests
import time
import sys

if len(sys.argv) == 2:
    API_KEY = sys.argv[1]
else:
    print('Введите Market API-KEY')
    API_KEY = input()

#API_KEY = '85tzR2QL7p4yV0Jd7Mvq4zB9RytNadE'

API_URL_ITEMS = f"https://market.csgo.com/api/v2/items?key={API_KEY}"
API_URL_PING = f"https://market.csgo.com/api/v2/ping?key={API_KEY}"

def saleItems(itemID,itemPrice):
    return f"https://market.csgo.com/api/v2/add-to-sale?key={API_KEY}&id={itemID}&price={itemPrice}&cur=RUB"

def setPrice(itemID,itemPrice):
    return f"https://market.csgo.com/api/v2/set-price?key={API_KEY}&item_id={itemID}&price={itemPrice}&cur=RUB"

def searchItem(hash_name):
    return f"https://market.csgo.com/api/v2/search-item-by-hash-name-specific?key={API_KEY}&hash_name={hash_name}"

def tryToRequest(URL):
    response = requests.get(URL)
    while response.status_code != 200:
        print(f"Попытка переподключения к {URL}")
        response = requests.get(URL)
        time.sleep(0.25)
    return response.json()


flag = 0
while True:    
    tryToRequest(API_URL_PING)
    time.sleep(180)