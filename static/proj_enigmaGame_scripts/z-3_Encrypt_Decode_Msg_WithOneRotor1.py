# IMPORT SECTION
import string
from os import  system

# My Own Color Constants
NO_COLOR = "\033[00m"
FR_RED   = "\033[91m"
FR_GREEN = "\033[92m"
FR_YELL  = "\033[93m"
FR_BLUE  = "\033[94m"
FR_MAG   = "\033[95m"

def alphab_jump(alph,k):
    # jump value -k to rotate list    
    return alph[-k:] + alph[:-k]

if __name__ == "__main__":

    print()

    # create list of alphabet
    #string.ascii_lowercase 
    #'abcdefghijklmnopqrstuvwxyz'
    #alphab = list(string.ascii_lowercase)

    alphab = list('xyzabcdefghijklmnopqrstuvw')    
    print(f"{FR_YELL}ALPHABET: {FR_GREEN}{' '.join(alphab)}{NO_COLOR}")
    
    print()
    
    # list of all derived alphabets with rotation by 1 to right position
    alphab_list = []  
    for jump in range(27):
        alphab_list.append(alphab_jump(alphab,jump))
        jump_2f = "{:2}".format(jump)
        print(f"alphab index: {jump_2f} | alphab: {' '.join(alphab_list[jump])}")

    # message to encrypt
    print() 
    #msg = "murcielago" 
    msg = "murcielago murcielago murcielago" 
    print()
    print(f"msg: {msg} | length: {len(msg)}")

    encrypted_msg = ""
    counter = 0
    for ch in msg:
        if ch != ' ':
            counter_2f = "{:2}".format(counter)
            print(f"ch {counter_2f}: {ch} ==> alphab.index: {alphab.index(ch)}")    

        if ch == ' ':
            encrypted_msg = encrypted_msg + ' ' 
        else:
            encrypted_msg = encrypted_msg + alphab_list[counter % 26][alphab.index(ch)]
            counter=counter+1

    print(f"{FR_GREEN}Chars counter value:{NO_COLOR} {counter} | counter % 6: {counter % 26}")          
    print()    
    print(f"{FR_YELL}Encrypted message:{NO_COLOR} {encrypted_msg} | length: {len(encrypted_msg)}") 
    print()
    print(f"============ DECODING PROCESS ============")
    print()
    print(f"{FR_BLUE}Last alphabet used in encryting process:{NO_COLOR}\n{' '.join(alphab_list[(counter % 26)-1])}")
    print()
    print(f"Starting decoding loop !")
    print()

    counter = 0
    decoded_msg = ""
    for ch in encrypted_msg:
        if ch != ' ':
            counter_2f = "{:2}".format(counter)
            index_2f = "{:2}".format(alphab_list[counter % 26].index(ch))
            print(f"ch {counter_2f}: {ch} index: {index_2f} | {' '.join(alphab_list[counter % 26])} | alphab letter: {alphab[alphab_list[counter % 26].index(ch)]}")
        if ch == ' ':
            decoded_msg = decoded_msg + ' '
        else:
            decoded_msg = decoded_msg + alphab[alphab_list[counter % 26].index(ch)]
            counter=counter+1

    print()  
    print(f"{FR_YELL}Encrypted message:{NO_COLOR} {encrypted_msg} | length: {len(encrypted_msg)}")   
    print(f"{FR_YELL}Decoded   message:{NO_COLOR} {decoded_msg} | length: {len(decoded_msg)}") 
    print()
