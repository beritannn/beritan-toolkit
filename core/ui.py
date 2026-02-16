from colorama import Fore

def good(msg):
    print(Fore.GREEN + msg)

def bad(msg):
    print(Fore.RED + msg)

def info(msg):
    print(Fore.CYAN + msg)

def warn(msg):
    print(Fore.YELLOW + msg)
