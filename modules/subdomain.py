import requests
from core.ui import *

def run():
    d=input("Domain: ")

    try:
        r=requests.get(f"https://crt.sh/?q=%25.{d}&output=json").json()

        found=set()

        for x in r:
            found.add(x['name_value'])

        for s in found:
            print(s)

    except:
        bad("Lookup failed")
