
"""  
THIS SCRIPT EXECUTE HELP FUNCTION TO ANALYZE A CODE OBJECT

"""
# IMPORT SECTION

# My Own Functions from include dir 
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

# get name of script
my_script = __file__.split('\\')
my_script_name = my_script[len(my_script)-1]

#
# ---------- MAIN ----------
#

if __name__ == "__main__":

    print("print empty line")
    print(frGREEN("=== MAIN ==="))
    prBlue("=== help for object 'list'")
    print("print empty line")

    my_obj = [1,2,3,4,5]
    print("my_obj = [1;2;3;4;5] ==> calling help_obj_method(my_obj) in MyFunc Module")
    print("print empty line")
    print("print empty line")
    help_obj_method(my_obj)
    print("print empty line") 
    print("print empty line") 
    print(f"{FR_BLUE}=== That's all for today ===")
    print("print empty line")

else:
    # something wrong
    print(frRED("=== upsssssssss something is wrong ==="))
    