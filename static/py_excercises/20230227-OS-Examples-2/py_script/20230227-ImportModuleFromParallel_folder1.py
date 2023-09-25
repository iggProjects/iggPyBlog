# IMPORT FUNCTION FROM A PARALLEL FOLDER
#
# SOURCE OF INFO
# https://docs.python.org/es/3/library/sys_path_init.html

# https://www.geeksforgeeks.org/python-import-module-from-different-directory/
# https://es.stackoverflow.com/questions/401804/python-importerror-attempted-relative-import-with-no-known-parent-package
# https://problemsolvingwithpython.com/07-Functions-and-Modules/07.05-Calling-Functions-from-Other-Files/#:~:text=To%20use%20the%20functions%20written,of%20the%20filename%20during%20import.
# https://stackoverflow.com/questions/4383571/importing-files-from-different-folder
# https://stackoverflow.com/questions/24622041/python-importing-a-module-from-a-parallel-directory
# https://www.reddit.com/r/learnpython/comments/50795d/how_to_load_module_from_parallel_directory/
# https://dkhambu.medium.com/importing-files-in-python-repository-28ab49fade37
#

## Create file __init__.py empty in that folder - to read dir

#   FOLDER SCHEMA
#   root folder
#      ----  sub folder MyFunctions
#            - file MyColors.py
#            - file MyFunc.py 
#      ----  sub folder Other_Functions
#            - file ImportModuleFromParallel_folder.py
#      list of scripts.py in root folder
#
#   Execute ImportModuleFromParallel_folder.py 
#  

try:   # Import My Own Functions from include dir 
    import sys, traceback     
    from os.path import dirname, realpath
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
        #write_log_file("my_messages.txt","IN '" + my_script_name + "'")
        print("print empty line")
        print(f"=== MAIN ===")
        #print(f"{FR_BLUE}=== MAIN ===")  -- NOTE: this command is not defined yet
        print("print empty line")

        print(f"=== Using functions located in a parallel folder ===")
        print("print empty line")

        # printing folders in path without including de parallel folder with my functions --- default colors
        init_path = sys.path
        init_folders = []
        for fold in init_path:
            init_folders.append(fold)
        
        #print(f"type of var init_path:  {type(init_folders)} | values: {init_folders}")
        print("---printing list of folders in path, without including colors of 'my functions', located in parallel folder")
        for fold in init_folders:
            print(f"\t{fold}")
        print("print empty line")
        """
        up2_dir = dirname(dirname(__file__))
        print(f"up2_dir: {up2_dir}")
        sys.path.append(up2_dir)
        """        
        # Add the MyFunction folder to path 
        # in my case ↓↓↓↓
        # sys.path.append(up3_dir)
        sys.path.insert(1, 'C:\\ML_Project\\NazarethCourse2023\\iggPyBlog\\static\\py_excercises\\20230227-OS-Examples-2\\MyFunctions')
        # in your case, create a folder MyFunctions and copy path with double \\ like ↑↑↑↑

        # create a new list with sys.path updated
        new_path = sys.path

        # IMPORT MODULE FROM PARALLEL FOLDER MyFunctions
        from MyColors import *
        from MyFunc import *

        print(f'{FR_BLUE}Original sys.path in BLUE')       # this function is in MyColors
        #print(f"type of var init_path:  {type(init_folders)} | values: {init_folders}")
        for fold in init_folders:
            print(f"\t{FR_BLUE}{fold}")
        print("print empty line")

        print(f'{FR_GREEN}Updated sys.path in GREEN')
        print(f'\t{FR_RED}NOTE that one new folder is included now:  MyFunctions')
        for fold in new_path:
            print(f"\t{FR_GREEN}{fold}")
        print("print empty line")

        print(f"{FR_BLUE}=== That's All ===\n")
        print("print empty line")

    except Exception as Argument:
        error_msg = "ERROR IN <" + my_script_name + ">. SEE server_messages.txt !"
        #write_log_file("my_messages.txt",error_msg)
        #write_traceback_info(Argument,traceback,my_script_name)        
