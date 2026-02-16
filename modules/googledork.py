from core.ui import *
import webbrowser

def run():
    target=input("Target: ")

    dorks=[
f'site:{target}',
f'intitle:"index of" {target}',
f'inurl:login {target}',
f'filetype:pdf {target}',
f'"confidential" {target}',
f'"password" {target}',
f'ext:sql {target}',
f'ext:log {target}',
]

    for d in dorks:
        info(d)

    if input("Open browser? y/n: ")=="y":
        for d in dorks:
            webbrowser.open("https://www.google.com/search?q="+d)
