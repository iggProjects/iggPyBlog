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
        

https://stackoverflow.com/questions/1855095/how-to-create-a-zip-archive-of-a-directory

def zipdir(path, ziph):
    # ziph is zipfile handle
    for root, dirs, files in os.walk(path):
        for file in files:
            ziph.write(os.path.join(root, file), 
                       os.path.relpath(os.path.join(root, file), 
                                       os.path.join(path, '..')))

with zipfile.ZipFile('Python.zip', 'w', zipfile.ZIP_DEFLATED) as zipf:
    zipdir('tmp/', zipf)        

********************************
    zf = zipfile.ZipFile("myzipfile.zip", "w")
    for dirPath, subdirs, files in os.walk(dirPath):
        zf.write(dirPath)
        for filename in files:
            zf.write(os.path.join(dirPath, filename))
    zf.close()    
    


"""

# IMPORT SECTION
try:   # Import My Own Functions from include dir 
    import os, sys, traceback, zipfile     
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

# Functions for zip file
# https://techoverflow.net/2022/09/24/how-to-zip-folder-recursively-using-python-zipfile/
# https://stackoverflow.com/questions/10480440/zip-folder-with-subfolder-in-python
def zip_compression_tree(root_path, zip_name):
    with zipfile.ZipFile(zip_name, 'w') as z:
        for root, dirs, files in os.walk(root_path):
            for file in files:                
                z.write(os.path.join(root, file))
            for directory in dirs:
                z.write(os.path.join(root, directory))

"""
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
                    print(f"file added: {filename}")
            for subfolder in subfolders:
                subfolderPath = os.path.join(folderName, subfolder)
                zipObj.write(subfolderPath, basename(subfolderPath))        
    print()

"""

#
# ---------- MAIN ----------
#

if __name__ == "__main__":

    system('cls')
    print("\n---------- MAIN ----------\n")
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

    zip_compression_tree(dirPath, fileNameZip)

    """
    zf = ZipFile("myzipfile.zip", "w")
    dirPath1 = dirname(__file__)
    print(f"===> dirPath1 '{dirPath1}'")
    for dirPath1, subdirs, files in os.walk(dirPath):
        zf.write(dirPath1)
        for filename in files:
            zf.write(os.path.join(dirPath1, filename))
    zf.close() 
    """
    #fileNameZip1 = dirName+'-9'+'.zip'
    #zipFilesInDir(dirPath,fileNameZip1,lambda name: 'py' or 'DL' in name)
    
    if os.path.exists(fileNameZip):

        print()
        print(f"{FR_BLUE}{fileNameZip} succesfully created !{NO_COLOR}")
        print()
        pause()

        # Copy file to folder in PC
        import shutil

        # source file path
        src_path = dirPath + '\\' + fileNameZip
        print(f"{FR_GREEN}src_path{NO_COLOR}")
        print(f"{src_path}")
        print()

        # Destiny file path
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