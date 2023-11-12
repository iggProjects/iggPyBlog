
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
# My Own Functions from include dir 
try:   # Import My Own Functions from include dir 
    import os, sys, traceback
    import platform
    from os import system
    from os.path import dirname, realpath
    # import My Own Func
    from MyColors import *
    from MyFunc_copy_DL import *    
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
        
        # clear console screen
        clear_console_screen()        # get name of script
        my_script = __file__.split('\\')
        my_script_name = my_script[len(my_script)-1]
        print("\n---------- MAIN ----------\n")
        print()
        pause()

        # list_paths: append Directory of file
        dirPath = dirname(__file__)
        os.chdir(dirPath)
        dirPath = os.getcwd()
        print(f"dirPath: {dirPath}")
        list_paths = []
        list_paths.append(dirPath)

        # name of zip file
        dirArray = dirPath.split('\\')    
        dirName = dirArray[len(dirArray)-1]
        fileNameZip = dirName + '.zip'
        print(f"fileNameZip: {fileNameZip}")

        # list_paths: append paths to MyColor.py & MyFunc.py
        #static_path = dirname(dirname(dirname(__file__))) 
        #print(f"static_path: {static_path}")
        print()
        
        MyColors_path = os.path.join(dirPath,'MyColors.py')
        list_paths.append(MyColors_path)  
        """
        MyFunc_path = os.path.join(dirPath,'MyFunc_copy_DL.py')
        list_paths.append(MyFunc_path)      
        """
        
        for path in list_paths:
            print(f"\t{path}")
        print()    
        
        # delete if exists  
        if os.path.exists(fileNameZip):
            os.remove(fileNameZip)
            print(f"===> file '{fileNameZip}' deleted")
            print()    

        print(f"{FR_BLUE}*** Creating Zip File '{fileNameZip}' ***{NO_COLOR}")
        print()

        zipFilesInList(list_paths, fileNameZip, lambda name: 'DL' in name)
        print()
        print(f"{FR_BLUE}*** Zip File Created ***{NO_COLOR}")    
        pause()
    
        print(f"\n{FR_GREEN}---------- That's all for today 👌 ----------{NO_COLOR}\n")

        pause()
        

        # ------------------------------------------------
        #           ASKING FOR SHOW VARS INFO 
        #------------------------------------------------- 
        
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
    
    except Exception as Argument:
        write_traceback_info(Argument,traceback,my_script_name)        
        pause()
  
else:
    # something wrong
    print(frRED("\n---- ******** ----\n"))
    # pause()