from core.ui import *
import webbrowser

def run():
    u=input("Username: ")

    links=[
f"https://google.com/search?q={u}",
f"https://duckduckgo.com/?q={u}",
f"https://bing.com/search?q={u}",
f"https://github.com/{u}",
f"https://reddit.com/user/{u}",
f"https://instagram.com/{u}",
f"https://twitter.com/{u}"
]

    for l in links:
        good(l)

    if input("Open? y/n: ")=="y":
        for l in links:
            webbrowser.open(l)
