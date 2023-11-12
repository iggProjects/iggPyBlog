
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

 
    print(frGREEN("---------- main ----------"))
    print(frGREEN("--------------- pause() called --------------"))

    msg="------- EXIT PAUSE FUNCTION COMPLETED -------"
    prGreen(msg)   

    print(f"{FR_GREEN}---------- That's all for today ----------{NO_COLOR}")


else:
    # something wrong
    print(frRED("---- ******** ----"))
    pause()