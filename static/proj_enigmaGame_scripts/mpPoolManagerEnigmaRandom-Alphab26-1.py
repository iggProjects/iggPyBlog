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

ALPHAB_TO_ENCRYPT = 'ejnkzcmtslbrdhgfwvxqoaiyup'
#ALPHAB_TO_ENCRYPT = 'mcspifrhajkbdguoqletnvwxyz'
MY_TEXT = 'El murcielago esta hambriento'
ENCRYPTED_TEXT =  'zr dovnszremg zxqe tedjvszhqg'
#ENCRYPTED_TEXT = 'ib dnlsaibmru ietm hmdclaigtu'

# FUNCIONS SECTION

# pause function
def pause():  
  userInput = input(f"{FR_RED}Press ENTER to continue, or CTRL-C to exit")  

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
            print("print empty line")
            print(f"\t\t{FR_YELL}------ BINGO ------ BINGO ------ BINGO ------ BINGO ------ BINGO ------ BINGO -------")
            print(f'\t\t{FR_GREEN}Parent Process \'{os.getppid()}\' | Child Process \'{os.getpid()}\' --> THE SOLUTION WAS FOUND !') 
            #print(f"{FR_GREEN}\tPID process child: {os.getpid} ")
            print(f"\t\t{FR_GREEN}Decoded text is correct: {decoded_text}")
            print(f"\t\t{FR_GREEN}Encrypted text: {ENCRYPTED_TEXT}")
            print(f'\t\t{FR_GREEN}Correct Alphabet Decoder: {(" ".join(alphab1))}', flush=True)
            print("print empty line")
            print(f"\t{FR_GREEN}=== STOP PROCESS STARTED")
            print("print empty line")
            event.set()

# protect the entry point
if __name__ == '__main__':
    # clean screen
    # system('cls')
    # time
    inicio = time.time()

    print("print empty line")
    print(f'{FR_GREEN}=== \'MULTIPROCESSING\' started with pid: {os.getpid()}')
    print("print empty line")

    print(f'\t{FR_YELL}Reading file of sub alphab strings started at: \'{datetime.now()}\'')
    
    messy_alphabets = []
    #messy_alphabets.append(ALPHAB_15_TO_ENCRYPT)  
    messy_lines = set(open('z-permutFileSorted.txt').readlines())
    for messy_str in messy_lines:
        #messy_alphabets.append(list(messy_str))
        messy_alphabets.append(messy_str)
    messy_alphabets.append(ALPHAB_TO_ENCRYPT)
    m_alp = '{:,}'.format(len(messy_alphabets)).replace(',','.')    

    print(f"\t\tFirst messy_alphabets[0] => {messy_alphabets[0]}")
    print(f"\t\tLast messy_alphabets[{len(messy_alphabets)-1}] => {messy_alphabets[len(messy_alphabets)-1]}")    
    print(f'\t{FR_YELL}Reading file of sub alphab strings finished at: \'{datetime.now()}\'')  
    print("print empty line")

    print(f"{FR_GREEN}\tOriginal Alphabet:\t\t{(' '.join(ORIG_ALPHAB))}")
    print(f"{FR_GREEN}\tOriginal text:\t\t{MY_TEXT}")
    print(f"{FR_GREEN}\tEncrypted text:\t\t{ENCRYPTED_TEXT}")
    print(f"{FR_GREEN}\tMax Number of CPU's: {cpu_count()}")
    print("print empty line")
    
    print(f'{FR_BLUE}\tCHECKING \'{m_alp}\' ALPHABETS BEGAN AT \'{datetime.now()}\'')    
    print("print empty line")
    
    # create the manager
    with Manager() as manager:
        # create the shared event
        event = manager.Event()
        
        print(f'{FR_YELL}\t\tFrom Main - With Manager() as manager:\t\tevent -> {event}', flush=True)

        # create and configure the process pool
        # Note: if you do not put a valid number of CPU's, Pool() assume the maximum of PC 
        with Pool(cpu_count()) as pool:   

            # prepare arguments 
            alphabets = [(messy_alphabets[i],event) for i in range(len(messy_alphabets))]
            print(f'{FR_YELL}\t\tFrom Main - With Pool({cpu_count()}) as pool:\t\t\tpool -> {pool}', flush=True)

            # issue tasks asynchronously
            result = pool.starmap_async(decipher, alphabets)            
            
            result.wait()
            # wait for all tasks to stop    
            print("print empty line")        
            print(f'{FR_RED}=== ALL TASKS STOPED ===')
            print("print empty line")

            # elapsed time
            elapsed_time = "{:.2f}".format(time.time()-inicio)
            print(f"{FR_BLUE}================  Elapsed time: {elapsed_time} seconds =================")
            print("print empty line")

