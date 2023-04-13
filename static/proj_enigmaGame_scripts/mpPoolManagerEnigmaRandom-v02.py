# https://superfastpython.com/multiprocessing-pool-stop-all-tasks/
# SuperFastPython.com
# example of safely stopping all tasks in the process pool

from time import sleep
from multiprocessing import Event
from multiprocessing import Manager
from multiprocessing.pool import Pool
from os import system
import random
from random import randrange

import string
from MyFunc import pause

# CONSTANTS
# Colors
NO_COLOR = "\033[00m"
FR_RED   = "\033[91m"
FR_GREEN = "\033[92m"
FR_YELL  = "\033[93m"
FR_BLUE  = "\033[94m"
FR_MAG   = "\033[95m"

# my text
ALPHAB_STR = 'abcdefghijklmnopqrstuvwxyz'
ORIG_ALPHAB = list(string.ascii_lowercase)      # in list mode
ALPHAB = list(string.ascii_lowercase)
MY_TEXT = 'abcdef ghijk lmnopq KAIXO TEACHER'

ALPHAB_TO_ENCRYPT  = ['j', 'h', 'm', 'a', 'r', 'e', 'd', 'i', 'q', 'o', 't', 'c', 'g', 'f', 's', 'p', 'u', 'n', 'z', 'v', 'k', 'w', 'y', 'l', 'x', 'b']     
ENCRYPTED_TEXT = 'jhmare diqot cgfspu tjqls vrjmirn'

# FUNCIONS SECTION

def decipher(alphab1, event):
    
    decoded_text = ''     
    for ch in ENCRYPTED_TEXT:
        # find 'ch' in new_alphab 
        if ch in alphab1:
            ind = alphab1.index(ch) 
            decoded_text += ALPHAB[ind]
        elif ch == ' ':
            decoded_text += ch
        else:      
            pass 
    
    if MY_TEXT.casefold() == decoded_text:
        print(f'{FR_GREEN}\n\tdecode text: {NO_COLOR}{decoded_text} {FR_YELL}------ BINGO ------ BINGO ------{NO_COLOR}\n')
        print(f'{FR_MAG}\t...stopping...{NO_COLOR}', flush=True)
        event.set()
    else:
        print(f'{FR_GREEN}\n\tdecode text: {NO_COLOR}{decoded_text}')

# protect the entry point
if __name__ == '__main__':
    # clean screen
    system('cls')
    print(f"{FR_GREEN}\n---------- main ----------\n\n{NO_COLOR}")   
    print(f"{FR_YELL}Original Alphabet:{NO_COLOR}\n{ORIG_ALPHAB}\n")
    print(f"{FR_GREEN}Original text:{NO_COLOR}\n\t{MY_TEXT}\n")

    # create the manager
    with Manager() as manager:
        # create the shared event
        event = manager.Event()
        print(f'\n{FR_YELL}From Main - With Manager() as manager:{NO_COLOR}\n\tevent -> {event}\n', flush=True)

        # create and configure the process pool
        # Note: if you do not put a valid number of CPU's, Pool() assume the maximum of PC 
        with Pool(4) as pool:   

            # prepare arguments            
            messy_alphab1 = ['w', 'n', 'y', 'x', 'o', 'v', 'r', 'l', 'u', 'z', 'q', 'a', 'b', 'm', 'd', 'h', 'f', 'c', 's', 't', 'k', 'e', 'g', 'i', 'p', 'j']
            print(f"{FR_GREEN}Random Messy Alphabet used to encrypt original text:\n{NO_COLOR}{ALPHAB_TO_ENCRYPT}\n")
            pause()

            messy_alphabets = []            
            messy_alphabets.append(messy_alphab1)
            messy_alphabets.append(messy_alphab1)
            messy_alphabets.append(messy_alphab1)
            messy_alphabets.append(ALPHAB_TO_ENCRYPT)
            messy_alphabets.append(messy_alphab1)
            messy_alphabets.append(messy_alphab1)
            messy_alphabets.append(messy_alphab1)            

            alphabets = [(messy_alphabets[i],event) for i in range(len(messy_alphabets))]

            print(f'{FR_YELL}From Main - With Pool() as pool:{NO_COLOR}\n\tpool -> {pool}\n', flush=True)
            for alphabet in alphabets:
                print(f'{FR_YELL}From Main:{NO_COLOR} decipher with {alphabet} running', flush=True)    
            print()

            # issue tasks asynchronously
            result = pool.starmap_async(decipher, alphabets)
          
            # safely stop the issued tasks
            sleep(5)
            print(f'\n{FR_MAG}Safely stopping all tasks{NO_COLOR}\n')
            
            # wait for all tasks to stop            
            print(f'\n{FR_RED}=== ALL TASKS STOPED ==={NO_COLOR}\n')
            result.wait()