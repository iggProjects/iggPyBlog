
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

#
# ---------- MAIN ----------
#

if __name__ == "__main__":

    print("\n---------- MAIN ----------\n")
    
    # Name of the Directory to be zipped    
    dirPath = dirname(__file__)
    print(f"dirPath: {dirPath}\nos.getcwd(): {os.getcwd()}")
    #dirPath = os.getcwd()
    dirArray = dirPath.split('\\')
    dirName = dirArray[len(dirArray)-1]
    dirNameZip = dirName+'.zip'
    print(f"\tdirPath: {dirPath}\n\tdirName: {dirName}\n")   

    # delete if exists  
    if os.path.exists(dirNameZip):
        os.remove(dirNameZip)
        print(f"\told {dirNameZip} deleted\n")    

    print(f"\t*** Creating a zip archive of only .py files in {dirPath} ***\n")
    zipFilesInDir(dirPath, dirNameZip, lambda name : 'py' in name)

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
        shutil.copy(src_path, downloads_path)        
        print(f"\t\tCopy Process\n\t\t{dirNameZip} Copied in folder {downloads_path}\n")   
    

    else:
        print(f"UPSSSSSS............")
    
    print(f"\n{FR_GREEN}---------- That's all for today 👌 ----------{NO_COLOR}\n")

else:
    # something wrong
    print(frRED("\n---- upsssssssss something is wrong 😢😢  ----\n"))
    # pause()