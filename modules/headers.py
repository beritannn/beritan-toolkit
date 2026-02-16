import requests
from core.ui import *

def run():
    url=input("URL: ")

    try:
        r=requests.get(url)

        for k,v in r.headers.items():
            print(k,":",v)

    except:
        bad("Request failed")
