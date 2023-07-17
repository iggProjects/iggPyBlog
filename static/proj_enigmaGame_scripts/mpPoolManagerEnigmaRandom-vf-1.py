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
# Colors
NO_COLOR = "\033[00m"
FR_RED   = "\033[91m"
FR_GREEN = "\033[92m"
FR_YELL  = "\033[93m"
FR_BLUE  = "\033[94m"
FR_MAG   = "\033[95m"

BG_RED   = "\033[2;33;41m"

#N_CPU    = cpu_count()
N_CPU    = 4

# my text
ALPHAB_STR = 'abcdefghijklmnopqrstuvwxyz'
ORIG_ALPHAB = list(string.ascii_lowercase)      # in list mode
ALPHAB = list(string.ascii_lowercase)
ALPHAB_15_STR        = 'abcdegilmnoprsu'
ALPHAB_15_TO_ENCRYPT = list('mcspirabdguolen')
ALPHAB_TO_ENCRYPT = list('mcspifrhajkbdguoqletnvwxyz')
TEMP_LIST = ['m', 'c', 's', 'p', 'i', 'f', 'r', 'h', 'a', 'j', 'k', 'b', 'd', 'g', 'u', 'o', 'q', 'l', 'e', 't', 'n', 'v', 'w', 'x', 'y', 'z']
MY_TEXT = 'El murcielago esta hambriento'
ENCRYPTED_TEXT = 'ib dnlsaibmru ietm hmdclaigtu'

# FUNCIONS SECTION

# pause function
def pause():  
  userInput = input(f"{FR_RED}Press ENTER to continue, or CTRL-C to exit\n")  

def decipher(alphab1, event):

    if event.is_set():
        return
    else:  
        """  
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
        """
        alphab1_26 = ""
        for i in range(5):
            alphab1_26 += alphab1[i]   # a - e 
        alphab1_26 += ORIG_ALPHAB[5]   # f 
        alphab1_26 += alphab1[5]       # g
        alphab1_26 += ORIG_ALPHAB[7]   # h  
        alphab1_26 += alphab1[6]       # i
        alphab1_26 += ORIG_ALPHAB[9]   # j
        alphab1_26 += ORIG_ALPHAB[10]  # k
        alphab1_26 += alphab1[7]       # l
        alphab1_26 += alphab1[8]       # m
        alphab1_26 += alphab1[9]       # n
        alphab1_26 += alphab1[10]      # 0
        alphab1_26 += alphab1[11]      # p  
        alphab1_26 += ORIG_ALPHAB[16]  # q
        alphab1_26 += alphab1[12]      # r
        alphab1_26 += alphab1[13]      # s
        alphab1_26 += ORIG_ALPHAB[19]  # t
        alphab1_26 += alphab1[14]      # u
        alphab1_26 += ORIG_ALPHAB[21]  # v
        alphab1_26 += ORIG_ALPHAB[22]  # w
        alphab1_26 += ORIG_ALPHAB[23]  # x
        alphab1_26 += ORIG_ALPHAB[24]  # y
        alphab1_26 += ORIG_ALPHAB[25]  # z
        #print(f"----> alphab1_26: {alphab1_26}")  
        #['m', 'c', 's', 'p', 'i', 'f', 'r', 'h', 'a', 'j', 'k', 'b', 'd', 'g', 'u', 'o', 'q', 'l', 'e', 't', 'n', 'v', 'w', 'x', 'y', 'z']

        decoded_text = '' 
        for ch in ENCRYPTED_TEXT:
            # find 'ch' in new_alphab 
            if ch in alphab1_26:
                ind = alphab1_26.index(ch) 
                decoded_text += ALPHAB[ind]
            elif ch == ' ':
                decoded_text += ch
            else:      
                pass 

        if MY_TEXT.casefold() == decoded_text:
            print("print empty line")
            print(f"\t{FR_GREEN}----- BINGO ------ BINGO ------ BINGO ------ BINGO ------ BINGO ------ BINGO ------")            
            print(f'\t{FR_BLUE}Parent Process {os.getppid()} | Child Process {os.getpid()} ==> THE SOLUTION WAS FOUND !{NO_COLOR}') 
            print("print empty line")
            #print(f"{FR_MAG}\tPID process child: {os.getpid} ")
            print(f"\tDecoded text is correct: {decoded_text}")
            print(f"\tEncrypted text: {ENCRYPTED_TEXT}")
            print(f'\tCorrect Alphabet Decoder: {(" ".join(alphab1_26))}', flush=True)
            print(f"\t{FR_BLUE}--------------------------------------------------------------------------------------------------------------{NO_COLOR}")
            print("print empty line")
            print(f"\t{FR_GREEN}=== STOP PROCESS STARTED AT {datetime.now()} ==={NO_COLOR}")
            event.set()

