from core.ui import *

def run():
    path=input("Log path: ")

    try:
        with open(path) as f:
            for line in f:
                if "error" in line.lower():
                    warn(line.strip())
                if "fail" in line.lower():
                    bad(line.strip())
    except:
        bad("Cannot read log")
