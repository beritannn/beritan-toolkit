from core.ui import *
import webbrowser

def run():
    name=input("Name Surname: ")

    links=[
f"https://google.com/search?q={name}",
f"https://duckduckgo.com/?q={name}",
f"https://linkedin.com/search/results/all/?keywords={name}",
]

    for l in links:
        good(l)

    if input("Open? y/n: ")=="y":
        for l in links:
            webbrowser.open(l)
