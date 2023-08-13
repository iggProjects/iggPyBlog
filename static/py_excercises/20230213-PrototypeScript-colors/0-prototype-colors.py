
"""  
THIS SCRIPT IS FOR PRINTING WITH COLORS

"""


# IMPORT SECTION
# modules

from os import  system

# My functions
from MyFunc import *
from MyColors import *

# CONSTANTS

#
# ---------- MAIN ----------
#

if __name__ == "__main__":

    try:    

        write_log_file("my_messages.log","IN 'func 0-prototype-colors.py()'")

        system('cls')
        print(frGREEN("\n---------- main ----------\n"))

        print(frGREEN("\n---------- using CONTANTS ----------\n"))
        pause()
        colors= [FR_RED,FR_GREEN,FR_YELL,FR_BLUE,FR_MAG]
        colors_str=['\\033[91m - Red','\\033[92m - Green','\\033[93m - Yellow','\\033[94m - Blue','\\033[95m - Magenta']
        
        i=0
        for color in colors:
            color_str = color
            msg=" ==> TESTING COLOR FUNCTION"
            #print("FR_RED value: " + colors_str[0])
            print("\tPrint with ascii " + colrs_str[i] + f":\t{color}{msg}{NO_COLOR}") 
            i+=1   

        msg="print with default color\t\t ==> TESTING COLOR FUNCTION"
        print(f"\t{msg}")    

        msg="\tprint with function pfRed() --> TESTING COLOR FUNCTION"
        print(frGREEN("\n---------- using function prRed(msg) ----------\n"))
        pause()
        prRed(msg)   

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

    except Exception as Argument: 
        #logging.info(Argument)  
        logging.exception(" | exception from '0-prototype-colors.py()': ")

else:
    # something wrong
    print(frRED("\n---- upsssssssss something is wrong 😢😢  ----\n"))
    # pause()

