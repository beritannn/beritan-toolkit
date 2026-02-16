import requests
from core.ui import *

def run():
    ip=input("IP: ")

    try:
        data=requests.get(f"https://ipinfo.io/{ip}/json").json()

        info(f"City: {data.get('city')}")
        info(f"Region: {data.get('region')}")
        info(f"Country: {data.get('country')}")
        info(f"Org: {data.get('org')}")
        info(f"Loc: {data.get('loc')}")

    except:
        bad("Lookup failed")
