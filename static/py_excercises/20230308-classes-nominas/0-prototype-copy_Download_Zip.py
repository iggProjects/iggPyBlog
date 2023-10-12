"""  
    THIS SCRIPT IS ZIP FILES OF A DIRECTORY AND UPLOAD TO DOWNLOADS FOLDER OF PC
        - https://note.nkmk.me/en/python-os-basename-dirname-split-splitext/#:~:text=dirname()-,Use%20os.,name)%20from%20a%20path%20string.
        - https://stackoverflow.com/questions/2042342/how-to-copy-a-file-from-a-network-share-to-local-disk-with-variables 
        - https://www.tutorialspoint.com/How-to-create-a-zip-file-using-Python

        DONWLOAD FOLDER
        - https://stackoverflow.com/questions/35851281/python-finding-the-users-downloads-folder

            from pathlib import Path
            downloads_path = str(Path.home() / "Downloads")  

    permission problems
        https://stackoverflow.com/questions/7518067/python-ioerror-errno-13-permission-denied-when-im-copying-file    
        
"""

# IMPORT SECTION
try:   # Import My Own Functions from include dir 
    import os, sys, traceback
    import platform
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
    from static.include.MyColors import *
    from static.include.MyFunc import *
    #from static.include.MyFunc_copy_DL import *
except Exception as ImportError:
    FR_RED   = "\033[91m" 
    NO_COLOR = "\033[00m"
    print("print empty line") 
    print(f"{FR_RED}IMPORT ERROR ==>{NO_COLOR} {ImportError} | {ImportError.__class__} | {ImportError.__doc__}")


#
# ---------- MAIN ----------
#

if __name__ == "__main__":

    # clear console screen
    clear_console_screen()
    print()
    print("\n---------- MAIN ----------\n")
    print()
    pause()

    # list_paths: append Directory of file
    dirPath = dirname(__file__)
    os.chdir(dirPath)
    dirPath = os.getcwd()
    list_paths = []
    list_paths.append(dirPath)

    # name of zip file
    dirArray = dirPath.split('\\')    
    dirName = dirArray[len(dirArray)-1]
    fileNameZip = dirName+'.zip'

    # list_paths: append paths to MyColor.py & MyFunc.py
    static_path = dirname(dirname(dirname(__file__))) 
    #print(f"static_path: {static_path}")
    print()
    MyColors_path = static_path + '\include\MyColors.py'
    list_paths.append(MyColors_path)  
    MyFunc_path = static_path + '\include\MyFunc_copy_DL.py'
    list_paths.append(MyFunc_path)      

    """
    for path in list_paths:
        print(f"\t{path}")
    print()    
    """
    # delete if exists  
    if os.path.exists(fileNameZip):
        os.remove(fileNameZip)
        print(f"===> file '{fileNameZip}' deleted")
        print()    

    print(f"{FR_BLUE}*** Creating Zip File '{fileNameZip}' ***{NO_COLOR}")
    print()
    zipFilesInList(list_paths, fileNameZip, lambda name: 'DL' in name)

    if os.path.exists(fileNameZip):

        print()
        print(f"{FR_BLUE}{fileNameZip} succesfully created !{NO_COLOR}")
        print()

        # Copy file to folder in PC
        import shutil

        # source file path
        src_path = dirPath + '\\' + fileNameZip
        print(f"{FR_GREEN}src_path{NO_COLOR}")
        print(f"{src_path}")
        print()

        # folder to save file: "iggPyWeb" in Downloads folder
        downloads_path = str(Path.home() / "Downloads" / "iggPyWeb")
        print(f"download path in client ---> {downloads_path}")
        print()
        
        if not os.path.exists(downloads_path):
            os.mkdir(downloads_path)
            print(f"Dir {downloads_path} created !!!")
            print()

        #shutil.copy(src_path, dst_path)        
        shutil.copy(src_path, downloads_path)        
        print(f"{FR_GREEN}Copy Process:{NO_COLOR}")
        print()  
        print(f"\tFile '{fileNameZip}' copied in folder '{downloads_path}'")  
        print() 
    
    else:
        print(f"UPSSSSSS............")
    
    print(f"\n{FR_GREEN}---------- That's all for today 👌 ----------{NO_COLOR}\n")

    pause()
else:
    # something wrong
    print(frRED("\n---- upsssssssss something is wrong 😢😢  ----\n"))
    # pause()