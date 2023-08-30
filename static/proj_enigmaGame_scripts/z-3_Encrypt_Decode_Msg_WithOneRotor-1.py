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

    print("print empty line")

    # create list of alphabet
    string.ascii_lowercase 
    'abcdefghijklmnopqrstuvwxyz'
    alphab_orig = list(string.ascii_lowercase)
    #alphab = list('uvwxyzabcdefghijklmnopqrst')  # orig alphab rotated
    alphab = list('yzxuqrbapsfwjdtgiomhvelckn')  # a permutation of the alphab that is not a rotation
    
        
    print(f"{FR_BLUE}== INITIAL PERMUTED ALPHABET:  {FR_GREEN}{' '.join(alphab)} ==={NO_COLOR}")
    
    print("print empty line")
    print(f"{FR_GREEN}List of the {len(alphab)-1} distinct rotations of permuted alphabet{NO_COLOR}")
    print("print empty line")
    
    # list of all derived alphabets with rotation by 1 to right position
    alphab_list = []  
    for jump in range(27):
        alphab_list.append(alphab_jump(alphab,jump))
        jump_2f = "{:2}".format(jump)
        if jump != 26:
            print(f"permuted alphab rotation: +{jump_2f} | alphab: {' '.join(alphab_list[jump])}")
        else:
            print(f"permuted alphab rotation: +{jump_2f} | alphab: {' '.join(alphab_list[jump])}{FR_BLUE} <== INITIAL PERM ALPHAB{NO_COLOR}")

    # message to encrypt
    msg = "el murcielago no come murcielagos" 
    print("print empty line")    
    print(f"============ MESSAGE TO ENCRYPT ============")
    #msg = "murcielago murcielago murcielago murcielago murcielago murcielago murcielago" 
    print("print empty line")
    print(f"{FR_BLUE}msg: {msg} | length: {len(msg)}{NO_COLOR}")
    print("print empty line")

    encrypted_msg = ""
    counter = 0
    for ch in msg:
    
        if ch == ' ':
            encrypted_msg = encrypted_msg + ' ' 
        else:
            #counter_2f = "{:2}".format(counter)
            #print(f"ch {counter_2f}: {ch} ==> alphab_orig.index: {alphab_orig.index(ch)}") 

            encrypted_msg = encrypted_msg + alphab_list[counter % 26][alphab_orig.index(ch)]
            counter=counter+1

    print(f"{FR_GREEN}Chars != ' ' counter value: {counter}{NO_COLOR} | counter % 26: {counter % 26}")          
    print("print empty line")    
    print(f"============ ENCRYPTING PROCESS ============")
    print("print empty line")
    print(f"{FR_RED}Encrypted message:{NO_COLOR} {encrypted_msg} | length: {len(encrypted_msg)}") 
    print("print empty line")
    print(f"{FR_BLUE}Last alphabet used in encrypting process:{NO_COLOR}\n{' '.join(alphab_list[(counter % 26)-1])}")
    print("print empty line")

    print(f"============ DECODING PROCESS ============")
    print("print empty line")

    print(f"{FR_BLUE}Original Alphabet==> {NO_COLOR}{' '.join(alphab_orig)} | length: {len(alphab_orig)}")
    print("print empty line")


    counter = 0
    decoded_msg = ""
    for ch in encrypted_msg:
        if ch != ' ':
            if counter < 10:
                counter_2f = '0'+ str(counter)
            else:
                counter_2f = counter    
            if alphab_list[counter % 26].index(ch) < 10:
                index_2f = '0' + str(alphab_list[counter % 26].index(ch))  
            else:
                index_2f = "{:2}".format(alphab_list[counter % 26].index(ch))              
            """
            counter_2f = "{:2}".format(counter)
            index_2f = "{:2}".format(alphab_list[counter % 26].index(ch))       
            """
            print(f"ch {counter_2f}: {ch} index: {index_2f} | {' '.join(alphab_list[counter % 26])} | orig alphab: {alphab_orig[alphab_list[counter % 26].index(ch)]}")
        if ch == ' ':
            decoded_msg = decoded_msg + ' '
        else:
            decoded_msg = decoded_msg + alphab_orig[alphab_list[counter % 26].index(ch)]
            counter=counter+1

    print("print empty line")  
    print(f"{FR_RED}Encrypted message:{NO_COLOR} {encrypted_msg} | length: {len(encrypted_msg)}")   
    print(f"{FR_BLUE}Decoded   message:{NO_COLOR} {decoded_msg} | length: {len(decoded_msg)}") 
    print("print empty line")
