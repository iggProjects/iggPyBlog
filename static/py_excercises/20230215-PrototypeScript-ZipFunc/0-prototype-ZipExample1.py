
"""  
    THIS SCRIPT IS ZIP FILES OF A DIRECTORY AND UPLOAD TO DOWNLOADS FOLDER OF PC
        - https://note.nkmk.me/en/python-os-basename-dirname-split-splitext/#:~:text=dirname()-,Use%20os.,name)%20from%20a%20path%20string.
        - https://stackoverflow.com/questions/2042342/how-to-copy-a-file-from-a-network-share-to-local-disk-with-variables 
        - https://www.tutorialspoint.com/How-to-create-a-zip-file-using-Python

        DONWLOAD FOLDER
        - https://stackoverflow.com/questions/35851281/python-finding-the-users-downloads-folder

            from pathlib import Path
            downloads_path = str(Path.home() / "Downloads")   

"""

# IMPORT SECTION
try:   # Import My Own Functions from include dir 
    import os, sys, traceback     
    from os.path import basename, dirname, isdir, isfile, realpath
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
        
    try:

        # get name of script
        my_script = __file__.split('\\')
        my_script_name = my_script[len(my_script)-1]
        write_log_file("my_messages.txt","IN '" + my_script_name + "'")

        print("print empty line")
        print(f"{FR_GREEN}---------- MAIN ----------{NO_COLOR}")    
        print("print empty line")

        # list_paths: append Directory of file
        dirPath = dirname(__file__)
        os.chdir(dirPath)
        dirPath = os.getcwd()
        list_paths = []
        list_paths.append(dirPath)

        # os.path.normpath(path) 
        dirArray = os.path.split(dirPath)
        fileNameZip = dirArray[1] + '.zip'
        file_zip_path = os.path.join(dirname(__file__),fileNameZip)
        
        # list_paths: append paths to MyColor.py & MyFunc.py
        static_path = dirname(dirname(dirname(__file__))) 
        #print(f"static_path: {static_path}")
        print("print empty line")
        MyColors_path = os.path.join(static_path,'include','MyColors.py')
        #MyColors_path = static_path + '\include\MyColors.py'
        list_paths.append(MyColors_path)  
        MyFunc_path = os.path.join(static_path,'include','MyFunc_copy_DL.py')
        #MyFunc_path = static_path + '\include\MyFunc_copy_DL.py'
        list_paths.append(MyFunc_path)
    
        
        for path in list_paths:
            print(f"\t{path}")
        print("print empty line")    
        
        # delete if exists  
        if os.path.exists(fileNameZip):
            os.remove(fileNameZip)
            print(f"===> file '{fileNameZip}' deleted")
            print("print empty line")    

        print(f"{FR_BLUE}*** Creating Zip File '{fileNameZip}' ***{NO_COLOR}")
        print("print empty line")
        zipFilesInList(list_paths, fileNameZip, lambda name : 'DL' in name)

        if os.path.exists(fileNameZip):

            print("print empty line")
            print(f"{FR_BLUE}{fileNameZip} succesfully created !{NO_COLOR}")
            print("print empty line")

            # Copy file to folder in PC
            import shutil

            # source file path
            # src_path = dirPath + '\\' + fileNameZip

            # source file path
            src_path = os.path.join(dirPath, fileNameZip)

            print(f"{FR_GREEN}src_path{NO_COLOR}")
            print(f"{src_path}")
            print("print empty line")

            # folder to save file: "iggPyWeb" in Downloads folder
            downloads_path = str(Path.home() / "Downloads" / "iggPyWeb")

            if ('home' not in downloads_path):

                print(f"download path ---> {downloads_path}")
                print("print empty line")
            
                if not os.path.exists(downloads_path):
                    os.mkdir(downloads_path)
                    print(f"Dir {downloads_path} created !!!")
                    print("print empty line")

                # permission problems
                # https://stackoverflow.com/questions/7518067/python-ioerror-errno-13-permission-denied-when-im-copying-file    

                shutil.copy(src_path, downloads_path)        
                print(f"{FR_GREEN}Copy Process:{NO_COLOR}")
                print("print empty line")  
                print(f"\tFile '{fileNameZip}' copied in folder '{downloads_path}'")  
                print("print empty line")
                print(f"{FR_GREEN}---------- That's all for today  ----------{NO_COLOR}")
        
            else:
                print(f"{FR_GREEN}Find {fileNameZip} in base dir of script !{NO_COLOR}")


    except Exception as Argument:
        error_msg = "ERROR IN <" + my_script_name + ">. SEE server_messages.txt !"
        write_log_file("my_messages.txt",error_msg)
        write_traceback_info_1(Argument,traceback,my_script_name)  

else:
    # something wrong
    print(frRED("\n---- ******** ----\n"))
    # 