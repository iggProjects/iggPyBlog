# 
#    THIS SCRIPT IS FOR encrypt and decode texts
#

# IMPORT SECTION
import string
import random
from os import system

from MyFunc import *
from MyColors import *

# CONSTANTS
# Colors
NO_COLOR = "\033[00m"
FR_RED   = "\033[91m"
FR_GREEN = "\033[92m"
FR_YELL  = "\033[93m"
FR_BLUE  = "\033[94m"
FR_MAG   = "\033[95m"

# FUNCIONS SECTION

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

    system('cls')
    
    print(frGREEN("\n---------- main ----------\n"))

    # create list of alphabet
    string.ascii_lowercase
    'abcdefghijklmnopqrstuvwxyz'
    alphab = list(string.ascii_lowercase)
    old_alphab = list(string.ascii_lowercase)
    print(f"{FR_GREEN}old alphabet list:{NO_COLOR}\t{old_alphab}\n")
    
    # random.shuffle() to create new_alphab
    random.shuffle(old_alphab)
    #new_alphab=old_alphab  
    new_alphab = list('mcspifrhajkbdguoqletnvwxyz')     
    print(f"{FR_GREEN}new alphabet list:{NO_COLOR}\t{new_alphab}\n")
    pause()

    # my text
    my_text = "El murcielago esta hambriento"
    # my_text = 'abcdef ghijk lmnopq KAIXO TEACHER'

    print(f"{FR_GREEN}my text:{NO_COLOR}\t{my_text}\n")

    # call encrypt function to change original text
    encripted_text = ''    
    encrypt(my_text.casefold(),alphab,new_alphab)
    print(f"{FR_GREEN}encrypted text:{NO_COLOR}\t{encripted_text}\n") 

    # decode process
    decoded_text=''
    decipher(encripted_text,new_alphab,alphab)
    print(f"{FR_YELL}decoded text:{NO_COLOR}\t{decoded_text}\n")
    pause()

    # ------------------------------------------------
    #          SHOW VARS CHARACTERISTICS 
    #------------------------------------------------ 

    """
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
            print(f"\n\t{FR_RED}---- Var '{_what_var}' doesn't exits 🙄🙄  ----")
            print(f"\n{FR_GREEN}--------------- That's all for today 👌 ---------------{NO_COLOR}\n")
            #_my_Obj_name = None 

    else:
        print(f"\n{FR_GREEN}---------- That's all for today 👌 ----------{NO_COLOR}\n")
    """
else:
    # something wrong
    print(frRED("\n---- upsssssssss something is wrong 😢😢  ---\n"))
    pause()