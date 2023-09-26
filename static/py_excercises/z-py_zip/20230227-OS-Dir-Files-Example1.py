"""  
THIS SCRIPT IS FOR..................

"""
#
# IMPORT SECTION
#

try:   # Import My Own Functions from include dir 
    import os, sys, traceback, math, platform
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
# ---------- COURSE EXCERCISE ----------
#

if __name__ == "__main__":
        
    try:
        # get name of script
        my_script = __file__.split('\\')
        my_script_name = my_script[len(my_script)-1]
        write_log_file("my_messages.txt","IN '" + my_script_name + "'")

        print(f"\n{FR_GREEN}---------- main ----------{NO_COLOR}\n")    

        # my code    
        myPath = os.getcwd()
        f = []
        for (dirpath, dirnames, filenames) in os.walk(myPath):
            f.extend(filenames)
            break
        print(f"{FR_GREEN}path -->{NO_COLOR} {myPath}\n")
        matrix_view(f,3)
        print(f"\n------------------------------------------------\n")

        parent = os.chdir('../')
        parentPath = os.getcwd()
        print(f"{FR_GREEN}parent path -->{NO_COLOR} {parentPath}\n")
        f = []
        for (dirpath, dirnames, filenames) in os.walk(parentPath):
            f.extend(filenames)
            break
        matrix_view(f,3)
        print(f"\n------------------------------------------------\n")

        # Library methods info         
        library_methods(os)        
        library_methods(platform)

    except Exception as Argument:
        error_msg = "ERROR IN <" + my_script_name + ">. SEE server_messages.txt !"
        write_log_file("my_messages.txt",error_msg)
        write_traceback_info(Argument,traceback,my_script_name)        
    

else:
    # something wrong
    print(f"\n{FR_RED}---- upsssssssss something is wrong 😢😢  ---{NO_COLOR}\n")
    