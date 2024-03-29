"""

Script for

"""

# IMPORT SECTION

try:   # Import My Own Functions from include dir 
    import os, sys, traceback, zipfile
    import platform 
    from os.path import basename, dirname, realpath
    from zipfile import ZipFile
    from os import system
    from pathlib import Path

    # get parent up 2 from __file__ path: 'static path'   
    up2_dir = dirname(dirname(dirname(realpath(__file__))))
    # insert path in sys.path
    sys.path.append(up2_dir)
    # get parent up 3 from __file__ path: 'static parent path'       
    up3_dir = dirname(dirname(dirname(dirname(realpath(__file__)))))
    # insert path in sys.path
    sys.path.append(up3_dir)
    # import My Own Func    
    from static.include.MyColors import *
    from static.include.MyFunc import *
    #from static.include.MyFunc_copy_DL import *
except Exception as ImportError:
    FR_RED   = "\033[91m" 
    NO_COLOR = "\033[00m"
    print("print empty line") 
    print(f"{FR_RED}IMPORT ERROR ==>{NO_COLOR} {ImportError} | {ImportError.__class__} | {ImportError.__doc__}")

# Function for tree structure zip file, needed in this excercise
def zip_compression_tree(root_path, zip_name):
    print(f"..... from zip_compression_tree: {root_path} | zip_name: {zip_name}")
    with zipfile.ZipFile(zip_name, 'w') as z:
        for root, dirs, files in os.walk(root_path):
            for file in files:
                print(f"...file added: {file}")  
                if file != zip_name:             
                    z.write(os.path.join(root, file))
            for directory in dirs:
                print(f"...dir added: {directory}")               
                z.write(os.path.join(root, directory))

#
# ---------- MAIN ----------
#

if __name__ == "__main__":

    try:

        # clear console screen
        clear_console_screen()        
        # get name of script
        my_script = __file__.split('\\')
        my_script_name = my_script[len(my_script)-1]
        write_log_file("my_messages.txt","IN '" + my_script_name + "'")

        print()
        print("\n---------- MAIN ----------\n")
        print()
        pause()

        # list_paths: append Directory of file
        dirPath = dirname(__file__)
        os.chdir(dirPath)
        dirPath = os.getcwd()
        print(f"dirPath: {dirPath}")
        print()
        list_paths = []
        list_paths.append(dirPath)

        # os.path.normpath(path) 
        dirArray = os.path.split(dirPath)
        fileNameZip = dirArray[1] + '.zip'
        file_zip_path = os.path.join(dirname(__file__),fileNameZip)

        """
        print(f"list_paths:")
        for path in list_paths:
            print(f"\t{path}")
        print()    
        """
        print()
        print(f"{FR_BLUE}*** Creating Zip File '{fileNameZip}' ***{NO_COLOR}")
        print()
        pause()

        # delete if exists  
        if os.path.exists(fileNameZip):
            os.remove(fileNameZip)
            print()
            print(f"{FR_RED}file '{fileNameZip}' deleted{NO_COLOR}")
            print()

        zip_compression_tree(list_paths[0], fileNameZip)

        if os.path.exists(fileNameZip):

            print()
            print(f"{FR_BLUE}File '{fileNameZip}' succesfully created{NO_COLOR}\n\tstored in: {dirname(__file__)}")
            print()
            pause()

            # Case localhost, folder to save in Downloads folder: "iggPyWeb"
            #print(f".... os.path.expanduser('~'): {os.path.expanduser('~')}")    
            downloads_path = os.path.join(Path.home(),"Downloads","iggPyWeb")

            if ('home' not in downloads_path):

                print(f"{FR_GREEN}download path in client --->{NO_COLOR} {downloads_path}")
                print()

                # Copy file to folder in PC
                import shutil

                # source file path
                src_path = os.path.join(dirPath, fileNameZip)
                print(f"{FR_GREEN}src_path{NO_COLOR}")
                print(f"{src_path}")
                print()
               
                if not os.path.exists(downloads_path):
                    os.mkdir(downloads_path)
                    print(f"Dir {downloads_path} created !!!")
                    print()

                shutil.copy(src_path, downloads_path)        
                print(f"\tFile '{fileNameZip}' copied in folder '{downloads_path}'")  
                print() 

            else:
                print(f"{FR_MAG}Could not create file {fileNameZip}{NO_COLOR}")
        
        else:
            print(f"{FR_BLUE} Zip file could '{fileNameZip}' not be created !{NO_COLOR}")
        
        print(f"\n{FR_GREEN}---------- That's all for today 👌 ----------{NO_COLOR}\n")

        pause()

    except Exception as Argument:
        error_msg = "ERROR IN <" + my_script_name + ">. SEE server_messages.txt !"
        write_log_file("my_messages.txt",error_msg)
        write_traceback_info(Argument,traceback,my_script_name)    

else:
    # something wrong
    print(frRED("\n---- ******** ----\n"))
    # pause()