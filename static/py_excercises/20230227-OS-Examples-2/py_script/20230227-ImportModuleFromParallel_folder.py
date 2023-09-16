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
import sys
import os
from os import system


#
# ---------- COURSE EXCERCISE ----------
#

if __name__ == "__main__":

    system('cls')

    print(f"\n=== MAIN ===\n")
    #prBlue('\n=== MAIN ===\n')  NOTE: this command is not defined yet
    
    print(f"\n=== Using functions located in a parallel folder ===\n")

    # printing folders in path without including de parallel folder with my functions --- default colors
    init_path = sys.path
    init_folders = []
    for fold in init_path:
        init_folders.append(fold)
    
    #print(f"type of var init_path:  {type(init_folders)} | values: {init_folders}")
    print(f"---printing list of folders in path, without including colors of 'my functions', located in parallel folder")
    for fold in init_folders:
        print(f"\t{fold}")
    print()


    cwd = os.getcwd()
    print(f"cwd: {cwd}")
    dir_path = os.path.join(cwd,'\static\py_excercises\\20230227-OS-Examples-2\MyFunctions')
    print(f"dir path: {dir_path}")
    # Add the MyFunction folder to path 
    # in my case ↓↓↓↓
    #sys.path.insert(1, dir_path)
    sys.path.insert(1, 'C:\\ML_Project\\NazarethCourse2023\\iggPyBlog\\static\\py_excercises\\20230227-OS-Examples-2\\MyFunctions')
    # in your case, create a folder MyFunctions and copy path with double \\ like ↑↑↑↑

    # create a new list with sys.path updated
    new_path = sys.path

    # IMPORT MODULE FROM PARALLEL FOLDER MyFunctions
    from MyColors import *
    from MyFunc import *

    pause()                           # this function is in MyFunc

    prBlue('\nOriginal "sys.path"')       # this function is in MyColors
    #print(f"type of var init_path:  {type(init_folders)} | values: {init_folders}")
    for fold in init_folders:
        prBlue(f"\t{fold}")

    prGreen('\nUpdated "sys.path"')
    prPurple('\tNOTE that one new folder is included now:  "MyFunctions"')
    print()

    pause()
        
    for fold in new_path:
        prGreen(f"\t{fold}")

    prYellow(f"\n=== That's All ===\n")

