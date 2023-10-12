
"""  
THIS IS MY STANDAR SCRIPT TO CREATE NEWS SCRIPTS 

"""
# IMPORT SECTION

try:   # Import My Own Functions from include dir 
    import sys, traceback, platform     
    from os.path import dirname, realpath
    from os import system
    # get parent up 2 from __file__ path: 'static path'   
    up2_dir = dirname(dirname(dirname(realpath(__file__))))
    # insert path in sys.path
    sys.path.append(up2_dir)
    # get parent up 3 from __file__ path: 'static parent path'       
    up3_dir = dirname(dirname(dirname(dirname(realpath(__file__)))))
    # insert path in sys.path
    sys.path.append(up3_dir)
    # import My Own Func
    from static.include.MyFunc import *
    from static.include.MyColors import *
except Exception as ImportError:
    FR_RED   = "\033[91m" 
    NO_COLOR = "\033[00m"
    print() 
    print(f"{FR_RED}IMPORT ERROR ==>{NO_COLOR} {ImportError} | {ImportError.__class__} | {ImportError.__doc__}")

#
# ---------- MAIN ----------
#

if __name__ == "__main__":
        
    try:    

        # clear screen
        import platform
        if platform.system() == 'Windows':
            system('cls')
        elif platform.system() == 'Linux':
            system('clear')
        else:
            print(frGREEN("\n---------- MAIN ----------\n"))

        write_log_file("my_messages.txt","IN 'func 0-prototype.py()'")

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