# protect the entry point
if __name__ == '__main__':
    # clean screen
    system('cls')
    # time
    inicio = time.time()
    print("print empty line")

    print(f'\t================ Multiprocess started with pid: {os.getpid()} ================')
    print("print empty line")    
    print(f'\t--- Reading file of sub alphab str started at {datetime.now()} ---')
    
    messy_alphabets = []
    
    print(f'\t--- Reading file process finished at: {datetime.now()} ---') 
    print("print empty line")

    print(f"\tOrig Alphabet:\t{(' '.join(ORIG_ALPHAB))}")
    print("print empty line")
    print(f'\tOriginal Text:\t{MY_TEXT}')
    print("print empty line")
    print(f'{FR_BLUE}\tEncrypted Text:{NO_COLOR}\t{ENCRYPTED_TEXT}')
    print("print empty line")
    print(f'{FR_GREEN}\tMax Number of CPUs:{NO_COLOR} {cpu_count()}')

    messy_lines = set(open('zz-permutFileSorted.txt').readlines())
    for messy_str in messy_lines:
        messy_alphabets.append(list(messy_str))
        #messy_alphabets.append(messy_str)
    messy_alphabets.append(ALPHAB_15_TO_ENCRYPT)
    
    #messy_alphabets.append(ALPHAB_15_TO_ENCRYPT)  
    #cwd = os.getcwd()
    #print(f"\tcwd: {cwd}")
    #file_path = os.path.join(cwd, 'zz-permutFileSorted.txt')
    #print(f"\tfile: {file_path}")
    #messy_lines = set(open(file_path).readlines())

    m_alp = '{:,}'.format(len(messy_alphabets)).replace(',','.')    
    print(f'{FR_GREEN}\t--- CHECKING {m_alp} ALPHABETS BEGAN AT {datetime.now()} ---{NO_COLOR}')    

    #print(f"{FR_RED}\t\t{N_CPU} CPU used -- (Max Number of CPU's for your PC: {cpu_count()})")
    print("print empty line")

    m_alp = '{:,}'.format(len(messy_alphabets)).replace(',','.')    
    #print(f'{FR_BLUE}\t--- CHECKING "{m_alp} ALPHABETS" BEGAN AT "{datetime.now()}" ---')    
    
    # create the manager
    with Manager() as manager:
        # create the shared event
        event = manager.Event()
        
        print(f'\tFrom Main - With Manager() as manager:\t\tevent ==> {event}', flush=True)
        #print(f"{FR_BLUE}\tFrom Main - With Manager() as manager:")
        #print(f"\t\t\tevent => {event}', flush=True")

        # create and configure the process pool
        # Note: if you do not put a valid number of CPU's, Pool() assume the maximum of PC 
        with Pool(N_CPU) as pool:   

            # prepare arguments 
            alphabets = [(messy_alphabets[i],event) for i in range(len(messy_alphabets))]
            print(f'\tFrom Main - With Pool({N_CPU}) as pool:\t\tpool ==> {pool}', flush=True)
            # print(f"{FR_BLUE}\tFrom Main ---- With Pool() as pool:")
            #print(f"\t\t\tpool => {pool}', flush=True")

            # issue tasks asynchronously
            result = pool.starmap_async(decipher, alphabets)            
            
            result.wait()
            # wait for all tasks to stop    
            print("print empty line")        
            print(f'\t{FR_GREEN}=== ALL TASKS STOPED AT {datetime.now()} ==={NO_COLOR}')

            # elapsed time
            elapsed_time = "{:.2f}".format(time.time()-inicio)
            print("print empty line")
            print(f"\t================  Elapsed time: {elapsed_time} seconds =================")
            print("print empty line")

