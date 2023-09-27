
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

# CONSTANTS

# Zip the files from given directory that matches the filter
def zipFilesInDir(dirName, zipFileName, filter):
    # create a ZipFile object
    with ZipFile(zipFileName, 'w') as zipObj:
        # Iterate over all the files in directory
        for folderName, subfolders, filenames in os.walk(dirName):
            for filename in filenames:
                if filter(filename):
                    # create complete filepath of file in directory
                    filePath = os.path.join(folderName, filename)
                    # Add file to zip
                    zipObj.write(filePath, basename(filePath))
                    print(f"filename added: {filename}")
    print()

# Zip the files from given directory that matches the filter
def zipFilesInList(paths_list, zipFileName, filter):
    # create a ZipFile object
    with ZipFile(zipFileName, 'w') as zipObj:
        for path_name in paths_list: 
            if isdir(path_name):       
                # Iterate over all the files in directory
                for folderName, subfolders, filenames in os.walk(path_name):
                #for folderName, subfolders, filenames in os.walk(paths_list[0]):
                    for filename in filenames:
                        if filter(filename):
                            # create complete filepath of file in directory
                            filePath = os.path.join(folderName, filename)
                            # Add file to zip
                            zipObj.write(filePath, basename(filePath))
                            print(f"filename added: {filename}")
            elif isfile(path_name):
                print(f"\tpath: {path_name}")

    print()

#
# ---------- MAIN ----------
#

if __name__ == "__main__":

    system('cls')
    print("\n---------- MAIN ----------\n")
    pause()
    # Name of the Directory to be added to list_paths
    dirPath = dirname(__file__)
    os.chdir(dirPath)
    dirPath = os.getcwd()
    list_paths = []
    list_paths.append(dirPath)
    #name of zip file
    dirArray = dirPath.split('\\')    
    dirName = dirArray[len(dirArray)-1]
    dirNameZip = dirName+'.zip'
    # paths to MyColor.py & MyFunc.py
    #print(f"\tdirPath: {dirPath}\n\tdirName: {dirName}\n\tlist paths: {list_paths}\n")
    static_path = dirname(dirname(dirname(__file__))) 
    print(f"static_path: {static_path}")
    print()
    MyColors_path = static_path + '\include\MyColors.py'
    list_paths.append(MyColors_path)  
    MyFunc_path = static_path + '\include\MyFunc.py'
    list_paths.append(MyFunc_path)      
    
    for path in list_paths:
        print(f"\t{path}")
    print()    

    print(f"\tdirPath: {dirPath}")   
    print(f"\tdirName: {dirName}\n")   

    # delete if exists  
    if os.path.exists(dirNameZip):
        os.remove(dirNameZip)
        print(f"\told {dirNameZip} deleted\n")    

    print(f"{FR_BLUE}*** Creating a zip archive of only .py files in\n{dirPath} ***{NO_COLOR}\n")
    zipFilesInList(list_paths, dirNameZip, lambda name : 'py' in name)
    #zipFilesInDir(dirPath, dirNameZip, lambda name : 'py' in name)

    if os.path.exists(dirNameZip):

        print(f"\t\t{dirNameZip} succesfully created !\n")

        # Copy file to folder in PC
        import shutil

        # source file path
        src_path = dirPath + '\\' + dirNameZip
        print(f"\t\tsrc_path:\n\t\t{src_path}\n")

        # Destiny file path
        # dst_path = "c:/iggPyBlog_ZipFiles"
        downloads_path = str(Path.home() / "Downloads")
        print(f"\t\tdownload path in client ---> {downloads_path}\n\n")
        dst_path = r"c:\\Users\Amatxo\Downloads" 

        """    
        if not os.path.exists(dst_path):
            os.mkdir(dst_path)
            print(f"\t\tDir {dst_path} created !!!")
        """

        if not os.path.exists(downloads_path):
            os.mkdir(downloads_path)
            print(f"\t\tDir {downloads_path} created !!!")

        #shutil.copy(src_path, dst_path)        
        #shutil.copy(src_path, downloads_path)        
        print(f"\t\tCopy Process\n\t\t{dirNameZip} Copied in folder {downloads_path}\n")   
    

    else:
        print(f"UPSSSSSS............")
    
    print(f"\n{FR_GREEN}---------- That's all for today 👌 ----------{NO_COLOR}\n")

    pause()
    

    # ------------------------------------------------
    #           ASKING FOR SHOW VARS INFO 
    #------------------------------------------------- 
    """
    # with Y_N_2 function
    yesss=True   
    while yesss:
        _msg = "Do you want to see attributes for a specific VAR ? (Y,N): "
        answer=Y_N_2(_msg)        
        if answer in ['Y','N']: yesss = False

    if answer == 'Y':            
        # add question for name of var.....
        _what_var = str(input("What VAR ? "))
        try: 
            _what_var
            _my_Obj_name = eval(_what_var)
            print(f"\n{FR_GREEN}---------- INFO FOR OBJECT '{_my_Obj_name}' ----------{NO_COLOR}\n")
            # pause()
            # my objects functions  
            mostrar(_my_Obj_name)       

        except NameError:
            print(f"\n\t{FR_RED}---- Var '{_what_var}' doesn't exits 🙄🙄  ----")
            print(f"\n{FR_GREEN}--------------- That's all for today 👌 ---------------{NO_COLOR}\n")
            #_my_Obj_name = None 

    else:
        print(f"\n{FR_GREEN}---------- That's all for today 👌 ----------{NO_COLOR}\n")
    """

else:
    # something wrong
    print(frRED("\n---- upsssssssss something is wrong 😢😢  ----\n"))
    # pause()