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
FR_MAG   = "\033[91m"
FR_GREEN = "\033[92m"
FR_MAG   = "\033[93m"
FR_BLUE  = "\033[94m"
FR_MAG   = "\033[95m"

# my message
ALPHAB_STR = 'abcdefghijklmnopqrstuvwxyz'
ORIG_ALPHAB = list(string.ascii_lowercase)      # in list mode
ALPHAB = list(string.ascii_lowercase)

ALPHAB_TO_ENCRYPT = 'yzxuqrbapsfwjdtgiomhvelckn'
alphab = list(ALPHAB_TO_ENCRYPT)
#ALPHAB_TO_ENCRYPT = 'mcspifrhajkbdguoqletnvwxyz'
MY_MSG = 'el murcielago no come murcielagos'
ENCRYPTED_MSG =  'qf fodcxcuolu zz tnld vzcajadzbdi'
#ENCRYPTED_TEXT = 'ib dnlsaibmru ietm hmdclaigtu'

# FUNCIONS SECTION

# pause function
def pause():  
  userInput = input(f"{FR_MAG}Press ENTER to continue, or CTRL-C to exit")  

def alphab_jump(alph,k):
    # jump value -k to rotate list    
    return alph[-k:] + alph[:-k]

def decipher(alphab1, event):

    if event.is_set():
        return
    else: 
        
        # list of all derived alphabets with rotation by 1 to right position
        alphab_list = []  
        for jump in range(27):
            alphab_list.append(alphab_jump(alphab1,jump))

        # Process with alphab_list (rotor effect)
        counter = 0
        decoded_msg = ""
        for ch in ENCRYPTED_MSG:
            if ch == ' ':
                decoded_msg = decoded_msg + ' '
            else:
                if counter < 10:
                    counter_2f = '0'+ str(counter)
                else:
                    counter_2f = counter    
                if alphab_list[counter % 26].index(ch) < 10:
                    index_2f = '0' + str(alphab_list[counter % 26].index(ch))  
                else:
                    index_2f = "{:2}".format(alphab_list[counter % 26].index(ch))  

                #print(f"ch {counter_2f}: {ch} index: {index_2f} | {' '.join(alphab_list[counter % 26])} | orig alphab: {ORIG_ALPHAB[alphab_list[counter % 26].index(ch)]}")
                decoded_msg = decoded_msg + ORIG_ALPHAB[alphab_list[counter % 26].index(ch)]
                counter=counter+1
           
        if MY_MSG.casefold() == decoded_msg:
            print()
            print(f"\t\t{FR_MAG}------ BINGO ------ BINGO ------ BINGO ------ BINGO ------ BINGO ------ BINGO -------")
            print(f'\t\t{FR_GREEN}Parent Process \'{os.getppid()}\' | Child Process \'{os.getpid()}\' --> THE SOLUTION WAS FOUND !') 
            #print(f"{FR_GREEN}\tPID process child: {os.getpid} ")
            print(f"\t\t{FR_GREEN}Decoded message is correct: {decoded_msg}")
            print(f"\t\t{FR_GREEN}Encrypted message: {ENCRYPTED_MSG}")
            print(f'\t\t{FR_GREEN}Correct Alphabet Decoder: {(" ".join(alphab1))}', flush=True)
            print()
            print(f"\t{FR_GREEN}=== STOP PROCESS STARTED")
            print()
            event.set()


# protect the entry point
if __name__ == '__main__':
    # clean screen
    # system('cls')
    # time
    inicio = time.time()

    print()
    print(f'{FR_GREEN}=== \'MULTIPROCESSING\' started with pid: {os.getpid()}')
    print()

    print(f'\t{FR_MAG}Reading file of sub alphab strings started at: \'{datetime.now()}\'')
    
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
    print(f'\t{FR_MAG}Reading file of sub alphab strings finished at: \'{datetime.now()}\'')  
    print()

    print(f"{FR_GREEN}\tOriginal Alphabet:\t\t{(' '.join(ORIG_ALPHAB))}")
    print(f"{FR_GREEN}\tOriginal message:\t\t{MY_MSG}")
    print(f"{FR_GREEN}\tEncrypted message:\t\t{ENCRYPTED_MSG}")
    print(f"{FR_GREEN}\tMax Number of CPU's: {cpu_count()}")
    print()
    
    print(f'{FR_BLUE}\tCHECKING \'{m_alp}\' ALPHABETS BEGAN AT \'{datetime.now()}\'')    
    print()
    
    # create the manager
    with Manager() as manager:
        # create the shared event
        event = manager.Event()
        
        print(f'{FR_MAG}\t\tFrom Main - With Manager() as manager:\t\tevent -> {event}', flush=True)

        # create and configure the process pool
        # Note: if you do not put a valid number of CPU's, Pool() assume the maximum of PC 
        with Pool(cpu_count()) as pool:   

            # prepare arguments 
            alphabets = [(messy_alphabets[i],event) for i in range(len(messy_alphabets))]
            print(f'{FR_MAG}\t\tFrom Main - With Pool({cpu_count()}) as pool:\t\t\tpool -> {pool}', flush=True)

            # issue tasks asynchronously
            result = pool.starmap_async(decipher, alphabets)            
            
            result.wait()
            # wait for all tasks to stop    
            print()        
            print(f'{FR_MAG}=== ALL TASKS STOPED ===')
            print()

            # elapsed time
            elapsed_time = "{:.2f}".format(time.time()-inicio)
            print(f"{FR_BLUE}================  Elapsed time: {elapsed_time} seconds =================")
            print()

