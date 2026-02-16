import hashlib
from core.ui import *

def run():
    path=input("File: ")

    try:
        with open(path,"rb") as f:
            data=f.read()

        print("SHA256:",hashlib.sha256(data).hexdigest())

    except:
        bad("File error")
