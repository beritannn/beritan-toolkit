import requests
from core.ui import *

def run():
    file=input("File with URLs: ")

    try:
        with open(file) as f:
            urls=f.readlines()

        ok=0
        fail=0

        for u in urls:
            u=u.strip()

            try:
                r=requests.get(u,timeout=4)
                info(f"{u} -> {r.status_code}")
                ok+=1
            except:
                bad(u)
                fail+=1

        good(f"Success:{ok}")
        warn(f"Failed:{fail}")

    except:
        bad("File error")
