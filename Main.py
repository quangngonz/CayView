import requests
from bs4 import BeautifulSoup
import time
from threading import Thread
from datetime import datetime

url = "http://hn-ams.edu.vn/content/mock-gart-2021-gi%E1%BA%A3i-%C4%91%E1%BA%A5u-k%E1%BB%8Bch-t%C3%ADnh-v%C3%A0-%C4%91%E1%BA%A7y-th%C3%A1ch-th%E1%BB%A9c-%C4%91%E1%BA%BFn-t%E1%BB%AB-c%C3%A2u-l%E1%BA%A1c-b%E1%BB%99-greenams-6520-robotics"

session = requests.Session()

def get_html():
    for i in range(10000):
        previousTime = time.time()  

        res = session.get(url)
        res_status = res.status_code

        res = res.text
        soup = BeautifulSoup(res, "html.parser")
        view = soup.find_all("div", {"class": "views-field-phpcode"})[10]
        view = view.text.split("|")[2]

        now = datetime.now()
        print(now.strftime("%H:%M:%S"))
        print("Respone",res_status)
        print(view[1:], end="")

        currentTime = time.time()  
        print("Time: " + str(currentTime - previousTime), end="\n\n")

get_html()