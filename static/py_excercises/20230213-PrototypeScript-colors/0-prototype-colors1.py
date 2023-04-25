
"""  
THIS SCRIPT IS FOR PRINTING WITH COLORS

"""
# IMPORT SECTION
from MyFunc import *
from MyColors import *
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

    print(f"{FR_GREEN}---------- main ----------{NO_COLOR}")

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

else:
    # something wrong
    print(frRED("---- upsssssssss something is wrong ----"))
