import requests
import json

import pandas as pd

url = "https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY"

header = {
    "User-Agent":"Nasa"
}

data = requests.get(url,headers=header)
#print(data)
#print(data.text)

json_store = json.loads(data.text)
#print(json_store["date"])
#print(json_store["url"])
new_js = []
new_js.append(json_store)
#print(new_js)
### create csv
##data = pd.DataFrame(new_js)
data = pd.DataFrame(new_js)

data.to_csv("output.csv",index=False)
