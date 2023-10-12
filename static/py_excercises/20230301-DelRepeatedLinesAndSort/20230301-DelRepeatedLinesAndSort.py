"""  
THIS SCRIPT IS FOR DELETE REPEATED LINES AND SORT RESULTING FILE

"""
#
# IMPORT SECTION
#
try:   # Import My Own Functions from include dir 
    import os, sys, traceback, platform  
    from os.path import dirname, realpath
    from os import system
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
        
        # clear console screen
        if platform.system() == 'Windows':
            system('cls')
        elif platform.system() == 'Linux':
            system('clear')
        else:
            print(f"you OS is {platform.system()}. Find corresponding command to clear console screen")        

        my_script = __file__.split('\\')
        my_script_name = my_script[len(my_script)-1]
        write_log_file("my_messages.txt","IN '" + my_script_name + "'")

        print()
        print(f"\n{FR_BLUE}=== MAIN{NO_COLOR}\n")
        print()
        pause()

        cwd = os.getcwd()
        print(f"cwd: {cwd}")
        #base_dir = os.path.dirname(os.getcwd())
        #print(f"base dir: {base_dir}")
        file_path = os.path.join(cwd, 'static\py_excercises\\20230301-DelRepeatedLinesAndSort\z-fileRepeatedLines.txt')
        # static\py_excercises\20230301-DelRepeatedLinesAndSort\20230301-DelRepeatedLinesAndSort.py
        print(f"file: {file_path}")
        file = open(file_path,"r")
        #file = open("z-fileRepeatedLines.txt","r")
        print(f"\n{FR_YELL}\tRead and print '{file.name}'{NO_COLOR}\n")
        # read lines
        lines = file.readlines()
        # print lines of backup file    
        for line in lines:  
            print(f"\t\t{line}")
        file.close()

        print(f"{FR_YELL}\tRead 'file z-fileRepeatedLines.txt' with 'uniqlines = set('z-fileRepeatedLines.txt').readlines'{NO_COLOR}\n")
        uniqlines = set(open('static\py_excercises\\20230301-DelRepeatedLinesAndSort\z-fileRepeatedLines.txt').readlines())
        uniqlines_bef = str(uniqlines).replace(',',';').replace('\\n','')
        print(f"\tuniqlines before: {uniqlines_bef}\n")

        print(f"{FR_YELL}\tSort \"uniqlines\" with sorted(uniqlines){NO_COLOR}\n")
        uniqlines = sorted(uniqlines)
        uniqlines_aft = str(uniqlines).replace(',',';').replace('\\n','')

        print(f"\tuniqlines type is {type(uniqlines)}\n")
        print(f"\tuniqlines after: {uniqlines_aft}\n")

        print(f"{FR_YELL}\tCreating sorted file without repeated lines \"z-fileWithOutRepetitionLines.txt\"\n")
        open('static\py_excercises\\20230301-DelRepeatedLinesAndSort\z-fileWithOutRepetitionLines.txt', 'w').writelines(uniqlines)

        pause()

    except Exception as Argument:
        error_msg = "ERROR IN <" + my_script_name + ">. SEE server_messages.txt !"
        write_log_file("my_messages.txt",error_msg)
        write_traceback_info(Argument,traceback,my_script_name)        

else:
    # something wrong
    print(f"----- upsssssssss something is wrong -----")

    # ------------------------------------------------
    #          SHOW VARS CHARACTERISTICS 
    #------------------------------------------------ 
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
            pause()
            # my objects functions  
            mostrar(_my_Obj_name)   
            pause()    

        except NameError:
            print(f"\n\t{FR_RED}---- Var '{_what_var}' doesn't exits 🙄🙄  ----")
            print(f"\n{FR_GREEN}--------------- That's all for today 👌 ---------------{NO_COLOR}\n")

    else:
        print(f"\n{FR_GREEN}---------- That's all for today 👌 ----------{NO_COLOR}\n")
