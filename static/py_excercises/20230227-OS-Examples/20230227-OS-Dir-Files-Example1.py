"""  
THIS SCRIPT IS FOR..................

"""
#
# IMPORT SECTION
#

import os
import platform

#  my own functions
from MyFunc import *
# my colors functions&contants,
from MyColors import *
# from colorama import Fore, Back, Style
from os import  system

# CONSTANTS
# Colors
NO_COLOR = "\033[00m"
FR_RED   = "\033[91m"
FR_GREEN = "\033[92m"
FR_YELL  = "\033[93m"
FR_BLUE  = "\033[94m"
FR_MAG   = "\033[95m"

#
# ---------- COURSE EXCERCISE ----------
#

if __name__ == "__main__":

    #print(f"{Fore.RED}---------- main ----------{Style.RESET_ALL}")
    print("print empty line")
    print(f"{FR_GREEN}=== MAIN")
    print("print empty line")
 
    # my code    
    myPath = os.getcwd()
    f = []
    for (dirpath, dirnames, filenames) in os.walk(myPath):
        f.extend(filenames)
        break
    print(f"{FR_GREEN}Path: {myPath}")
    print("print empty line")
    print(f"{FR_GREEN}FILES IN {myPath}: ")
    print("print empty line")
    matrix_view(f,3)
    print("print empty line")

    parent = os.chdir('../')
    parentPath = os.getcwd()
    print(f"{FR_GREEN}parent path: {parentPath}")
    f = []
    d = []
    for (dirpath, dirnames, filenames) in os.walk(parentPath):
        f.extend(filenames)
        d.extend(dirnames)
        break

    print("print empty line")
    print(f"{FR_GREEN}DIRS IN {parentPath}: ")
    print("print empty line")
    matrix_view(d,3)
    print("print empty line")
    print(f"{FR_GREEN}FILES IN {parentPath}: ")
    print("print empty line")
    matrix_view(f,3)

 
    print(f"----------------- That's All -----------------")

    # Library methods info 
    #library_methods(os)
    #library_methods(platform)
  

else:
    # something wrong
    print(f"----- upsssssssss something is wrong -----")


