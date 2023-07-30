"""  
THIS SCRIPT IS FOR DELETE REPEATED LINES AND SORT RESULTING FILE

"""
#
# IMPORT SECTION
#
from MyFunc import *
from MyColors import *
import math
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

    import os

    system('cls')
    print(f"\n{FR_BLUE}=== MAIN{NO_COLOR}\n")
    #pause()

    cwd = os.getcwd()
    print(f"cwd: {cwd}")
    #base_dir = os.path.dirname(os.getcwd())
    #print(f"base dir: {base_dir}")
    file_path = os.path.join(cwd, 'static\py_excercises\\20230301-DelRepeatedLinesAndSort\z-fileRepeatedLines.txt')
    # static\py_excercises\20230301-DelRepeatedLinesAndSort\20230301-DelRepeatedLinesAndSort.py
    print(f"file: {file_path}")
    file = open(file_path,"r")
    #file = open("z-fileRepeatedLines.txt","r")
    print(f"\n{FR_YELL}\tRead and print '{file.name}'{NO_COLOR}\n")
    # read lines
    lines = file.readlines()
    # print lines of backup file    
    for line in lines:  
        print(f"\t\t{line}")
    file.close()

    print(f"{FR_YELL}\tRead 'file z-fileRepeatedLines.txt' with 'uniqlines = set('z-fileRepeatedLines.txt').readlines'{NO_COLOR}\n")
    uniqlines = set(open('static\py_excercises\\20230301-DelRepeatedLinesAndSort\z-fileRepeatedLines.txt').readlines())
    uniqlines_bef = str(uniqlines).replace(',',';').replace('\\n','')
    print(f"\tuniqlines before: {uniqlines_bef}\n")

    print(f"{FR_YELL}\tSort \"uniqlines\" with sorted(uniqlines){NO_COLOR}\n")
    uniqlines = sorted(uniqlines)
    uniqlines_aft = str(uniqlines).replace(',',';').replace('\\n','')

    print(f"\tuniqlines type is {type(uniqlines)}\n")
    print(f"\tuniqlines after: {uniqlines_aft}\n")

    print(f"{FR_YELL}\tCheck sorted file \"z-fileWithOutRepetitionLines.txt\"\n")
    open('static\py_excercises\\20230301-DelRepeatedLinesAndSort\z-fileWithOutRepetitionLines.txt', 'w').writelines(uniqlines)

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
            print(f"\n{FR_GREEN}---------- INFO FOR OBJECT '{_my_Obj_name}' ----------{NO_COLOR}\n")
            pause()
            # my objects functions  
            mostrar(_my_Obj_name)       

        except NameError:
            print(f"\n\t{FR_RED}---- Var '{_what_var}' doesn't exits 🙄🙄  ----")
            print(f"\n{FR_GREEN}--------------- That's all for today 👌 ---------------{NO_COLOR}\n")

    else:
        print(f"\n{FR_GREEN}---------- That's all for today 👌 ----------{NO_COLOR}\n")
