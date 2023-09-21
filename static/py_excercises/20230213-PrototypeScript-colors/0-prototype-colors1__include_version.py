
"""  
THIS SCRIPT IS FOR PRINTING WITH COLORS

"""
# IMPORT SECTION

import logging
import os, sys, traceback
from os import  system


# include root path in sys.path
ROOT_DIR = os.path.abspath(os.curdir)
# check in what server is app
if "iggWebNz" in ROOT_DIR:              # pythonanywhere  
    ROOT_DIR = ROOT_DIR + "/mysite"
else:                                   # working in localhost server
    pass 
#sys.path.insert(1, ROOT_DIR)

# get name of script
my_script = __file__.split('\\')
my_script_name = my_script[len(my_script)-1]


#print(f"----------------------- os.curdir --> {type(os.curdir)} | value: {os.curdir}")
#print(f"----------------------- os.path.abspath(os.curdir) --> {ROOT_DIR}")
#print(f"----------------------- os.getcwd() --> {os.getcwd()}")

# import "My Own Funct" from root path
#from MyFunc1 import *
try:
    from include import MyFunc1
except Exception as ImportError:   
    print(f"IMPORT ERROR ==> {ImportError}")    

#
# ---------- MAIN ----------
#

if __name__ == "__main__":

    print(f"IN __main__")

    try:

        MyFunc1.write_log_file("my_messages.txt","IN 'func 0-prototype-colors1.py()'")
        print("print empty line")

        print(f"{MyFunc1.FR_GREEN}---------- MAIN ----------{MyFunc1.NO_COLOR}")
        print("print empty line")

        print(f"---------- using CONTANTS for colors ----------")
        print("print empty line")

        colors= [MyFunc1.FR_RED,MyFunc1.FR_GREEN,MyFunc1.FR_YELL,MyFunc1.FR_BLUE,MyFunc1.FR_MAG]
        colors_str=['\\033[91m - Red','\\033[92m - Green','\\033[93m - Yellow','\\033[94m - Blue','\\033[95m - Magenta']
        
        i=0
        for color in colors:
            color_str = color
            msg=" ==> TESTING COLOR FUNCTION"
            msg = msg.rjust(30)
            #print("FR_RED value: " + colors_str[0])
            print("\tPrint with ascii " + colors_str[i] + f":\t{color}{msg}") 
            i+=1  
        msg="print with default color:\t\t ==> TESTING COLOR FUNCTION"
        print(f"\t{ms}")   
        print("print empty line")

        print(MyFunc1.frGREEN(f"---------- using function prRed(msg) ----------"))         
        msg="\tprint with function pfRed(msg) --> TESTING COLOR FUNCTION"
        print("print empty line")
        MyFunc1.prRed(msg)   
        print("print empty line")
        
        print(f"{MyFunc1.FR_GREEN}---------- That's all for today ----------{MyFunc1.NO_COLOR}")

    except Exception as Argument:
        error_msg = "ERROR IN <" + my_script_name + ">. SEE server_messages.txt !"
        print(f"my_messages.txt ==> {error_msg}")
        #MyFunc1.write_log_file("my_messages.txt",error_msg)
        #MyFunc1.write_traceback_info(Argument,traceback,my_script_name)
        
    
else:
    # something wrong
    print(MyFunc1.frRED("---- upsssssssss something is wrong ----"))
