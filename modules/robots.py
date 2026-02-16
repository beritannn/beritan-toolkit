import requests
from core.ui import *

def run():
    site=input("Site URL: ")
    url=site.rstrip("/")+"/robots.txt"

    try:
        r=requests.get(url)
        print(r.text)
    except:
        bad("Cannot fetch robots.txt")
