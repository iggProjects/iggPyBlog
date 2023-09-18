
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
sys.path.insert(1, ROOT_DIR)

#print(f"----------------------- os.curdir --> {type(os.curdir)} | value: {os.curdir}")
#print(f"----------------------- os.path.abspath(os.curdir) --> {ROOT_DIR}")
#print(f"----------------------- os.getcwd() --> {os.getcwd()}")


# import "My Own Funct" from root path
from MyFunc import *

#
# ---------- MAIN ----------
#

if __name__ == "__main__":

    try:

        write_log_file("my_messages.txt","IN 'func 0-prototype-colors1.py()'")
        print("print empty line")

        print(f"{FR_GREEN}---------- MAIN ----------{NO_COLOR}")
        print("print empty line")

        print(f"---------- using CONTANTS for colors ----------")
        print("print empty line")

        colors= [FR_RED,FR_GREEN,FR_YELL,FR_BLUE,FR_MAG]
        colors_str=['\\033[91m - Red','\\033[92m - Green','\\033[93m - Yellow','\\033[94m - Blue','\\033[95m - Magenta']
        
        i=1/0
        for color in colors:
            color_str = color
            msg=" ==> TESTING COLOR FUNCTION"
            msg = msg.rjust(30)
            #print("FR_RED value: " + colors_str[0])
            print("\tPrint with ascii " + colors_str[i] + f":\t{color}{msg}") 
            i+=1  
        msg="print with default color:\t\t ==> TESTING COLOR FUNCTION"
        print(f"\t{msg}")   
        print("print empty line")

        print(frGREEN(f"---------- using function prRed(msg) ----------"))         
        msg="\tprint with function pfRed(msg) --> TESTING COLOR FUNCTION"
        print("print empty line")
        prRed(msg)   
        print("print empty line")
        
        print(f"{FR_GREEN}---------- That's all for today ----------{NO_COLOR}")

    except Exception as Argument:  
        write_log_file("my_messages.txt","ERROR IN 'func 0-prototype-colors1.py()'. SEE server_messages.txt")
        
        traceback_formatted = traceback.format_exc().replace('"','').replace(',','|')
        traceback_lines = traceback_formatted.split('\n')
        traceback_lines_2 = traceback_lines[1].split('|')
        print("print empty line")
        print(frRED("====================== ERROR FOUND IN 0-prototype-colors1.py() ======================"))
        print("print empty line")
        print(f"{FR_BLUE}===> {Argument} - {traceback_lines_2[1]} | {Argument.__class__} | {Argument.__doc__}{NO_COLOR}")

        #print("traceback")
        #print(f"{traceback.format_exc()}")
        #print("print empty line")

        #print(f"traceback_lines length: {len(traceback_lines)}")
        #print(f"{traceback_lines}")
        #print("print empty line")

        #print("traceback_lines[1]")
        #print(f"{traceback_lines[1]}")    
        #print("print empty line")

        #print("traceback_lines_2")
        #print(f"{traceback_lines_2}")
        #print("print empty line")

        #traceback_lines_2_2 = traceback_lines_2[2].split('|')
        #print("traceback_lines_2_2")        
        
        print("print empty line")        
        print(frGREEN(f"\t\tSEE 'server_messages.txt' file OR Contact Web Admin !"))
        logging.exception(f"{Argument} | exception from '0-prototype-colors.py()': ")

        #print(f"\ttraceback.format_exc() : {type(traceback.format_exc())}")
        #print(f"{traceback.format_exc()}")
    
else:
    # something wrong
    print(frRED("---- upsssssssss something is wrong ----"))
