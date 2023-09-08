
"""  
THIS SCRIPT IS FOR PRINTING WITH COLORS

"""
# IMPORT SECTION
import logging

import os
from os import  system
import sys

# My Own Funct in root path
ROOT_DIR = os.path.abspath(os.curdir)
sys.path.insert(1, ROOT_DIR)
from MyFunc import *

# CONSTANTS

#
# ---------- MAIN ----------
#

if __name__ == "__main__":

    try:

        write_log_file("my_messages.txt","IN 'func 0-prototype-colors1.py()'")
        print("print empty line")

        print(f"{FR_GREEN}---------- MAIN ----------{NO_COLOR}")

        print(f"---------- using CONTANTS for colors ----------")

        colors= [FR_RED,FR_GREEN,FR_YELL,FR_BLUE,FR_MAG]
        colors_str=['\\033[91m - Red','\\033[92m - Green','\\033[93m - Yellow','\\033[94m - Blue','\\033[95m - Magenta']
        
        i=0
        for color in colors:
            color_str = color
            msg=" ==> TESTING COLOR FUNCTION"
            msg = msg.rjust(30)
            #print("FR_RED value: " + colors_str[0])
            print("\tPrint with ascii " + colors_str[i] + f":\t{color}{msg}") 
            i+=1   

        msg="print with default color:\t\t ==> TESTING COLOR FUNCTION"
        print(f"\t{msg}")    

        msg="\tprint with function pfRed(msg) --> TESTING COLOR FUNCTION"
        print(frGREEN(f"---------- using function prRed(msg) ----------"))    
        prRed(msg)   
        
        print(f"{FR_GREEN}---------- That's all for today ----------{NO_COLOR}")

    except Exception as Argument:  
        write_log_file("my_messages.log","ERROR IN 'func 0-prototype-colors1.py()'. SEE server_messages.log")
        print("print empty line")
        print(frRED(f"UPSSSS THERE IS AN ERROR IN 'func 0-prototype-colors1.py()'."))
        print("print empty line")
        print(frRED(f"SEE 'server_messages.log' file OR Contact Web Admin !"))
        print("print empty line")
        logging.exception(" | exception from '0-prototype-colors.py()': ")
    
else:
    # something wrong
    print(frRED("---- upsssssssss something is wrong ----"))
