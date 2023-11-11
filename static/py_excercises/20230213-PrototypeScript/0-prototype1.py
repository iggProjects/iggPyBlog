
"""  
THIS IS MY STANDAR SCRIPT TO CREATE NEWS SCRIPTS 

"""
try:   # Import My Own Functions from include dir 
    import sys, traceback, platform     
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
    print() 
    print(f"{FR_RED}IMPORT ERROR ==>{NO_COLOR} {ImportError} | {ImportError.__class__} | {ImportError.__doc__}")

#
# ---------- MAIN ----------
#

if __name__ == "__main__":

    print(f"{FR_GREEN}---------- prototype py model ----------{NO_COLOR}")

    print("print empty line")
    print("print empty line")

    print(f"{FR_BLUE}\t\t\t\t\t\t---------- USE DOWNLOAD OPTION ----------{NO_COLOR}")

    #
    # YOUR CODE
    #     

else:
    # something wrong
    print(f"{FR_GREEN}---- ****** ----{NO_COLOR}")
