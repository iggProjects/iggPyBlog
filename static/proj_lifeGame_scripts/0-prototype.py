"""  
    
    THIS SCRIPT IS FOR .............

"""
# IMPORT SECTION

try:   # Import My Own Functions from include dir 
    import sys, traceback
    import numpy as np   
    from os.path import dirname, realpath
    from os import scandir
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

# ---------- CONSTANTS & FUNCTIONS ----------


#
# ---------- MAIN ----------
#

if __name__ == "__main__":

    try:

        clear_console_screen()

        my_script = __file__.split('\\')
        my_script_name = my_script[len(my_script)-1]
        print()
        write_log_file("my_messages.txt","IN '" + my_script_name + "'")
        print()

        print(f"{FR_GREEN}---------- MAIN ----------{NO_COLOR}")
        print()

        # YOUR CODE

        print(f"{FR_GREEN}---------- That's all for today ----------{NO_COLOR}")
        print()
        pause()

    except Exception as Argument:
        error_msg = "ERROR IN <" + my_script_name + ">. SEE server_messages.txt !"
        write_log_file("my_messages.txt",error_msg)
        write_traceback_info_1(Argument,traceback,my_script_name)
        pause()     
    
else:
    # something wrong
    print(frRED("---- ********* ----"))
