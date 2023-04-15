"""  
THIS SCRIPT IS FOR..................

"""
# IMPORT SECTION
from MyFunc import *
from MyColors import *
from os import  system

# CONSTANTS
# Colors
NO_COLOR = "\033[00m"
FR_RED   = "\033[91m"
FR_GREEN = "\033[92m"
FR_YELL  = "\033[93m"
FR_BLUE  = "\033[94m"
FR_MAG   = "\033[95m"

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
    print(frGREEN("\n---------- main ----------\n"))
    pause()

    # your code
    encripted_text = ''
    decoded_text = ''

    my_text = 'Mi buen amigo, como has estado?'
    print(frGREEN(f"orig text:\n {my_text}\n"))
    
    encrypt(my_text)
    print(frGREEN(f"encripted text:\n {encripted_text}\n"))
    
    decipher(encripted_text)
    print(frGREEN(f"decoded text:\n {decoded_text}\n"))

    
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

else:
    # something wrong
    print(frRED("\n---- upsssssssss something is wrong ---\n"))
    pause()