# IMPORT FUNCTION FROM A PARALLEL FOLDER
#
# SOURCE OF INFO
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
#            - file Colors_ForTeacher.py
#            - file MyFunc_ForTeacher.py 
#      ----  sub folder Other_Functions
#            - file ImportModuleFromParallel_folder.py
#      list of scripts.py in root folder
#
#   Execute ImportModuleFromParallel_folder.py 
#  
import sys

init_path = sys.path
# print folders in path
for fold in init_path:
    print(f"\t{fold}")
print()    

# Add the MyFunction folder to path 
# in my case ↓↓↓↓
sys.path.insert(1, 'c:\\Users\\alu01\\Documents\\igg-Python\\Python-Nazareth-2023\\MyFunctions')
# in your case, create a folder MyFunctions and copy path with double \\ like ↑↑↑↑

new_path = sys.path
for fold in new_path:
    print(f"\t{fold}")
print()

# IMPORT MODULE FROM PARALLEL FOLDER MyFunctions
from Colors_ForTeacher import *
from MyFunc_ForTeacher import *

pause()                           # this function is in MyFunc_ForTeacher

prYellow('Original path\n')       # this function is in Colors_ForTeacher
for fold in init_path:
    prBlue(fold)

prPurple('path actualizado\n')    # this function is in Colors_ForTeacher
for fold in new_path:
    prGreen(fold)

pause()                           # this function is in MyFunc_ForTeacher

# NOTE: check the differences in the first 2 prints before IMPORT MyFunc and Colors
#       with the prints after import