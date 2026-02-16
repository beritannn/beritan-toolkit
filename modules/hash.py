import hashlib
from core.ui import *

def run():
    t=input("Text: ").encode()

    print("MD5:",hashlib.md5(t).hexdigest())
    print("SHA1:",hashlib.sha1(t).hexdigest())
    print("SHA256:",hashlib.sha256(t).hexdigest())
