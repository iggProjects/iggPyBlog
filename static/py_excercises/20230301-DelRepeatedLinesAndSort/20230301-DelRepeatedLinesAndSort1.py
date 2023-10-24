"""  
THIS SCRIPT IS FOR DELETE REPEATED LINES AND SORT RESULTING FILE

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

        """
        base_dir = os.path.dirname(os.getcwd())
        print(f"base dir: {base_dir}")
        print("print empty line")
        """    
        
        # list_paths: append Directory of file
        dirName = dirname(__file__)
        os.chdir(dirname(__file__))
        dirPath = os.getcwd()
        
        """
        # os.path.normpath(path) 
        dirArray = os.path.split(dirPath)
        fileNameZip = dirArray[1] + '.zip'
        file_zip_path = os.path.join(dirname(__file__),fileNameZip)

        """
        file_txt_path = os.path.join(dirPath,"z-fileRepeatedLines.txt")
        #file = open("z-fileRepeatedLines.txt","r")
        file = open(file_txt_path)
        #file = open("static\py_excercises\\20230301-DelRepeatedLinesAndSort\z-fileRepeatedLines.txt")
        print(f"{FR_GREEN}Read and print '{file.name}'")
        # read lines
        lines = file.readlines()
        # print lines of backup file    
        for line in lines:  
            print(f"\t{line}")
        file.close()
        print("print empty line")

        print(f"{FR_GREEN}Read file 'z-fileRepeatedLines.txt' with command <uniqlines = set('z-fileRepeatedLines.txt').readlines>")
        uniqlines = set(open(file_txt_path).readlines())
        #uniqlines = set(open('static\py_excercises\\20230301-DelRepeatedLinesAndSort\z-fileRepeatedLines.txt').readlines())
        uniqlines_bef = str(uniqlines).replace(',',';').replace('\\n','')
        print(f"\tuniqlines type is {type(uniqlines)}")
        print(f"\tuniqlines before: {uniqlines_bef}")
        print("print empty line")

        print(f"{FR_GREEN}Sort 'uniqlines' with sorted(uniqlines)")
        uniqlines = sorted(uniqlines)
        uniqlines_aft = str(uniqlines).replace(',',';').replace('\\n','')
        print(f"\tList sorted and without repeated lines: {uniqlines_aft}")
        print("print empty line")

        print(f"{FR_BLUE}Creating sorted file without repeated lines 'z-fileWithOutRepetitionLines.txt'")
        file_txt_sorted_uniq = os.path.join(dirPath,"z-fileWithOutRepetitionLines.txt")
        open(file_txt_sorted_uniq, 'w').writelines(uniqlines)
        print(f"{NO_COLOR}")

    except Exception as Argument:
        error_msg = "ERROR IN <" + my_script_name + ">. SEE server_messages.txt !"
        write_log_file("my_messages.txt",error_msg)
        write_traceback_info_1(Argument,traceback,my_script_name)        

else:
    # something wrong
    print(f"----- upsssssssss something is wrong -----")
