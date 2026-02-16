from core.ui import *

def run():
    p=input("Password: ")

    score=0

    if len(p)>12: score+=1
    if any(c.isupper() for c in p): score+=1
    if any(c.islower() for c in p): score+=1
    if any(c.isdigit() for c in p): score+=1
    if any(not c.isalnum() for c in p): score+=1

    info("Score: "+str(score)+"/5")

    if score>=4:
        good("Strong")
    else:
        warn("Weak")
