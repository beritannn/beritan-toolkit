import socket
from core.ui import *

def run():
    domain=input("Domain: ")

    try:
        ip=socket.gethostbyname(domain)
        good("Resolved IP: "+ip)

        info("Reverse:")
        try:
            rev=socket.gethostbyaddr(ip)
            print(rev)
        except:
            warn("No reverse")

    except:
        bad("DNS failed")
