from core.ui import *
import webbrowser

def run():
    n=input("Phone number: ")

    links=[
f"https://google.com/search?q={n}",
f"https://sync.me/search/?number={n}",
f"https://www.truecaller.com/search?q={n}",
]

    for l in links:
        info(l)

    if input("Open? y/n: ")=="y":
        for l in links:
            webbrowser.open(l)
