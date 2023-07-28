
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
    print(frGREEN("---------- main ----------"))
    prBlue("---------- help for object 'list' ----------")
    print("print empty line")

    my_obj = [1,2,3,4,5]
    print("my_obj = [1;2;3;4;5] ==> calling help_obj_method(my_obj) in MyFunc Module")
    print("print empty line")
    help_obj_method(my_obj)
    print("print empty line") 
    print(f"{FR_GREEN}---------- That's all for today ----------{NO_COLOR}")
    print("print empty line")

else:
    # something wrong
    print(frRED("---- upsssssssss something is wrong ----"))
    