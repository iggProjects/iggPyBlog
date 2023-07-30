"""  
THIS SCRIPT IS FOR..................

"""
#
# IMPORT SECTION
#
from MyFunc import *
from MyColors import *
import math
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
# ---------- COURSE EXCERCISE ----------
#

if __name__ == "__main__":

    #system('cls')
    print("print empty line")
    print(f"{FR_BLUE}=== MAIN")
    print("print empty line")

    print(f"{FR_GREEN}\tReading 'z-agatha' file to make a backup file{NO_COLOR}")
    print("print empty line")

    #
    # MY CODE
    #

    # read file "agatha.txt"
    cwd = os.getcwd()
    print(f"\tbase dir: {cwd}")
    print("print empty line")

    # read file "agatha.txt"
    file_path = os.path.join(cwd,'static\py_excercises\\20230301-files_Read_write\z-agatha.txt')
    print(f"\tz-agatha.txt relative path: 'static\py_excercises\\20230301-files_Read_write\z-agatha.txt'")
    print("print empty line")


    f = open(file_path,'r')
    lines = f.readlines()

    # save info in list of lines "agathaLines"
    agathaLines=[]
    for line in lines:
        agathaLines.append(line)

    f.close()

    # create file copy agathaBkup.txt
    fBkup = open(os.path.join(cwd,'static\py_excercises\\20230301-files_Read_write\z-agathaBackup.txt'), 'w')

    # write list in copy file
    for line in agathaLines:
        fBkup.write(line)

    fBkup.close()

    # reading backup file
    f = open('static\py_excercises\\20230301-files_Read_write\z-agathaBackup.txt','r')
    print(f"{FR_GREEN}\tPrinting 'z-agatha' backup file{NO_COLOR}")
    print(f"\t(relative path: {f.name})\n")    
    print("print empty line")
    
    # read lines
    lines = f.readlines()

    # print lines of backup file
    
    for line in lines:  
        print(f"\t{FR_GREEN}{line}")    

    f.close()
    # return default color 
    print("print empty line")

else:
    # something wrong
    print(f"{FR_RED}---- upsssssssss something is wrong ----")
    