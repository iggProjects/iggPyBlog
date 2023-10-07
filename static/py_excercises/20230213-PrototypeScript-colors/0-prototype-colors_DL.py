
"""  
THIS SCRIPT IS FOR PRINTING WITH COLORS

ONLY WORK IN LOCALHOST

"""
# IMPORT SECTION

# My Own Functions from include dir 
try:   # Import My Own Functions from include dir 
    import sys, traceback     
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

#
# ---------- MAIN ----------
#

if __name__ == "__main__":

    try:    

        system('cls')
        # get name of script
        my_script = __file__.split('\\')
        my_script_name = my_script[len(my_script)-1]

        print(frGREEN("\n---------- main ----------\n"))

        print(frGREEN("\n---------- using CONTANTS ----------\n"))
        pause()

        colors= [FR_RED,FR_GREEN,FR_YELL,FR_BLUE,FR_MAG]
        colors_str=['\\033[91m - Red','\\033[92m - Green','\\033[93m - Yellow','\\033[94m - Blue','\\033[95m - Magenta']
        
        i=0
        for color in colors:
            color_str = color
            msg=" ==> TESTING COLOR FUNCTION"            
            print("\tPrint with ascii " + colors_str[i] + f":\t{color}{msg}{NO_COLOR}") 
            i+=1   

        print()
        msg="print with default color\t\t ==> TESTING COLOR FUNCTION"
        print(f"\t{msg}")    

        print(frGREEN("\n---------- using function prRed(msg) ----------\n"))
        msg="\tprint with function pfRed() --> TESTING COLOR FUNCTION\n"        
        prRed(msg)   
        pause()

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

            #except Exception as Argument:
            except Exception as Argument:
                #print(f"\n\t{FR_RED}---- FROM 'WHAT VAR ?': {NameError}' 🙄🙄  ----")
                print(f"\n\t{FR_RED}---- FROM 'WHAT VAR ?': {Argument}' | {Argument.__class__} 🙄🙄  ----")
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
    # pause()

