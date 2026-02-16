import requests
from core.ui import *

paths=[
"admin","login","dashboard","panel","backup",
".git",".env","config","db","robots.txt",
"sitemap.xml","uploads","api"
]

def run():
    url=input("Base URL: ").rstrip("/")

    for p in paths:
        try:
            r=requests.get(url+"/"+p,timeout=3)
            if r.status_code<400:
                good(f"{p} -> {r.status_code}")
        except:
            pass
