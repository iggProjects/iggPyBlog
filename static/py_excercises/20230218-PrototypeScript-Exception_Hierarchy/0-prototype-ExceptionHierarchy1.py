
"""  
THIS SCRIPT IS FOR PRINTING WITH COLORS

"""
# IMPORT SECTION
try:   # Import My Own Functions from include dir 
    import sys, traceback
    import inspect
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

# CONSTANTS & FUNCTIONS

# Print Exception Hierrachy
def classtree(cls, indent=0):
    print('.' * indent, cls.__name__)
    for subcls in cls.__subclasses__():
        classtree(subcls, indent + 3)


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
        print(f"{FR_GREEN}---------- main ----------{NO_COLOR}")
        print("print empty line")

        print(frGREEN("\n---------- Exception Hierarchy ----------\n"))    
        print("print empty line")

        # 
        #inspect.getclasstree(inspect.getmro(Exception))
        #classtree(Exception)

        #class_Exception = Exception
        class_Exception = ValueError  # sub class of Exception hierarchy
        print(f"{FR_GREEN}The hierarchy for built-in '{class_Exception}' is{NO_COLOR}:")
        print("print empty line")

        inspect.getclasstree(inspect.getmro(class_Exception))
        print(f"{FR_BLUE}---------- Tree for {class_Exception} ----------{NO_COLOR}")
        print("print empty line")

        classtree(class_Exception)


        print("print empty line")
        print(f"{FR_GREEN}---------- That's all for today ----------{NO_COLOR}")
        print("print empty line")

    except Exception as Argument:
        error_msg = "ERROR IN <" + my_script_name + ">. SEE server_messages.txt !"
        write_log_file("my_messages.txt",error_msg)
        write_traceback_info_1(Argument,traceback,my_script_name)        

else:
    # something wrong
    print(frRED("---- ******** ----"))
