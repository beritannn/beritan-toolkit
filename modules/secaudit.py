import requests
from core.ui import *

checks=[
"Content-Security-Policy",
"X-Frame-Options",
"Strict-Transport-Security",
"X-Content-Type-Options",
"Referrer-Policy",
"Permissions-Policy"
]

def run():
    url=input("URL: ")

    try:
        h=requests.get(url,timeout=5).headers

        for c in checks:
            if c in h:
                good(c+" ✔")
            else:
                warn(c+" ✘ Missing")

    except:
        bad("Audit failed")
