
"""  
THIS IS MY STANDAR SCRIPT TO CREATE NEWS SCRIPTS 

"""
# IMPORT SECTION

# modules
import os, sys
from os import  system

# Include root path in sys.path
ROOT_DIR = os.path.abspath(os.curdir)
sys.path.insert(1, ROOT_DIR)

# Import My Own Funct in root path
from MyFunc import *

#
# ---------- MAIN ----------
#

if __name__ == "__main__":
        
    try:    

        write_log_file("my_messages.txt","IN 'func 0-prototype.py()'")

        system('cls')
        print(frGREEN("\n---------- MAIN ----------\n"))

        #
        # YOUR CODE
        #     

        # ------------------------------------------------
        #           ASKING FOR SHOW VARS INFO 
        #------------------------------------------------- 
        
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
                pause()
                # my objects functions  
                mostrar(_my_Obj_name)       

            except NameError:
                print(f"\n\t{FR_RED}---- Var '{_what_var}' doesn't exits 🙄🙄  ----")
                print(f"\n{FR_GREEN}--------------- That's all for today 👌 ---------------{NO_COLOR}\n")
                #_my_Obj_name = None 

        else:
            print(f"\n{FR_GREEN}---------- That's all for today 👌 ----------{NO_COLOR}\n")

    except Exception as Argument: 
        #logging.info(Argument)  
        logging.exception(" | exception from '0-prototype.py()': ")
        
    

else:
    # something wrong
    print(frRED("\n---- upsssssssss something is wrong 😢😢  ----\n"))
    pause()