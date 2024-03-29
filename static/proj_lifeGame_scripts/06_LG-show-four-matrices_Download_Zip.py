
# IMPORT SECTION
try:   # Import My Own Functions from include dir 
    import os, sys, traceback
    import platform
    from os.path import basename, dirname, isdir, isfile, realpath
    from zipfile import ZipFile
    from os import system
    from pathlib import Path

    # get parent up 2 from __file__ path: 'static path'   
    up2_dir = dirname(dirname(realpath(__file__)))
    #up2_dir = dirname(dirname(dirname(realpath(__file__))))
    # insert path in sys.path
    sys.path.append(up2_dir)
    # get parent up 3 from __file__ path: 'static parent path'       
    up3_dir = dirname(dirname(dirname(realpath(__file__))))
    print(f"up2_dir {up2_dir}")
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

    # clear screen
    clear_console_screen()
    print()
    print("---------- MAIN ----------")
    print()

    # list_paths: append Directory of file
    dirName = dirname(__file__)
    os.chdir(dirname(__file__))
    dirPath = os.getcwd()
    print(f"dirPath: {dirPath}")

    list_paths = []
    list_paths.append(dirPath)

    # os.path.normpath(path) 
    #dirArray = os.path.split(dirPath)
    fileNameZip = basename(__file__) + '.zip'
    fileNameZip = fileNameZip.replace('_Download_Zip.py','')
    print(f"fileNameZip: {fileNameZip}")
    file_zip_path = os.path.join(dirname(__file__),fileNameZip)
    
    # list_paths: append paths to MyColor.py & MyFunc.py
    static_path = dirname(dirname(__file__))   
    #static_path = dirname(dirname(dirname(__file__))) 
    print(f"static_path: {static_path}")
    MyColors_path = static_path + '/include/MyColors.py'
    list_paths.append(MyColors_path)  
    MyFunc_path = static_path + '/include/MyFunc_copy_DL.py'
    list_paths.append(MyFunc_path)      

    print()
    for path in list_paths:
        print(f"\t{path}")
    print()    
    

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

    
    zipFilesInList(list_paths, file_zip_path, lambda name: 'four-matrices_DL' in name)
    
    if os.path.exists(fileNameZip):

        print()
        print(f"{FR_BLUE}File '{fileNameZip}' succesfully created{NO_COLOR}\n\tstored in: {dirname(__file__)}")
        print()
    
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

            if not os.path.exists(downloads_path):
                os.mkdir(downloads_path)
                print(f"Dir {downloads_path} created !!!")
                print()

            shutil.copy(src_path, downloads_path)        
            print(f"{FR_GREEN}File '{fileNameZip}'{NO_COLOR} also copied in folder '{downloads_path}'")  
            print() 
    
        else:
            print(f"{FR_MAG}Could not create file {fileNameZip}{NO_COLOR}")
    
    print(f"\n{FR_GREEN}---------- That's all for today 👌 ----------{NO_COLOR}\n")

else:
    # something wrong
    print(frRED("\n---- upsssssssss something is wrong 😢😢  ----\n"))
    pause()