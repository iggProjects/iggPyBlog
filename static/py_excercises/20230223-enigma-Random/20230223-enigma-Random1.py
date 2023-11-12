# 
#    THIS SCRIPT IS FOR encrypt and decode texts
#

# IMPORT SECTION

try:   # Import My Own Functions from include dir 
    import sys, traceback, string, random    
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
        
    try:
        # get name of script
        my_script = __file__.split('\\')
        my_script_name = my_script[len(my_script)-1]
        write_log_file("my_messages.txt","IN '" + my_script_name + "'")
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

    except Exception as Argument:
        error_msg = "ERROR IN <" + my_script_name + ">. SEE server_messages.txt !"
        write_log_file("my_messages.txt",error_msg)
        write_traceback_info_1(Argument,traceback,my_script_name)        

else:
    # something wrong
    print(frRED("---- ******** ---"))
    