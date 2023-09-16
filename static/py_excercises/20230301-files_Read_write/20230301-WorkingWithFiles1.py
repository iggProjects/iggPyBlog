"""  
THIS SCRIPT IS FOR..................

"""
#
# IMPORT SECTION
#
import os, sys, math

"""
cwd = os.cwd()
print(f"\tCWD: {cwd}")
print("print empty line")

"""

# include root path in sys.path
ROOT_DIR = os.path.abspath(os.curdir)
# check in what server is app
if "iggWebNz" in ROOT_DIR:              # pythonanywhere  
    ROOT_DIR = ROOT_DIR + "/mysite"
else:                                   # working in localhost server
    pass 
sys.path.insert(1, ROOT_DIR)

# import "My Own Funct" from root path
from MyFunc import *


# CONSTANTS

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

    # base dir
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
    