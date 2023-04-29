"""  
THIS SCRIPT IS FOR DELETE REPEATED LINES AND SORT RESULTING FILE

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

    import os

    system('cls')
    print(f"{FR_GREEN}---------- main ----------")

    base_dir = os.path.dirname("/baz/foo")
    print(f"base dir: {base_dir}")
        
    file = open("z-fileRepeatedLines.txt","r")
    print(f"{FR_BLUE}\tRead and print '{file.name}'")
    # read lines
    lines = file.readlines()
    # print lines of backup file    
    for line in lines:  
        print(f"\t\t{line}")
    file.close()

    print(f"{FR_BLUE}\tRead 'file z-fileRepeatedLines.txt' with 'uniqlines = set('z-fileRepeatedLines.txt').readlines'")
    uniqlines = set(open('z-fileRepeatedLines.txt').readlines())
    print(f"\tuniqlines before: {uniqlines}")

    print(f"{FR_BLUE}\tSort \"uniqlines\" with sorted(uniqlines)")
    uniqlines = sorted(uniqlines)

    print(f"\tuniqlines type is {type(uniqlines)}")
    print(f"\tuniqlines after: {uniqlines}")

    print(f"{FR_BLUE}\tWrite List \"uniqlines\" in file \"z-fileWithOutRepetitionLines.txt\"")
    open('z-fileWithOutRepetitionLines.txt', 'w').writelines(uniqlines)

