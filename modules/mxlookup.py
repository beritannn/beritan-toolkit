import dns.resolver
from core.ui import *

def run():
    d=input("Domain: ")

    try:
        answers=dns.resolver.resolve(d,"MX")

        for r in answers:
            info("MX: "+str(r.exchange))
            info("Priority: "+str(r.preference))
            print()

    except:
        bad("MX lookup failed")
