import os
import time
from core.ui import *

def run():
    path=input("File path: ")

    try:
        stat=os.stat(path)

        info("Size: "+str(stat.st_size))
        info("Created: "+time.ctime(stat.st_ctime))
        info("Modified: "+time.ctime(stat.st_mtime))
        info("Accessed: "+time.ctime(stat.st_atime))

    except:
        bad("File not found")
