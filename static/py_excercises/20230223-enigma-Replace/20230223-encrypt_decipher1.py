"""  
THIS SCRIPT IS FOR..................

"""
# IMPORT SECTION

import os, sys
from os import  system

# include root path in sys.path
ROOT_DIR = os.path.abspath(os.curdir)
# check in what server is app
if "iggWebNz" in ROOT_DIR:              # pythonanywhere  
    ROOT_DIR = ROOT_DIR + "/mysite"
else:                                   # working in localhost server
    pass 
sys.path.insert(1, ROOT_DIR)

# import "My Own Funct" from root path
from MyFunc import *


# CONSTANTS

# print char by char
def print_char_by_char(my_text):
    for ch in my_text:
        print(ch)

# funtion to encrypt a text
def encrypt(text):
    global encripted_text        
    #list_changes_chars = {'a':128, 'b':129, 'c':130}    
    text=text.replace('a','128') 
    text=text.replace('b','129')
    text=text.replace('c','130')    
    encripted_text=text

def decipher(text):
    global decoded_text    
    text=text.replace('128','a')
    text=text.replace('129','b')
    text=text.replace('130','c')    
    decoded_text = text

#
# ---------- MAIN ----------
#
if __name__ == "__main__":
    
    system('cls')
    print(frGREEN("---------- main ----------"))
    pause()

    # your code
    encripted_text = ''
    decoded_text = ''

    my_text = 'Mi buen amigo, como has estado?'
    print(frGREEN(f"orig text: {my_text}"))
    
    encrypt(my_text)
    print(frGREEN(f"encripted text: {encripted_text}"))
    
    decipher(encripted_text)
    print(frGREEN(f"decoded text: {decoded_text}"))

    
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
            print(f"{FR_GREEN}---------- INFO FOR OBJECT '{_my_Obj_name}' ----------{NO_COLOR}")
            pause()
            # my objects functions  
            mostrar(_my_Obj_name)       

        except NameError:
            print(f"\t{FR_RED}---- Var '{_what_var}' doesn't exits ----")
            print(f"{FR_GREEN}--------------- That's all for today ---------------{NO_COLOR}")
            #_my_Obj_name = None 

    else:
        print(f"{FR_GREEN}---------- That's all for today ----------{NO_COLOR}")

else:
    # something wrong
    print(frRED("---- ******** ---"))
    pause()