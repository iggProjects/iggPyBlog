"""  
THIS SCRIPT IS FOR..................

"""
# IMPORT SECTION
# My Own Functions from include dir 
try:   # Import My Own Functions from include dir 
    import sys, traceback
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

# get name of script
my_script = __file__.split('\\')
my_script_name = my_script[len(my_script)-1]

# FUNCTIONS
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
    
    # clear console screen
    if platform.system() == 'Windows':
        system('cls')
    elif platform.system() == 'Linux':
        system('clear')
    else:
        print(f"you OS is {platform.system()}. Find corresponding command to clear console screen")        
    
    print(frGREEN("\n---------- main ----------\n"))
    print()
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

else:
    # something wrong
    print(frRED("\n---- upsssssssss something is wrong ---\n"))
    pause()