"""  
THIS SCRIPT IS FOR..................

"""
#
# IMPORT SECTION
#
from MyFunc import *
from MyColors import *
import math
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
# ---------- COURSE EXCERCISE ----------
#

if __name__ == "__main__":

    system('cls')
    print(f"{FR_GREEN}---------- main ----------")
    

    #
    # MY CODE
    #

    # read file "agatha.txt"
    f = open("agatha.txt","r")
    #f = open(agatha.txt,"r")
    lines = f.readlines()

    # save info in list of lines "agathaLines"
    agathaLines=[]
    for line in lines:
        agathaLines.append(line)

    f.close()

    # create file copy agathaBkup.txt
    fBkup = open("agathaBackup.txt", "w")

    # write list in copy file
    for line in agathaLines:
        fBkup.write(line)

    fBkup.close()

    # reading backup file
    f = open("agathaBackup.txt","r")
    print(f"{FR_YELL}\tprinting backup file: {f.name}")

    # read lines
    lines = f.readlines()

    # print lines of backup file
    print("\033[34m")
    for line in lines:  
        print(f"\t{FR_GREEN}{line}")

    f.close()
    # return default color 
    print(f"")

    

else:
    # something wrong
    print(f"{FR_RED}---- upsssssssss something is wrong ----")
    