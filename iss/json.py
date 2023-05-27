import requests
import json
import pandas as pd

n = 0
arr = []
while n < 10:
    print(n)
    url = "http://api.open-notify.org/iss-now.json"
    header = {
        "User-Agent":"Nasa"
    }

    data = requests.get(url,headers=header)
    print(data)
    #print(data.text)
    json_store = json.loads(data.text)
    lat = json_store["iss_position"]
 
    print(lat)
    input("aa")
