"""  
THIS SCRIPT IS FOR..................

"""
#
# IMPORT SECTION
#
#import MyFunctions.MyFunc as MyFunc
#import MyFunctions.Colors_out as Col
import math
import os
import platform

from colorama import Fore, Back, Style

from MyFunc_ForTeacher import *
from Colors_ForTeacher import *

#
# ---------- COURSE EXCERCISE ----------
#

if __name__ == "__main__":
    #print(f"\n{Fore.RED}---------- main ----------{Style.RESET_ALL}\n")
    print(f"\n{FR_GREEN}---------- main ----------{NO_COLOR}\n")
    pause()

    # my code    
    myPath = os.getcwd()
    f = []
    for (dirpath, dirnames, filenames) in os.walk(myPath):
        f.extend(filenames)
        break
    print(f"{FR_GREEN}path -->{NO_COLOR} {myPath}\n")
    matrix_view(f,3)
    print(f"\n------------------------------------------------\n")

    parent = os.chdir('../')
    parentPath = os.getcwd()
    print(f"{FR_GREEN}parent path -->{NO_COLOR} {parentPath}\n")
    f = []
    for (dirpath, dirnames, filenames) in os.walk(parentPath):
        f.extend(filenames)
        break
    matrix_view(f,3)
    print(f"\n------------------------------------------------\n")

    # Library methods info 
    pause()
    library_methods(os)
    pause()
    library_methods(platform)
   
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
            #_my_Obj_name = None 

    else:
        print(f"\n{FR_GREEN}---------- That's all for today 👌 ----------{NO_COLOR}\n")

else:
    # something wrong
    print(f"\n{FR_RED}---- upsssssssss something is wrong 😢😢  ---{NO_COLOR}\n")
    pause()