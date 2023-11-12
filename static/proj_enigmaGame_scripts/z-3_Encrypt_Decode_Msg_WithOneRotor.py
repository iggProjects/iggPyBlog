"""  
    
    THIS SCRIPT IS FOR .............

"""
# IMPORT SECTION

try:   # Import My Own Functions from include dir 
    import sys, traceback, string
    import numpy as np   
    from os.path import dirname, realpath
    from os import scandir
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
    print() 
    print(f"{FR_RED}IMPORT ERROR ==>{NO_COLOR} {ImportError} | {ImportError.__class__} | {ImportError.__doc__}")

# ---------- CONSTANTS & FUNCTIONS ----------

def alphab_jump(alph,k):
    # jump value -k to rotate list    
    return alph[-k:] + alph[:-k]

#
# ---------- MAIN ----------
#

if __name__ == "__main__":

    try:

        clear_console_screen()

        my_script = __file__.split('\\')
        my_script_name = my_script[len(my_script)-1]
        print()
        write_log_file("my_messages.txt","IN '" + my_script_name + "'")
        print()

        print(f"{FR_GREEN}---------- MAIN ----------{NO_COLOR}")
        print()

        # create list of alphabet
        string.ascii_lowercase 
        'abcdefghijklmnopqrstuvwxyz'
        alphab_orig = list(string.ascii_lowercase)
        #alphab = list('uvwxyzabcdefghijklmnopqrst')  # orig alphab rotated
        alphab = list('yzxuqrbapsfwjdtgiomhvelckn')  # a permutation of the alphab that is not a rotation    

        print(f"{FR_BLUE}== INITIAL PERMUTED ALPHABET:  {FR_GREEN}{' '.join(alphab)} ==={NO_COLOR}")

        print()
        print(f"{FR_GREEN}List of the {len(alphab)-1} distinct rotations of permuted alphabet{NO_COLOR}")
        print()

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
        print()    
        print(f"============ MESSAGE TO ENCRYPT ============")
        #msg = "murcielago murcielago murcielago murcielago murcielago murcielago murcielago" 
        print()
        print(f"{FR_BLUE}msg: {msg} | length: {len(msg)}{NO_COLOR}")
        print()

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
        print()    
        print(f"============ ENCRYPTING PROCESS ============")
        print()
        print(f"{FR_RED}Encrypted message:{NO_COLOR} {encrypted_msg} | length: {len(encrypted_msg)}") 
        print()
        print(f"{FR_BLUE}Last alphabet used in encrypting process:{NO_COLOR}\n{' '.join(alphab_list[(counter % 26)-1])}")
        print()

        print(f"============ DECODING PROCESS ============")
        print()

        print(f"{FR_BLUE}Original Alphabet==> {NO_COLOR}{' '.join(alphab_orig)} | length: {len(alphab_orig)}")
        print()


        counter = 0
        decoded_msg = ""
        for ch in encrypted_msg:
            if ch == ' ':
                decoded_msg = decoded_msg + ' '
            else:
                ind = alphab_list[counter % 26].index(ch)
                counter_2f = "{:2}".format(counter)
                index_2f = "{:2}".format(ind)    
                print(f"ch {counter_2f}: {ch} index: {index_2f} | {' '.join(alphab_list[counter % 26])} | orig alphab: {alphab_orig[ind]}")
                decoded_msg = decoded_msg + alphab_orig[ind]
                counter=counter+1

        print()  
        print(f"{FR_RED}Encrypted message:{NO_COLOR} {encrypted_msg} | length: {len(encrypted_msg)}")   
        print(f"{FR_BLUE}Decoded   message:{NO_COLOR} {decoded_msg} | length: {len(decoded_msg)}") 
        print()

        print(f"{FR_GREEN}---------- That's all for today ----------{NO_COLOR}")
        print()
        pause()

    except Exception as Argument:
        error_msg = "ERROR IN <" + my_script_name + ">. SEE server_messages.txt !"
        write_log_file("my_messages.txt",error_msg)
        write_traceback_info_1(Argument,traceback,my_script_name)
        pause()     
    
else:
    # something wrong
    print(frRED("---- ********** ----"))
