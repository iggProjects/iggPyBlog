
"""  
THIS SCRIPT IS FOR..................

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
    print(frGREEN("\n--------------- pause() called --------------\n"))

    msg="------- EXIT PAUSE FUNCTION COMPLETED -------\n"
    prGreen(msg)   

    print(f"\n{FR_GREEN}---------- That's all for today 👌 ----------{NO_COLOR}\n")


else:
    # something wrong
    print(frRED("\n---- upsssssssss something is wrong 😢😢  ----\n"))
    pause()