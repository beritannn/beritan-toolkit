import ssl, socket
from core.ui import *

def run():
    host=input("Domain: ")

    ctx=ssl.create_default_context()

    try:
        with ctx.wrap_socket(socket.socket(), server_hostname=host) as s:
            s.connect((host,443))
            cert=s.getpeercert()

            info("Issuer:")
            print(cert['issuer'])

            info("Valid From:")
            print(cert['notBefore'])

            info("Valid To:")
            print(cert['notAfter'])

    except:
        bad("SSL lookup failed")
