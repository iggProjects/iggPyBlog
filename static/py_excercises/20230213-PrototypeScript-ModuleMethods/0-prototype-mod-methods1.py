
"""  
THIS SCRIPT IS FOR..................

"""
# IMPORT SECTION
from MyFunc import *
from MyColors import *
import os
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
# ---------- MAIN ----------
#

if __name__ == "__main__":

    print("print empty line")
    print(f"{FR_BLUE}=== MAIN")    
    print("print empty line")
    print(f"{FR_GREEN}=== List of OS module methods")
    print("print empty line")
    library_methods(os)    
    print("print empty line")
    print(f"{FR_GREEN}=== That's all for today ===")

else:
    # something wrong
    print(f"{FR_RED}---- upsssssssss something is wrong  ----")
    