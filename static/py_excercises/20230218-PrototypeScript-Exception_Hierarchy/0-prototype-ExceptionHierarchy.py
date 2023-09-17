
"""  
THIS SCRIPT IS FOR PRINTING WITH COLORS

"""
# IMPORT SECTION

import os, sys
from os import  system

# Include root path in sys.path
ROOT_DIR = os.path.abspath(os.curdir)
sys.path.insert(1, ROOT_DIR)

# Import My Own Funct in root path
from MyFunc import *


# CONSTANTS

#
# ---------- MAIN ----------
#

if __name__ == "__main__":

    import inspect
    
    system('cls')
    print(frGREEN("\n---------- main ----------\n"))

    print(frGREEN("\n---------- Exception Hierarchy ----------\n"))
    
    print(frRED("The class hierarchy for built-in exceptions is:"))
    print()

    #
    inspect.getclasstree(inspect.getmro(Exception))
    classtree(Exception)
    
    print(f"\n{FR_GREEN}---------- That's all for today 👌 ----------{NO_COLOR}\n")
    

    # ------------------------------------------------
    #           ASKING FOR SHOW VARS INFO 
    #------------------------------------------------- 
    """
    # with Y_N_2 function
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
            # pause()
            # my objects functions  
            mostrar(_my_Obj_name)       

        except NameError:
            print(f"\n\t{FR_RED}---- Var '{_what_var}' doesn't exits 🙄🙄  ----")
            print(f"\n{FR_GREEN}--------------- That's all for today 👌 ---------------{NO_COLOR}\n")
            #_my_Obj_name = None 

    else:
        print(f"\n{FR_GREEN}---------- That's all for today 👌 ----------{NO_COLOR}\n")
    """

else:
    # something wrong
    print(frRED("\n---- upsssssssss something is wrong 😢😢  ----\n"))
    # pause()