
"""  
THIS SCRIPT IS FOR PRINTING WITH COLORS

ONLY WORK IN LOCALHOST

"""


# IMPORT SECTION
import os, sys, logging, traceback
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

    try:    

        system('cls')
        print(frGREEN("\n---------- main ----------\n"))

        print(frGREEN("\n---------- using CONTANTS ----------\n"))
        pause()
        colors= [FR_RED,FR_GREEN,FR_YELL,FR_BLUE,FR_MAG]
        colors_str=['\\033[91m - Red','\\033[92m - Green','\\033[93m - Yellow','\\033[94m - Blue','\\033[95m - Magenta']
        
        i=1/0
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
        print(frRED(f"-------- upsssssssss: ERROR in '0-prototype-colors.py()' | {Argument}--------\n"))
        logging.exception(" | exception from '0-prototype-colors.py()': ")

        
        print("traceback")
        print(f"{traceback.format_exc()}")
        print()

        traceback_formatted = traceback.format_exc().replace('"','').replace(',','|')
        traceback_lines = traceback_formatted.split('\n')
        print(f"traceback_lines length: {len(traceback_lines)}")
        print(f"{traceback_lines}")
        print()

        for line in traceback_lines:
            print(f"{line}")    


        print("traceback_lines[1]")
        print(f"{traceback_lines[1]}")    
        print()

        traceback_lines_2 = traceback_lines[1].split('|')
        print("traceback_lines_2")
        print(f"{traceback_lines_2}")
        print()

        #traceback_lines_2_2 = traceback_lines_2[2].split('|')
        print("traceback_lines_2_2")        
        print(traceback_lines_2[1])
        


else:
    # something wrong    
    print(frRED("\n---- upsssssssss something is wrong 😢😢  ----\n"))
    # pause()

