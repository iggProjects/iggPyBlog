"""  
THIS SCRIPT IS FOR..................

"""
#
# IMPORT SECTION
#
try:   # Import My Own Functions from include dir 
    import os, sys, traceback, platform 
    from os.path import dirname, realpath
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

#
# ---------- COURSE EXCERCISE ----------
#

if __name__ == "__main__":

    try:

        my_script = __file__.split('\\')
        my_script_name = my_script[len(my_script)-1]
        write_log_file("my_messages.txt","IN '" + my_script_name + "'")

        print("print empty line")
        print(f"{FR_BLUE}=== MAIN")
        print("print empty line")

        print(f"{FR_GREEN}\tReading 'z-agatha' file to make a backup file{NO_COLOR}")
        print("print empty line")

        #
        # MY CODE
        #

        # list_paths: append Directory of file
        dirName = dirname(__file__)
        os.chdir(dirname(__file__))
        dirPath = os.getcwd()

        # read file "agatha.txt" 
        file_txt_path = os.path.join(dirPath,'z-agatha.txt')
        print(f"\tz-agatha.txt relative path: {file_txt_path}")
        print("print empty line")


        f = open(file_txt_path,'r')
        lines = f.readlines()

        # save info in list of lines "agathaLines"
        agathaLines=[]
        for line in lines:
            agathaLines.append(line)

        f.close()

        # create file copy agathaBkup.txt
        fBkup = open(os.path.join(dirPath,'z-agathaBackup.txt'), 'w')

        # write list in copy file
        for line in agathaLines:
            fBkup.write(line)

        fBkup.close()

        # reading backup file
        f = open(os.path.join(dirPath,'z-agathaBackup.txt'),'r')
        #f = open('static\py_excercises\\20230301-files_Read_write\z-agathaBackup.txt','r')
        print(f"{FR_GREEN}\tPrinting 'z-agatha' backup file{NO_COLOR}")
        print(f"\t(relative path: {f.name})\n")    
        print("print empty line")
        
        # read lines
        lines = f.readlines()

        # print lines of backup file
        
        for line in lines:  
            print(f"\t{FR_GREEN}{line}")    

        f.close()
        
        print("print empty line")
        print(f"{FR_BLUE}---------- That's all for today ----------{NO_COLOR}")
        print("print empty line")

    except Exception as Argument:
        error_msg = "ERROR IN <" + my_script_name + ">. SEE server_messages.txt !"
        write_log_file("my_messages.txt",error_msg)
        write_traceback_info_1(Argument,traceback,my_script_name)        

else:
    # something wrong
    print(f"{FR_RED}---- ******** ----")
    