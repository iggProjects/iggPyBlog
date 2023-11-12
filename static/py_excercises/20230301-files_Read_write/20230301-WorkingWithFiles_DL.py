"""  
THIS SCRIPT IS FOR..................

"""
#
# IMPORT SECTION
#

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
# ---------- COURSE EXCERCISE ----------
#

if __name__ == "__main__":

    try:

        # clear console screen
        clear_console_screen()
        # get name of script
        my_script = __file__.split('\\')
        my_script_name = my_script[len(my_script)-1]

        print()
        print(f"\n{FR_BLUE}---------- MAIN ----------{NO_COLOR}\n")
        print()
        pause()
        
        cwd = os.getcwd()
        print(f"\nos.cwd() --> {cwd}\n")

        # read file "agatha.txt"
        file_path = os.path.join(cwd,'z-agatha_DL.txt')
        f = open(file_path,'r')
        #f = open(agatha.txt,"r")
        lines = f.readlines()
        # save info in list of lines "agathaLines"
        agathaLines=[]
        for line in lines:
            agathaLines.append(line)
        f.close()

        # create file copy agathaBkup.txt
        fBkup = open(os.path.join(cwd,'z-agathaBackup_DL.txt'), 'w')

        # write list in copy file
        for line in agathaLines:
            fBkup.write(line)

        fBkup.close()

        # reading backup file
        f = open('z-agathaBackup_DL.txt','r')
        print(f"\n{FR_YELL}\tPrinting 'z-agatha' backup file{NO_COLOR}\n\n\t(relative path: {f.name})\n")
        pause()

        # read lines
        lines = f.readlines()

        # print lines of backup file
        print("\033[34m")
        for line in lines:  
            print(f"\t{FR_GREEN}{line}")

        f.close()
        # return default color 
        print(f"{NO_COLOR}")
        pause()
    
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
                print(f"\n{FR_GREEN}---------- INFO FOR OBJECT\n'{_my_Obj_name}' ----------{NO_COLOR}\n")
                pause()
                # my objects functions  
                mostrar(_my_Obj_name) 
                pause()   

            except NameError:
                print(f"\n\t{FR_RED}---- Var '{_what_var}' doesn't exits ----")
                print(f"\n{FR_GREEN}--------------- That's all for today  ---------------{NO_COLOR}\n")

    except Exception as Argument:
        write_traceback_info(Argument,traceback,my_script_name)        
        pause()

else:
    # something wrong
    print(f"\n{FR_RED}---- ******** ----{NO_COLOR}\n")
    