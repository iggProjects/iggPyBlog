
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
from zipfile import ZipFile
import os
from os import system
from os.path import basename, dirname
from pathlib import Path

# My OWN

# CONSTANTS

# Functions

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

    system('cls')
    print("\n---------- MAIN ----------\n")
    
    # Name of the Directory to be zipped
    
    dirPath = os.getcwd()
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
        dst_path = "c:/iggPyBlog_ZipFiles"
        downloads_path = str(Path.home() / "Downloads")
        print(f"\t\tdownload path in client ---> {downloads_path}\n\n")
        #dst_path = r"c:\\Users\Amatxo\Downloads" 

        if not os.path.exists(dst_path):
            os.mkdir(dst_path)
            print(f"\t\tDir {dst_path} created !!!")

        if not os.path.exists(downloads_path):
            os.mkdir(downloads_path)
            print(f"\t\tDir {downloads_path} created !!!")

        shutil.copy(src_path, dst_path)        
        shutil.copy(src_path, downloads_path)        
        print(f"\t\tCopy Process\n\t\t{dirNameZip} Copied in folder {dst_path}\n")   

    else:
        print(f"UPSSSSSS............")
    
    print(f"\n---------- That's all for today 👌 ----------\n")

else:
    # something wrong
    print("\n---- upsssssssss something is wrong 😢😢  ----\n")
    # 