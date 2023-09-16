# 
#    THIS SCRIPT IS FOR encrypt and decode texts
#

# IMPORT SECTION
import os, sys, string, random
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

    print("print empty line")
    print(f"{FR_GREEN}=== MAIN")    
    print("print empty line")
    # create list of alphabet
    string.ascii_lowercase
    'abcdefghijklmnopqrstuvwxyz'
    alphab = list(string.ascii_lowercase)
    old_alphab = list(string.ascii_lowercase)
    print(frGREEN(f"Alphabet list\n\t{old_alphab}"))    
    
    # random.shuffle() to create new_alphab
    random.shuffle(old_alphab)
    new_alphab=old_alphab       
    print(frGREEN(f"{FR_GREEN}Messy alphabet list to encrypt\n\t{new_alphab}"))
    
    print("print empty line")

    # my text
    my_text = 'abcdef ghijk lmnopq KAIXO TEACHER'
    print(f"&nbsp;\n{FR_BLUE}my text\n\t{my_text}")    

    # call encrypt function to change original text
    encripted_text = ''    
    encrypt(my_text.casefold(),alphab,new_alphab)
    print(f"{FR_RED}encrypted text\n\t{encripted_text}")    
    #print(frRED(f"encrypted text\n\t{encripted_text}"))    

    # decode process
    decoded_text=''
    decipher(encripted_text,new_alphab,alphab)
    print(f"{FR_GREEN}decoded text\n\t{decoded_text}")
    
else:
    # something wrong
    print(frRED("---- upsssssssss something is wrong ---"))
    