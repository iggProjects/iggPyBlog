
"""  
THIS SCRIPT IS FOR PRINTING WITH COLORS

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

    import inspect

    print("print empty line")
    print(f"{FR_GREEN}---------- main ----------{NO_COLOR}")
    print("print empty line")

    print(frGREEN("\n---------- Exception Hierarchy ----------\n"))    
    print(frRED("The class hierarchy for built-in exceptions is:"))
    print("print empty line")

    # 
    inspect.getclasstree(inspect.getmro(Exception))
    classtree(Exception)

    print("print empty line")
    print(f"{FR_GREEN}---------- That's all for today ----------{NO_COLOR}")
    print("print empty line")

else:
    # something wrong
    print(frRED("---- upsssssssss something is wrong ----"))
