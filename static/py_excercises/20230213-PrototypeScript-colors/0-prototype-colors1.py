
"""  
    THIS SCRIPT IS FOR PRINTING WITH COLORS

"""
# IMPORT SECTION
# My Own Functions from include dir
 
try: 

    import os, sys
    from os.path import dirname, realpath 
    # get parent up 3 from __file__ path   
    up3_dir = dirname(dirname(dirname(dirname(realpath(__file__)))))
    # insert "root path" path in sys.path
    sys.path.append(up3_dir)
    from static.MyFunc1 import *
    from static.MyColors1 import *

except Exception as ImportError:   
    print(f"IMPORT ERROR ==> {ImportError}")    

# get name of script
my_script = __file__.split('\\')
my_script_name = my_script[len(my_script)-1]

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

        print(frGREEN(f"---------- using function prRed(msg) ----------"))         
        msg="\tprint with function pfRed(msg) --> TESTING COLOR FUNCTION"
        print("print empty line")
        prRed(msg)   
        print("print empty line")
        
        print(f"{FR_GREEN}---------- That's all for today ----------{NO_COLOR}")

    except Exception as Argument:
        error_msg = "ERROR IN <" + my_script_name + ">. SEE server_messages.txt !"
        write_log_file("my_messages.txt",error_msg)
        write_traceback_info(Argument,traceback,my_script_name)        
    
else:
    # something wrong
    print(frRED("---- upsssssssss something is wrong ----"))
