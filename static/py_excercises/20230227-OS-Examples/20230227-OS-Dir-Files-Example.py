"""  
THIS SCRIPT IS FOR..................

"""
#
# IMPORT SECTION
#

try:   # Import My Own Functions from include dir 
    import os, sys, traceback 
    import platform  
    from os.path import dirname, realpath
    from os import system
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

# CONSTANTS

#
# ---------- COURSE EXCERCISE ----------
#

if __name__ == "__main__":

    try:

        # clear console screen
        if platform.system() == 'Windows':
            system('cls')
        elif platform.system() == 'Linux':
            system('clear')
        else:
            print(f"you OS is {platform.system()}. Find corresponding command to clear console screen")        

        # get name of script
        my_script = __file__.split('\\')
        my_script_name = my_script[len(my_script)-1]

        print()
        print(f"\n{FR_GREEN}---------- MAIN ----------{NO_COLOR}\n")
        pause()
        # my code    
        # my code    
        myPath = dirname(dirname(__file__))
        d = []
        for (dirpath, dirnames, filenames) in os.walk(myPath):
            d.extend(dirnames)
            #f.extend(filenames)
            break
        print(f"{FR_GREEN}Path: {myPath}")
        print()
        print(f"{FR_GREEN}FILES IN {myPath}: ")
        print()
        matrix_view(d,3)
        print()
        pause()

        os.chdir(myPath)
        os.chdir('../../')
        rootPath = os.getcwd()
        print(f"{FR_GREEN}parent path: {rootPath}")
        print()

        f = []
        d = []
        for (dirpath, dirnames, filenames) in os.walk(rootPath):
            f.extend(filenames)
            d.extend(dirnames)
            break

        print(f"{FR_GREEN}DIRS IN {rootPath}: ")
        print()
        matrix_view(d,3)
        print()
        pause()
        
        print(f"{FR_GREEN}FILES IN {rootPath}: ")
        print()
        matrix_view(f,3)
        pause()

        print(f"\n{FR_GREEN}---------- THAT'S ALL ----------{NO_COLOR}\n")
   
    except Exception as Argument:
        error_msg = "ERROR IN <" + my_script_name + ">. SEE server_messages.txt !"
        write_log_file("my_messages.txt",error_msg)
        write_traceback_info(Argument,traceback,my_script_name)  

else:
    # something wrong
    print(f"\n{FR_RED}---- upsssssssss something is wrong 😢😢  ---{NO_COLOR}\n")
    pause()

