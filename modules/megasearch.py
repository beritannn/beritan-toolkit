from core.ui import *
import webbrowser

def run():
    term=input("Target: ")

    engines=[
"https://google.com/search?q=",
"https://bing.com/search?q=",
"https://duckduckgo.com/?q=",
"https://yandex.com/search/?text="
]

    for e in engines:
        url=e+term
        good(url)

    if input("Launch all? y/n: ")=="y":
        for e in engines:
            webbrowser.open(e+term)
