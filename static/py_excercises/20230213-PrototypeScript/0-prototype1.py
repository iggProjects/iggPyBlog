
"""  
THIS IS MY STANDAR SCRIPT TO CREATE NEWS SCRIPTS 

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

    print(f"{FR_GREEN}---------- prototype py model ----------{NO_COLOR}")

    print("print empty line")
    print("print empty line")

    print(f"{FR_BLUE}\t\t\t\t\t\t---------- USE DOWNLOAD OPTION ----------{NO_COLOR}")

    #
    # YOUR CODE
    #     

else:
    # something wrong
    print(f"{FR_GREEN}---- upsssssssss something is wrong ----{NO_COLOR}")
