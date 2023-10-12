"""  
THIS SCRIPT IS FOR..................

"""
#
# IMPORT SECTION
#

# My Own Functions from include dir 
try:   # Import My Own Functions from include dir 
    import sys, traceback     
    from os import system
    from os.path import dirname, realpath
    # import My Own Func
    from MyColors import *
    from MyFunc_copy_DL import *    
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

        # clear console screen
        clear_console_screen()
        # get name of script
        my_script = __file__.split('\\')
        my_script_name = my_script[len(my_script)-1]
        print()
        print(f"\n{FR_GREEN}---------- MAIN ----------{NO_COLOR}\n")
        print()
        pause()

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
        f = []
        d = []
        for (dirpath, dirnames, filenames) in os.walk(rootPath):
            f.extend(filenames)
            d.extend(dirnames)
            break

        print()
        print(f"{FR_GREEN}DIRS IN {rootPath}: ")
        print()
        matrix_view(d,3)
        print()
        print(f"{FR_GREEN}FILES IN {rootPath}: ")
        print()
        matrix_view(f,3)

        print(f"\n{FR_GREEN}---------- THAT'S ALL ----------{NO_COLOR}\n")
        pause()
   
    except Exception as Argument:
        write_traceback_info(Argument,traceback,my_script_name)        
        pause()

else:
    # something wrong
    print(f"\n{FR_RED}---- upsssssssss something is wrong 😢😢  ---{NO_COLOR}\n")
    pause()

