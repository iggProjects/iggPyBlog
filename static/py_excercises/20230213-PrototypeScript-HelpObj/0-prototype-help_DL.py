
"""  
THIS SCRIPT EXECUTE HELP FUNCTION TO ANALYZE A CODE OBJECT

ONLY WORK IN LOCALHOST

"""

# My Own Functions from include dir 
try: 

    import sys, traceback
    from os.path import dirname, realpath
    from os import system
    # My Own Func
    from MyColors import *
    from MyFunc_copy_DL import *    

except Exception as ImportError:   
    print(f"IMPORT ERROR ==> {ImportError}")    


#
# ---------- MAIN ----------
#

if __name__ == "__main__":

    try:
        # clear console screen
        import platform
        clear_console_screen()
        # get name of script
        my_script = __file__.split('\\')
        my_script_name = my_script[len(my_script)-1]

        print(frGREEN("\n---------- main ----------\n"))
        prYellow("\n---------- help for object 'list' ----------\n")

        my_obj = [1,2,3,4,5]
        pause()
        help_obj_method(my_obj)
        
        print(f"\n{FR_GREEN}---------- That's all for today 👌 ----------{NO_COLOR}\n")

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
                    _my_Obj_name = " ".join(_my_Obj_name.split())
                    # " ".join(s.split())
                    print(f"\n{FR_GREEN}---- INFO FOR OBJECT ==> {NO_COLOR}'{ _my_Obj_name }'\n")
                    # pause()
                    # my objects functions  
                    mostrar(_my_Obj_name)       

                except Exception as Argument:
                #except NameError:
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
    print(frRED("\n---- upsssssssss something is wrong 😢😢  ----\n"))
    pause()