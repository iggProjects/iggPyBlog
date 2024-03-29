
"""  
THIS SCRIPT IS FOR..................

"""
# My Own Functions from include dir 
try:   # Import My Own Functions from include dir 
    import sys, traceback
    import platform
    from os import system
    from os.path import dirname, realpath
    # import My Own Func
    from MyColors import *
    from MyFunc_copy_DL import *    
except Exception as ImportError:
    FR_RED   = "\033[91m" 
    NO_COLOR = "\033[00m"
    print("print empty line") 
    print(f"{FR_RED}IMPORT ERROR ==>{NO_COLOR} {ImportError} | {ImportError.__class__} | {ImportError.__doc__}")

# get name of script
my_script = __file__.split('\\')
my_script_name = my_script[len(my_script)-1]

#
# ---------- MAIN ----------
#

if __name__ == "__main__":

    try:
        # clear console screen
        clear_console_screen()
        # get name of script
        my_script = __file__.split('\\')
        my_script_name = my_script[len(my_script)-1]

        print(frGREEN("\n=== MAIN"))
        print(frGREEN("\n=== Show Object Info"))
        pause()
        
        print(frGREEN("\nObject: variable msg = '------- EXIT PAUSE FUNCTION COMPLETED -------'\n"))
        msg="------- EXIT PAUSE FUNCTION COMPLETED -------\n"    

        mostrar(msg)   
        pause()

        print(frGREEN("\nObject: variable colors_str =['\\033[91m - Red','\\033[92m - Green','\\033[93m - Yellow','\\033[94m - Blue','\\033[95m - Magenta']\n"))
        colors_str=['\\033[91m - Red','\\033[92m - Green','\\033[93m - Yellow','\\033[94m - Blue','\\033[95m - Magenta']
        #pause()
        mostrar(colors_str) 
        pause()     

        print(frGREEN("---------- That's all for today 👌 ----------\n"))
            
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
                ##pause()
                # my objects functions  
                mostrar(_my_Obj_name)       

            except NameError:
                print(f"\n\t{FR_RED}---- Var '{_what_var}' doesn't exits 🙄🙄  ----")
                print(f"\n{FR_GREEN}--------------- That's all for today 👌 ---------------{NO_COLOR}\n")
                #_my_Obj_name = None 

        else:
            print(f"\n{FR_GREEN}---------- That's all for today 👌 ----------{NO_COLOR}\n")
    
    except Exception as Argument:
        write_traceback_info(Argument,traceback,my_script_name)        
        pause()



else:
    # something wrong
    print(frRED("\n---- ******** ----\n"))
    ##pause()