
"""  
THIS SCRIPT EXECUTE HELP FUNCTION TO ANALYZE A CODE OBJECT

"""
# IMPORT SECTION
import os, sys
from os import  system

# include root path in sys.path
ROOT_DIR = os.path.abspath(os.curdir)
# check in what server is app
if "iggWebNz" in ROOT_DIR:              # pythonanywhere  
    ROOT_DIR = ROOT_DIR + "/mysite"
else:                                   # working in localhost server
    pass 
sys.path.insert(1, ROOT_DIR)

# import "My Own Funct" from root path
from MyFunc import *


# CONSTANTS

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
    