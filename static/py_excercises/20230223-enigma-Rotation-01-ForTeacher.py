"""  
THIS SCRIPT IS FOR..................

"""
# IMPORT SECTION
from MyFunc_ForTeacher import *
from Colors_ForTeacher import *
import string
import random


# Yes-No function
def Y_N(msg):
    global moreData    
    ans=str(input(msg))
    print(f"\t\tAnswer -> {ans}\n")  
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
    print(frGREEN("\n---------- main ----------\n"))

    # create list of alphabet
    string.ascii_lowercase
    'abcdefghijklmnopqrstuvwxyz'
    alphab = list(string.ascii_lowercase)
    old_alphab = list(string.ascii_lowercase)
    print(frGREEN(f"old alphabet list ➡  {NO_COLOR}{old_alphab}\n"))
    
    # random.shuffle() to create new_alphab
    random.shuffle(old_alphab)
    new_alphab=old_alphab       
    print(frGREEN(f"new alphabet list ➡  {NO_COLOR}{new_alphab}\n"))
    

    # my text
    my_text = 'abcdef ghijk hello world'
    print(frGREEN(f"my text ➡  {NO_COLOR}{my_text}\n"))

    # call encrypt function to change original text
    encripted_text = ''    
    encrypt(my_text,alphab,new_alphab)
    print(frGREEN(f"encrypted text ➡  {NO_COLOR}{encripted_text}\n"))    

    # decode process
    decoded_text=''
    decipher(encripted_text,new_alphab,alphab)
    print(frGREEN(f"decoded text ➡ \033[00m {decoded_text}\n"))
    print((frGREEN("\n---------- That's all for today 👌 ----------\n")))
    pause()
   
    # ------------------------------------------------
    #      IF YOU WANT, SHOW VARS CHARACTERISTICS 
    #------------------------------------------------- 
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

    else:
        print(f"\n{FR_GREEN}---------- That's all for today 👌 ----------{NO_COLOR}\n")

else:
    # something wrong
    print(frRED("\n---- upsssssssss something is wrong 😢😢  ---\n"))
    pause()