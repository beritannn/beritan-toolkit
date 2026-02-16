import requests
from core.ui import *

tech_signatures={
"WordPress":"wp-content",
"Shopify":"cdn.shopify",
"React":"react",
"Vue":"vue",
"jQuery":"jquery",
"Bootstrap":"bootstrap",
"Cloudflare":"cloudflare",
}

def run():
    url=input("URL: ")

    try:
        r=requests.get(url,timeout=6)

        info("Server: "+str(r.headers.get("Server")))
        info("Powered: "+str(r.headers.get("X-Powered-By")))

        body=r.text.lower()

        for name,sig in tech_signatures.items():
            if sig in body:
                good("Detected: "+name)

    except:
        bad("Detection failed")
