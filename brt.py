from colorama import Fore, init
init(autoreset=True)

import os
import modules


# ================= BANNER =================

def banner():
    os.system("cls")

    clown = """
      .-\"\"\"\"-.
     / -   -  \\
    |  .-. .- |
    |  \\o| |o (
    \\     ^    \\
     '.  )--'  /
       '-...-'
    """

    print(Fore.MAGENTA + clown)

    print(Fore.CYAN+r"""
██████╗ ███████╗██████╗ ██╗████████╗ █████╗ ███╗   ██╗
██╔══██╗██╔════╝██╔══██╗██║╚══██╔══╝██╔══██╗████╗  ██║
██████╔╝█████╗  ██████╔╝██║   ██║   ███████║██╔██╗ ██║
██╔══██╗██╔══╝  ██╔══██╗██║   ██║   ██╔══██║██║╚██╗██║
██████╔╝███████╗██║  ██║██║   ██║   ██║  ██║██║ ╚████║
╚═════╝ ╚══════╝╚═╝  ╚═╝╚═╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═══╝
""")

    print(Fore.YELLOW+"        BERITAN CYBER TOOLKIT\n")


# ================= EXAMPLES =================

examples={
16:"example → example.com",
17:"example → https://site.com",
18:"example → gmail.com",
19:"example → example.com",
20:"example → urls.txt",
21:"example → site:gov filetype:pdf",
22:"example → username",
23:"example → +905xxxxxxxxx",
24:"example → ad soyad",
25:"example → target"
}


# ================= MENU =================

def menu():

    tools=[
"IP Info","DNS Lookup","WHOIS","HTTP Headers","Port Check",
"Hash Generator","Metadata Reader","Robots Viewer","SSL Info","Username Check",
"Subdomain Scan","Password Strength","Log Analyzer","File Hash Verify","Config Viewer",
"Web Tech Detector","Security Header Audit","Email MX Lookup","Directory Probe","URL Batch Check",
"Google Dork Helper","Username Deep Search","Phone OSINT","Name OSINT","Multi Search"
]

    print(Fore.GREEN+"════════════════════════════════════════════════════")
    print(Fore.CYAN+"                AVAILABLE MODULES")
    print(Fore.GREEN+"════════════════════════════════════════════════════\n")

    colors=[Fore.CYAN,Fore.YELLOW,Fore.MAGENTA]

    for i in range(0,len(tools),3):

        row=tools[i:i+3]
        line=""

        for j,x in enumerate(row):
            idx=i+j+1
            block=f"[ {idx:02} ] {x}"
            line+=colors[j%3]+f"{block:<32}"

        print(line)

    print(Fore.GREEN+"\n════════════════════════════════════════════════════")
    print(Fore.WHITE+"Select Module → ",end="")



# ================= RUN =================

def run_tool(c):

    mapping={
1:modules.ipinfo.run,
2:modules.dns.run,
3:modules.whois.run,
4:modules.headers.run,
5:modules.port.run,
6:modules.hash.run,
7:modules.meta.run,
8:modules.robots.run,
9:modules.ssl.run,
10:modules.username.run,
11:modules.subdomain.run,
12:modules.password.run,
13:modules.logscan.run,
14:modules.filehash.run,
15:modules.configview.run,
16:modules.webtech.run,
17:modules.secaudit.run,
18:modules.mxlookup.run,
19:modules.dirprobe.run,
20:modules.urlbatch.run,
21:modules.googledork.run,
22:modules.userdeep.run,
23:modules.phoneosint.run,
24:modules.nameosint.run,
25:modules.megasearch.run
}

    if c in examples:
        print(Fore.YELLOW+"\n"+examples[c])

    if c in mapping:
        mapping[c]()
    else:
        print("Invalid selection")


# ================= MAIN =================

while True:

    banner()
    menu()

    try:
        c=int(input())
        run_tool(c)
    except:
        print("Input error")

    input(Fore.GREEN+"\nENTER...")
