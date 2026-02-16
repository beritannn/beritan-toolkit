import socket
from core.ui import *

def run():
    host=input("Host: ")
    ports=[21,22,25,53,80,110,139,143,443,445,3389]

    for p in ports:
        s=socket.socket()
        s.settimeout(0.5)
        r=s.connect_ex((host,p))

        if r==0:
            good(f"OPEN {p}")
        s.close()
