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

    #system('cls')
    print("print empty line")
    print(f"{FR_BLUE}=== MAIN")
    print("print empty line")
    base_dir = os.path.dirname(os.getcwd())
    print(f"base dir: {base_dir}")
    print("print empty line")
        
    #file = open("z-fileRepeatedLines.txt","r")
    file = open("static\py_excercises\\20230301-DelRepeatedLinesAndSort\z-fileRepeatedLines.txt")
    print(f"{FR_GREEN}Read and print '{file.name}'")
    # read lines
    lines = file.readlines()
    # print lines of backup file    
    for line in lines:  
        print(f"\t{line}")
    file.close()
    print("print empty line")

    print(f"{FR_GREEN}Read file 'z-fileRepeatedLines.txt' with command <uniqlines = set('z-fileRepeatedLines.txt').readlines>")
    uniqlines = set(open('static\py_excercises\\20230301-DelRepeatedLinesAndSort\z-fileRepeatedLines.txt').readlines())
    uniqlines_bef = str(uniqlines).replace(',',';').replace('\\n','')
    print(f"\tuniqlines type is {type(uniqlines)}")
    print(f"\tuniqlines before: {uniqlines_bef}")
    print("print empty line")

    print(f"{FR_GREEN}Sort 'uniqlines' with sorted(uniqlines)")
    uniqlines = sorted(uniqlines)
    uniqlines_aft = str(uniqlines).replace(',',';').replace('\\n','')
    print(f"\tuniqlines after: {uniqlines_aft}")
    print("print empty line")

    print(f"{FR_GREEN}\tCheck sorted file 'z-fileWithOutRepetitionLines.txt'")
    open('static\py_excercises\\20230301-DelRepeatedLinesAndSort\z-fileWithOutRepetitionLines.txt', 'w').writelines(uniqlines)
    print(f"{NO_COLOR}")

