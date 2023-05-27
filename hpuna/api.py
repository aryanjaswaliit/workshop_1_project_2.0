import requests
import json
import pandas as pd
from bs4 import BeautifulSoup

url = "https://hpuna.nic.in/about-district/whos-who/"
header = {
    "User-Agent":"Nasa"
}

data = requests.get(url,headers=header)
print(data)

soup = BeautifulSoup(data.text)

admin = soup.find("div",{"class":"whoswho"})
#print(admin)

table = admin.find_all("td")
#print(table)
new_arr = []
n=0
name = ""
des =""
add = ""
phone = ""
email = ""
for api in table:
    if n == 0:
        name = str(api.text)
        n =n +1
    elif n == 1:
        des = str(api.text)
        n =n +1
    elif n == 2:
        add = str(api.text)
        n =n +1
    elif n == 3:
        phone = str(api.text)
        n =n +1
    elif n == 4:
        email = str(api.text)
        n =0

        new_js = {
            "name":name,
            "des":des,
            "add":add,
            "phone":phone,
            "email":email
        }

        new_arr.append(new_js)
    
    
print(new_arr)

data = pd.DataFrame(new_arr)
data.to_csv("una_info.csv",index=False)