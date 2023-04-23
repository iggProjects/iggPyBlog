
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

    system('cls')
    print(frGREEN("\n---------- main ----------\n"))

    print(frGREEN("\n---------- using CONTANTS ----------\n"))
    colors= [FR_RED,FR_GREEN,FR_YELL,FR_BLUE,FR_MAG]
    colors_str=['\\033[91m - Red','\\033[92m - Green','\\033[93m - Yellow','\\033[94m - Blue','\\033[95m - Magenta']
    
    i=0
    for color in colors:
        color_str = color
        msg="--> TESTING COLOR FUNCTION"
        #print("FR_RED value: " + colors_str[0])
        print("\tPrint with ascii " + colors_str[i] + f":\t{color}{msg}{NO_COLOR}") 
        i+=1   

    msg="print with default color\t\t--> TESTING COLOR FUNCTION"
    print(f"\t{msg}")    

    msg="\tprint with function pfRed() --> TESTING COLOR FUNCTION"
    print(frGREEN("\n---------- using function prRed(msg) ----------\n"))    
    prRed(msg)   
    
    print(f"\n{FR_GREEN}---------- That's all for today 👌 ----------{NO_COLOR}\n")

else:
    # something wrong
    print(frRED("\n---- upsssssssss something is wrong 😢😢  ----\n"))
