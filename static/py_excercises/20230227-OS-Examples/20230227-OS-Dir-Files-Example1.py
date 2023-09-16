"""  
THIS SCRIPT IS FOR..................

"""
#
# IMPORT SECTION
#

import os, sys, platform

# include root path in sys.path
ROOT_DIR = os.path.abspath(os.curdir)
# check in what server is app
if "iggWebNz" in ROOT_DIR:              # pythonanywhere  
    ROOT_DIR = ROOT_DIR + "/mysite"
else:                                   # working in localhost server
    pass 
sys.path.insert(1, ROOT_DIR)

# import "My Own Funct" from root path
from MyFunc import *

# CONSTANTS

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


