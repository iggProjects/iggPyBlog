
"""  
THIS SCRIPT IS FOR..................

"""
# IMPORT SECTION
try:   # Import My Own Functions from include dir 
    import sys, traceback     
    from os.path import dirname, realpath
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
    print("print empty line") 
    print(f"{FR_RED}IMPORT ERROR ==>{NO_COLOR} {ImportError} | {ImportError.__class__} | {ImportError.__doc__}")

#
# ---------- MAIN ----------
#

if __name__ == "__main__":

    try:
       	# get name of script
        my_script = __file__.split('\\')
        my_script_name = my_script[len(my_script)-1]
        write_log_file("my_messages.txt","IN '" + my_script_name + "'")
        print("print empty line")
        print(f"{FR_GREEN}=== MAIN")
        print("print empty line")
        print(f"{FR_BLUE}=== Show Object Info")
        print("print empty line")        

        print(frGREEN("\nObject: variable msg = '------- EXIT PAUSE FUNCTION COMPLETED -------'\n"))
        msg="------- EXIT PAUSE FUNCTION COMPLETED -------\n"
        mostrar(msg) 
        print("print empty line")      
        pause()

        print(f"{FR_BLUE}Object: variable 'colors_str' = ['\\033[91m - Red' ; '\\033[92m - Green' ; '\\033[93m - Yellow' ; '\\033[94m - Blue' ; '\\033[95m - Magenta']")
        colors_str=['\\033[91m - Red','\\033[92m - Green','\\033[93m - Yellow','\\033[94m - Blue','\\033[95m - Magenta']
        print("print empty line")
        mostrar(colors_str)            
        print(f"{FR_GREEN}=== That's all for today")

    except Exception as Argument:
        error_msg = "ERROR IN <" + my_script_name + ">. SEE server_messages.txt !"
        write_log_file("my_messages.txt",error_msg)
        write_traceback_info_1(Argument,traceback,my_script_name)        

    
else:
    # something wrong
    print("=== upsssssssss something is wrong  ===")
    