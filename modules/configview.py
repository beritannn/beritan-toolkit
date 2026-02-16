import json
from core.ui import *

def run():
    try:
        c=json.load(open("config/settings.json"))
        print(c)
    except:
        bad("Config error")
