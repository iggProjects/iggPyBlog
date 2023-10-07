# 
#    THIS SCRIPT IS FOR encrypt and decode texts
#

# IMPORT SECTION
# My Own Functions from include dir 
try:   # Import My Own Functions from include dir 
    import sys, traceback, string, random
    from os import system
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

# FUNCTIONS SECTION

# funtion to encrypt a text
def encrypt(text,alphab1,alphab2):
    global encripted_text 
    for ch in text:
        # find 'ch' in new_alphab 
        if ch in alphab1:
            ind = alphab1.index(ch) 
            encripted_text += alphab2[ind]
        elif ch == ' ':
            encripted_text += ch
        else:      
            pass    

def decipher(text,alphab1,alphab2):
    global decoded_text    
    for ch in text:
        # find 'ch' in new_alphab 
        if ch in alphab1:
            ind = alphab1.index(ch) 
            decoded_text += alphab2[ind]
        elif ch == ' ':
            decoded_text += ch
        else:      
            pass    

#
# ---------- MAIN ----------
#

if __name__ == "__main__":

    try:
        # clear console screen
        system('cls')
        # get name of script
        my_script = __file__.split('\\')
        my_script_name = my_script[len(my_script)-1]
        print(frGREEN("\n---------- main ----------\n"))
        pause()

        # create list of alphabet
        string.ascii_lowercase
        'abcdefghijklmnopqrstuvwxyz'
        alphab = list(string.ascii_lowercase)
        old_alphab = list(string.ascii_lowercase)
        print(frGREEN(f"{FR_YELL}Alphabet list{NO_COLOR}\n{old_alphab}\n"))
        
        # random.shuffle() to create new_alphab
        random.shuffle(old_alphab)
        new_alphab=old_alphab       
        print(frGREEN(f"{FR_GREEN}Messy alphabet 'list' to encrypt{NO_COLOR}\n{new_alphab}\n"))
        print(frGREEN(f"{FR_GREEN}Messy alphabet 'string' to encrypt{NO_COLOR}\n{''.join(new_alphab)}\n"))
        pause()

        # my text
        my_text = 'El murcielago esta hambriento'
        #my_text = 'abcdef ghijk lmnopq KAIXO TEACHER'

        print(frGREEN(f"my text\n\t{my_text}\n"))

        # call encrypt function to change original text
        encripted_text = ''    
        encrypt(my_text.casefold(),alphab,new_alphab)
        print(frRED(f"encrypted text\n\t{encripted_text}\n"))    

        # decode process
        decoded_text=''
        decipher(encripted_text,new_alphab,alphab)
        print(f"{FR_YELL}decoded text\n\t{NO_COLOR} {decoded_text}\n")
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
                print(f"\n{FR_GREEN}---------- INFO FOR OBJECT '{_my_Obj_name}' ----------{NO_COLOR}\n")
                pause()
                # my objects functions  
                mostrar(_my_Obj_name)       

            except NameError:
                print(f"\n\t{FR_RED}---- Var '{_what_var}' doesn't exits ----")
                print(f"\n{FR_GREEN}--------------- That's all for today ---------------{NO_COLOR}\n")
                #_my_Obj_name = None 

        else:
            print(f"\n{FR_GREEN}---------- That's all for today ----------{NO_COLOR}\n")

    except Exception as Argument:
        error_msg = "ERROR IN <" + my_script_name + ">. SEE server_messages.txt !"
        write_log_file("my_messages.txt",error_msg)
        write_traceback_info(Argument,traceback,my_script_name)  

else:
    # something wrong
    print(frRED("\n---- upsssssssss something is wrong ---\n"))
    pause()