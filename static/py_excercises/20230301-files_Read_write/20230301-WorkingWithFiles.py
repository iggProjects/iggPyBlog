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
from os import system

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
    print(f"\n{FR_BLUE}---------- MAIN ----------{NO_COLOR}\n")

    #
    # MY CODE
    #

    cwd = os.getcwd()
    print(f"\ncwd: {cwd}\n")

    # read file "agatha.txt"
    file_path = os.path.join(cwd,'static\py_excercises\\20230301-files_Read_write\z-agatha.txt')
    f = open(file_path,'r')
    #f = open(agatha.txt,"r")
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
    print(f"\n{FR_YELL}\tPrinting 'z-agatha' backup file{NO_COLOR}\n\n\t(relative path: {f.name})\n")

    # read lines
    lines = f.readlines()

    # print lines of backup file
    print("\033[34m")
    for line in lines:  
        print(f"\t{FR_GREEN}{line}")

    f.close()
    # return default color 
    print(f"{NO_COLOR}")

    
    # ------------------------------------------------
    #          SHOW VARS CHARACTERISTICS 
    #------------------------------------------------ 
    yesss=True   
    while yesss:
        _msg = "Do you want to see attributes for a specific VAR ? (Y,N): "
        answer=Y_N_2(_msg)        
        if answer in ['Y','N']: yesss = False

    if answer == 'Y':            
        # add question for name of var.....
        _what_var = str(input("What VAR ? "))
        try: 
            _what_var
            _my_Obj_name = eval(_what_var)
            print(f"\n{FR_GREEN}---------- INFO FOR OBJECT\n'{_my_Obj_name}' ----------{NO_COLOR}\n")
            pause()
            # my objects functions  
            mostrar(_my_Obj_name)       

        except NameError:
            print(f"\n\t{FR_RED}---- Var '{_what_var}' doesn't exits ----")
            print(f"\n{FR_GREEN}--------------- That's all for today  ---------------{NO_COLOR}\n")

    else:
        print(f"\n{FR_YELL}---------- That's all for today  ----------{NO_COLOR}\n")

else:
    # something wrong
    print(f"\n{FR_RED}---- upsssssssss something is wrong 😢😢  ---{NO_COLOR}\n")
    pause()