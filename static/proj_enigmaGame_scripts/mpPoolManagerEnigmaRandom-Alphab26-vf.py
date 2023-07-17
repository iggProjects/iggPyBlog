# https://superfastpython.com/multiprocessing-pool-stop-all-tasks/
# SuperFastPython.com
# example of safely stopping all tasks in the process pool

import time
from time import sleep
from datetime import datetime
from multiprocessing import Event
from multiprocessing import Manager, cpu_count
from multiprocessing.pool import Pool
import os
from os import system
#import random
from random import randrange
import string

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
#ALPHAB_15_STR        = 'abcdegilmnoprsu'
#ALPHAB_15_TO_ENCRYPT = list('mcspirabdguolen')
ALPHAB_TO_ENCRYPT = 'mcspifrhajkbdguoqletnvwxyz'
#ALPHAB_TO_ENCRYPT = list('mcspifrhajkbdguoqletnvwxyz')
TEMP_LIST = ['m', 'c', 's', 'p', 'i', 'f', 'r', 'h', 'a', 'j', 'k', 'b', 'd', 'g', 'u', 'o', 'q', 'l', 'e', 't', 'n', 'v', 'w', 'x', 'y', 'z']
MY_TEXT = 'El murcielago esta hambriento'
ENCRYPTED_TEXT = 'ib dnlsaibmru ietm hmdclaigtu'

# FUNCIONS SECTION

# pause function
def pause():  
  userInput = input(f"{FR_RED}Press ENTER to continue, or CTRL-C to exit{NO_COLOR}\n")  

def decipher(alphab1, event):

    if event.is_set():
        return
    else:  
                
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
            print(f"\t{FR_YELL}------ BINGO ------ BINGO ------ BINGO ------ BINGO ------ BINGO ------ BINGO -------")
            print(f'\n\t{FR_GREEN}Parent Process "{os.getppid()}" | Child Process "{os.getpid()}" --> THE SOLUTION WAS FOUND !{NO_COLOR}') 
            #print(f"{FR_GREEN}\tPID process child: {os.getpid} {NO_COLOR}\n")
            print(f"\n\t\t{FR_GREEN}Decoded text is correct: {NO_COLOR}{decoded_text}")
            print(f"\t\t{FR_GREEN}Encrypted text: {NO_COLOR}{ENCRYPTED_TEXT}")
            print(f'\t\t{FR_GREEN}Correct Alphabet Decoder: {NO_COLOR}{(",".join(alphab1_26))}', flush=True)
            print(f"\n\t{FR_YELL}-------------------------------------------------------------------------------------")
            print(f"\n\t\033[2;33;41m-------- STOP PROCESS STARTED --------{NO_COLOR}\n")
            event.set()

# protect the entry point
if __name__ == '__main__':
    # clean screen
    system('cls')
    # time
    inicio = time.time()

    print(f'\n{FR_GREEN}\t================ "Multiprocess started with pid: {os.getpid()}"" ================\n{NO_COLOR}')
    print(f'{FR_YELL}\n\t--- reading file of sub alphab str started at "{datetime.now()}" ---{NO_COLOR}\n')

    messy_alphabets = []
    #messy_alphabets.append(ALPHAB_15_TO_ENCRYPT)  
    messy_lines = set(open('z-permutFileSorted.txt').readlines())
    for messy_str in messy_lines:
        #messy_alphabets.append(list(messy_str))
        messy_alphabets.append(messy_str)
    messy_alphabets.append(ALPHAB_TO_ENCRYPT)
    print(f"........... messy_alphabets[0] ===> {messy_alphabets[0]}")
    print(f"........... messy_alphabets[500001] ===> {messy_alphabets[500000]}")

    print(f'{FR_YELL}\t--- reading file process finished at "{datetime.now()}" ---{NO_COLOR}\n')  

    print(f"{FR_GREEN}\tOriginal Alphabet:{NO_COLOR}\n\t\t{(','.join(ORIG_ALPHAB))}")
    print(f"{FR_GREEN}\tOriginal text:{NO_COLOR}\n\t\t{MY_TEXT}")
    print(f"{FR_GREEN}\tEncrypted text:{NO_COLOR}\n\t\t{ENCRYPTED_TEXT}")
    print(f"{FR_GREEN}\tMax Number of CPU's:{NO_COLOR} {cpu_count()}\n")
    m_alp = '{:,}'.format(len(messy_alphabets)).replace(',','.')    
    print(f'{FR_YELL}\t--- CHECKING "{m_alp} ALPHABETS" BEGAN AT "{datetime.now()}" ---{NO_COLOR}\n')    
    
    # create the manager
    with Manager() as manager:
        # create the shared event
        event = manager.Event()
        
        print(f'\n{FR_YELL}\tFrom Main - With Manager() as manager:{NO_COLOR}\n\t\tevent -> {event}\n', flush=True)

        # create and configure the process pool
        # Note: if you do not put a valid number of CPU's, Pool() assume the maximum of PC 
        with Pool(cpu_count()) as pool:   

            # prepare arguments 
            alphabets = [(messy_alphabets[i],event) for i in range(len(messy_alphabets))]
            print(f'{FR_YELL}\tFrom Main - With Pool({cpu_count()}) as pool:{NO_COLOR}\n\t\tpool -> {pool}\n', flush=True)

            # issue tasks asynchronously
            result = pool.starmap_async(decipher, alphabets)            
            
            result.wait()
            # wait for all tasks to stop            
            print(f'\n\t{FR_RED}=== ALL TASKS STOPED ==={NO_COLOR}\n')

            # elapsed time
            elapsed_time = "{:.2f}".format(time.time()-inicio)
            print(f"\n\t{FR_YELL}================  Elapsed time: {elapsed_time} seconds ================={NO_COLOR}\n\n")

