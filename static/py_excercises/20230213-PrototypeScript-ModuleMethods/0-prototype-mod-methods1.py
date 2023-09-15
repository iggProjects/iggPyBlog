
"""  
THIS SCRIPT IS FOR..................

"""
# IMPORT SECTION
import os, sys
from os import  system

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
# ---------- MAIN ----------
#

if __name__ == "__main__":

    print("print empty line")
    print(f"=== MAIN ===")
    print("print empty line")
    print(f"{FR_GREEN}=== List of OS module methods{NO_COLOR}")
    print("print empty line")
    library_methods(os)    
    print("print empty line")
    print(f"{FR_GREEN}=== That's all for today ===")

else:
    # something wrong
    print(f"{FR_RED}---- upsssssssss something is wrong  ----")
    