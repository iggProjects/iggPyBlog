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
import sys, os, datetime, logging, traceback 
from os import system
from os.path import dirname

# error handlng 

# create dir logFiles for logging process
static_path = dirname(dirname(__file__))
logDirPath = os.path.join(static_path, 'logFiles')
if os.path.exists(logDirPath):
    pass
else:
    os.makedirs(logDirPath)
log_file_path = logDirPath + "/server_messages.txt"

logging.basicConfig(filename=log_file_path, 
                encoding='utf-8', level=logging.DEBUG, format="%(asctime)-15s %(levelname)-8s %(funcName)s %(message)s")
logging.captureWarnings(True)

"""
# function to write in logFile
def write_log_file(logFile,msg):

    try:
        # path to log file
        logFile_path = static_path + "/logFiles/" + logFile
        # creating/opening a file
        f = open(logFile_path, "a") 
        # write in file        
        f.write('%s | %s\n' % (datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3],msg))      
        # close file
        f.close()
    except Exception as Argument:
        print(f"Error {Argument}")
        logging.exception(f"{Argument} | exception from 'write_log_file()' ")

def write_traceback_info(Argum,TraceList,script): 
               
        traceback_formatted = TraceList.format_exc().replace('"','').replace(',',' | ')
        traceback_lines = traceback_formatted.split('\n')
        print()        
        print(f"====================== ERROR FOUND ======================")
        print()
        for line in traceback_lines:
            #if ('File' or 'line' or 'Module') in line:
            if 'line' in line:
                for field in line.split('|'):
                   if 'line' in field:
                      line_numb = field

        print(f"FILE: <{script}>")
        print()
        print(f"\tcode in{line_numb}:{traceback_lines[len(traceback_lines)-3]}")        
        print(f"\t{Argum} | {Argum.__class__} | {Argum.__doc__}")
        print()

        print(f"\t\tSEE 'server_messages.txt' file OR Contact Web Admin !")
        logging.exception(f"{Argum} | exception from '0-prototype-colors.py()': ")
"""

#
# ---------- COURSE EXCERCISE ----------
#

if __name__ == "__main__":

    system('cls')

    try:
        # get name of script
        my_script = __file__.split('\\')
        my_script_name = my_script[len(my_script)-1]
        #write_log_file("my_messages.txt","IN '" + my_script_name + "'")
        print()
        print(f"=== MAIN ===")
        #print(f"{FR_MAG}=== MAIN ===")  # NOTE: try to print and note that you must have an error
        print()

        print(f"=== Using functions located in a parallel folder ===")
        print()

        # printing folders in path without including de parallel folder with my functions --- default colors
        init_path = sys.path
        init_folders = []
        for fold in init_path:
            init_folders.append(fold)
        
        print("---printing list of folders in path, without including colors of 'my functions', located in parallel folder")
        for fold in init_folders:
            print(f"\t{fold}")
        print()
        
        # Add the '20230227-OS-Examples-2' folder to path                 
        up2_dir = dirname(dirname(__file__))  # look for '20230227-OS-Examples-2' path        
        sys.path.append(up2_dir)
        # Add 'MyFunctions' path
        myFunctions_path = up2_dir + '/MyFunctions'
        sys.path.append(myFunctions_path) 

        # create a new list with sys.path updated, to campare list of paths
        new_path = sys.path

        # IMPORT MODULE F
        # ROM PARALLEL FOLDER MyFunctions
        from MyFunctions.MyCol import *
        from MyFunctions.MyFun import *

        print(f'{FR_MAG}Original sys.path in MAG')       # this function is in MyColors
        for fold in init_folders:
            print(f"\t{FR_MAG}{fold}")
        print()
        pause()

        print(f'{FR_GREEN}Updated sys.path in GREEN')
        print(f'\t{FR_RED}NOTE that two new folders are included now: <20230227-OS-Examples-2> & <MyFunctions>')
        for fold in new_path:
            print(f"\t{FR_GREEN}{fold}")
        print()
        pause()

        print(f"{FR_MAG}=== That's All ===\n")
        print()

    except Exception as Argument:
        error_msg = "ERROR IN <" + my_script_name + ">. SEE server_messages.txt !"
        write_log_file("my_messages.txt",error_msg)
        write_traceback_info(Argument,traceback,my_script_name)    
        pause()    


