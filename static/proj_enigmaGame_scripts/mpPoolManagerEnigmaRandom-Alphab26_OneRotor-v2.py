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


ALPHAB_TO_ENCRYPT = 'yzxuqrbapsfwjdtgiomhvelckn'
MY_TEXT = 'el murcielago no come murcielagos'
ENCRYPTED_TEXT =  'qf fodcxcuolu zz tnld vzcajadzbdi'

"""
ALPHAB_TO_ENCRYPT = 'ejnkzcmtslbrdhgfwvxqoaiyup'
MY_TEXT = 'El murcielago esta hambriento'
ENCRYPTED_TEXT =  'zr dovnszremg zxqe tedjvszhqg'
"""
# FUNCIONS SECTION

# pause function
def pause():  
  userInput = input(f"{FR_RED}Press ENTER to continue, or CTRL-C to exit{NO_COLOR}\n")  

def decipher(alphab1, event):

    if event.is_set():
        return
    else:

        #print(f"\t\tdecipher: alphab1-> {alphab1}")
        alphab1_list = list(alphab1)  
        
        decoded_text = '' 
        counter=0        
        for ch in ENCRYPTED_TEXT:
            if ch == ' ':
                decoded_text = decoded_text + ch
            else:
                ind = (alphab1_list.index(ch) + counter) % 26
                decoded_text = decoded_text + ALPHAB[ind]
                counter=counter+1

        #print(f"\t\t\talphab: {alphab1}, decode text: {decoded_text}")
        #print()
        

        if MY_TEXT.casefold() == decoded_text:
            print(f"\t{FR_YELL}------ BINGO ------ BINGO ------ BINGO ------ BINGO ------ BINGO ------ BINGO -------")
            print(f'\t{FR_GREEN}Parent Process "{os.getppid()}" | Child Process "{os.getpid()}" --> THE SOLUTION WAS FOUND !{NO_COLOR}') 
            #print(f"{FR_GREEN}\tPID process child: {os.getpid} {NO_COLOR}")
            print(f"\t\t{FR_GREEN}Decoded text is correct: {NO_COLOR}{decoded_text}")
            print(f"\t\t{FR_GREEN}Encrypted text: {NO_COLOR}{ENCRYPTED_TEXT}")
            print(f'\t\t{FR_GREEN}Correct Alphabet Decoder: {NO_COLOR}{(",".join(alphab1))}', flush=True)
            print(f"\t{FR_YELL}-------------------------------------------------------------------------------------")
            print(f"\t\033[2;33;41m-------- STOP PROCESS STARTED --------{NO_COLOR}")
            print()
            event.set()

# protect the entry point
if __name__ == '__main__':
    # clean screen
    system('cls')
    # time
    inicio = time.time()

    print()
    print(f'{FR_GREEN}\t================ "Multiprocess started with pid: {os.getpid()}"" ================{NO_COLOR}')
    print()

    print(f"{FR_GREEN}\tOriginal Alphabet:{NO_COLOR}\t{(','.join(ORIG_ALPHAB))}")    
    print(f"{FR_GREEN}\tOriginal text:{NO_COLOR}\t\t{MY_TEXT}")
    print(f"{FR_GREEN}\tEncrypted text:{NO_COLOR}\t\t{ENCRYPTED_TEXT}")
    print(f"{FR_GREEN}\tMax Number of CPU's:{NO_COLOR}\t{cpu_count()}")
    print()

    print(f'{FR_YELL}\t--- reading file of sub alphab str started at "{datetime.now()}" ---{NO_COLOR}')

    messy_alphabets = []    
    messy_lines = set(open('z-permutFileSorted.txt').readlines())
    for messy_str in messy_lines:
        messy_alphabets.append(messy_str)
    messy_alphabets.append(ALPHAB_TO_ENCRYPT)
    m_alp = '{:,}'.format(len(messy_alphabets)).replace(',','.')    

    print(f"\t\tFirst messy_alphabets[0] ===> {messy_alphabets[0]}")
    print(f'{FR_YELL}\t--- reading file process finished at "{datetime.now()}" ---{NO_COLOR}')  
    print(f"\t\tLast messy_alphabets[{len(messy_alphabets)-1}] ===> {messy_alphabets[len(messy_alphabets)-1]}")
    print()
    print(f'{FR_YELL}\t--- CHECKING "{m_alp} ALPHABETS" BEGAN AT "{datetime.now()}" ---{NO_COLOR}')  
    print()  
    
    # create the manager
    with Manager() as manager:
        # create the shared event
        event = manager.Event()
        
        print(f'{FR_YELL}\tFrom Main - With Manager() as manager:{NO_COLOR}', flush=True)
        print(f'\t\tevent -> {event}', flush=True)
        print()
        
        # create and configure the process pool
        # Note: if you do not put a valid number of CPU's, Pool() assume the maximum of PC 
        with Pool(cpu_count()) as pool:   

            # prepare arguments 
            alphabets = [(messy_alphabets[i],event) for i in range(len(messy_alphabets))]
            print(f'{FR_YELL}\t\tFrom Main - With Pool({cpu_count()}) as pool:{NO_COLOR}', flush=True)
            print(f'\t\t\tpool -> {pool}', flush=True)
            print()

            # issue tasks asynchronously
            result = pool.starmap_async(decipher, alphabets)            
            
            # wait for all tasks to stop  
            result.wait()
            print()           
            print(f'\t{FR_MAG}=== ALL TASKS STOPED ==={NO_COLOR}')
            print()
            """
            # case not solution found
            if not event.is_set():
                print(f"{FR_RED}\t===================> SOLUTION NOT FOUND ! <==================={NO_COLOR}")
                print()
            """

            # elapsed time
            elapsed_time = "{:.2f}".format(time.time()-inicio)
            print(f"\t{FR_YELL}================  Elapsed time: {elapsed_time} seconds ================={NO_COLOR}")
            print()
            print()

