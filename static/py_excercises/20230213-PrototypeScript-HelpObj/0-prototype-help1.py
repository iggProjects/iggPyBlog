
"""  
THIS SCRIPT EXECUTE HELP FUNCTION TO ANALYZE A CODE OBJECT

"""
# IMPORT SECTION

try: 
    import sys
    from os.path import dirname, realpath
    filepath = realpath(__file__)
    file_dir = dirname(filepath)
    parent_dir = dirname(file_dir)
    grand_parent_dir = dirname(parent_dir)
    grand_grand_dir = dirname(grand_parent_dir)  
    sys.path.append(grand_grand_dir)  
    from static.config_path_MyFunc import *


except Exception as ImportError:   
    print(f"IMPORT ERROR ==> {ImportError}")    

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
    