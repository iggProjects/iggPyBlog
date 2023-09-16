"""  
THIS SCRIPT IS FOR..................

"""
#
# IMPORT SECTION
#

import os, sys, platform
from os import  system

# Include root path in sys.path
ROOT_DIR = os.path.abspath(os.curdir)
sys.path.insert(1, ROOT_DIR)

# Import My Own Funct in root path
from MyFunc import *

# CONSTANTS

#
# ---------- COURSE EXCERCISE ----------
#

if __name__ == "__main__":
    #print(f"\n{Fore.RED}---------- main ----------{Style.RESET_ALL}\n")
    system('cls')
    print(f"\n{FR_GREEN}---------- MAIN ----------{NO_COLOR}\n")
    pause()
    # my code    
    myPath = os.getcwd()
    f = []
    for (dirpath, dirnames, filenames) in os.walk(myPath):
        f.extend(filenames)
        break
    print(f"{FR_GREEN}Path: {myPath}")
    print()
    print(f"{FR_GREEN}FILES IN {myPath}: ")
    print()
    matrix_view(f,3)
    print()
    pause()

    parent = os.chdir('../')
    parentPath = os.getcwd()
    print(f"{FR_GREEN}parent path: {parentPath}")
    f = []
    d = []
    for (dirpath, dirnames, filenames) in os.walk(parentPath):
        f.extend(filenames)
        d.extend(dirnames)
        break

    print()
    print(f"{FR_GREEN}DIRS IN {parentPath}: ")
    print()
    matrix_view(d,3)
    print()
    print(f"{FR_GREEN}FILES IN {parentPath}: ")
    print()
    matrix_view(f,3)

    print(f"\n{FR_GREEN}---------- THAT'S ALL ----------{NO_COLOR}\n")
   

else:
    # something wrong
    print(f"\n{FR_RED}---- upsssssssss something is wrong 😢😢  ---{NO_COLOR}\n")
    pause()

