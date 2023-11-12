"""  
THIS SCRIPT IS FOR..................

"""
# IMPORT SECTION
import os, sys, string, random
from os import system

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

# Yes-No function
def Y_N(msg):
    global moreData    
    ans=str(input(msg))
    print(f"\t\tAnswer -> {ans}")  
    if ans == 'N':                        
        moreData=False
    elif ans == 'Y':                                
        moreData=True
    else:
        Y_N(msg)

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
    
    print("print empty line")
    print(frGREEN("---------- main ----------"))
    print("print empty line")
    pause()
    
    # create list of alphabet
    string.ascii_lowercase
    'abcdefghijklmnopqrstuvwxyz'
    alphab = list(string.ascii_lowercase)
    old_alphab = list(string.ascii_lowercase)
    print(f"{FR_YELL}Alphabet list: {NO_COLOR}{old_alphab}")
    
    # rotate alphab
    new_alphab = alphab[3:] + alphab[:3]
    
    print(f"{FR_GREEN}new alphabet list by rotation 3 places: {NO_COLOR}{new_alphab}")
        

    # my text
    my_text = 'abcdef ghijk hello world'
    print(frGREEN(f"my text{NO_COLOR}: {my_text}"))

    # call encrypt function to change original text
    encripted_text = ''    
    encrypt(my_text,alphab,new_alphab)
    print(frGREEN(f"encrypted text{NO_COLOR}: {encripted_text}"))    

    # decode process
    decoded_text=''
    decipher(encripted_text,new_alphab,alphab)
    print(frGREEN(f"decoded text{NO_COLOR}: {decoded_text}"))
    print((frGREEN("---------- That's all for today 👌 ----------")))
    pause()
   
    # ------------------------------------------------
    #      IF YOU WANT, SHOW VARS CHARACTERISTICS 
    #------------------------------------------------- 
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
            print(f"{FR_GREEN}---------- INFO FOR OBJECT '{_my_Obj_name}' ----------{NO_COLOR}")
            pause()
            # my objects functions  
            mostrar(_my_Obj_name)       

        except NameError:
            print(f"\t{FR_RED}---- Var '{_what_var}' doesn't exits  ----")
            print(f"{FR_GREEN}--------------- That's all for today ---------------{NO_COLOR}")
    

    else:
        print(f"{FR_GREEN}---------- That's all for today ----------{NO_COLOR}")
    """    

else:
    # something wrong
    print(frRED("---- ******** ----"))
    pause()