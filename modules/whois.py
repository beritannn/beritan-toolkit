import whois
from core.ui import *

def run():
    d=input("Domain: ")

    try:
        w=whois.whois(d)

        info("Registrar: "+str(w.registrar))
        info("Creation: "+str(w.creation_date))
        info("Expiration: "+str(w.expiration_date))
        info("Emails: "+str(w.emails))

    except:
        bad("WHOIS failed")
