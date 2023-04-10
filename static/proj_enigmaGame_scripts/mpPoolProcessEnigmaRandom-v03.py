# https://stackoverflow.com/questions/54224989/killing-a-multiprocessing-process-when-condition-is-met

import os, time
from time import sleep
from datetime import datetime
from multiprocessing import Process, Event, cpu_count
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
ORIG_ALPHAB = list(ALPHAB_STR)
ALPHAB = list(ALPHAB_STR)
ALPHAB_15_STR        = 'abcdegilmnoprsu'
ALPHAB_15_TO_ENCRYPT = list('mcspirabdguolen')
ALPHAB_TO_ENCRYPT = list('mcspifrhajkbdguoqletnvwxyz')
TEMP_LIST = ['m', 'c', 's', 'p', 'i', 'f', 'r', 'h', 'a', 'j', 'k', 'b', 'd', 'g', 'u', 'o', 'q', 'l', 'e', 't', 'n', 'v', 'w', 'x', 'y', 'z']
MY_TEXT = 'El murcielago esta hambriento'
ENCRYPTED_TEXT = 'ib dnlsaibmru ietm hmdclaigtu'

# FUNCIONS SECTION

def decipher(alphab1, target, found_event):  
    
    #print(f'\n\t{FR_GREEN}parent process: {os.getppid()}, {FR_YELL}child pid: {os.getpid()} {NO_COLOR} started at "{datetime.now()}"\n') 
    print(f"sub alphab : {alphab1}")
    # rewrite alphab1 with correct position in alphabet of 26
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
    # print(f"----> alphab1_26: {alphab1_26}")  
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
    #print(f"--------> decoded text: {decoded_text}\n")
    if  decoded_text == target:
        print(f"{FR_YELL}\t------ BINGO ------ BINGO ------ BINGO ------ BINGO ------ BINGO ------ BINGO ------\n")
        print(f'\t{FR_GREEN}Parent Process {os.getppid()}, {FR_YELL}in the Child Process "{os.getpid()}"{NO_COLOR} the solution was found !"') 
        print(f"\t\t{FR_YELL}{os.getpid()}{NO_COLOR} Decoded text is correct: {decoded_text}")  
        print(f'\t\t{FR_YELL}{os.getpid()}{NO_COLOR} Alphabet: {(",".join(ALPHAB_STR))}', flush=True)         
        print(f'\t\t{FR_YELL}{os.getpid()}{NO_COLOR} Decoder : {(",".join(alphab1_26))}', flush=True)   
        print(f"\t\t{FR_YELL}{os.getpid()}{NO_COLOR} Encrypted text: {ENCRYPTED_TEXT}")     
        print(f"\n\t\033[2;33;41m-------- STOP PROCESS STARTED --------{NO_COLOR}\n")
        found_event.set() 
    else:
        sleep(0.00001)       

    
#
#  MAIN
#

if __name__ == "__main__":

    os.system('cls')

    text = ""    

    print(f'\n{FR_GREEN}======  "MAIN" ======\n{NO_COLOR}')
    print(f"\nMODEL\n\tpool = [Process(target=decipher, args=(range_, target, found_event))  for range_ in ranges]\n")
    
    print(f"{FR_YELL}Original Alphabet:{NO_COLOR}\n\t{(','.join(ORIG_ALPHAB))}")
    print(f"{FR_YELL}Original text:{NO_COLOR}\n\t{MY_TEXT}\n")
    print(f"{FR_GREEN}Random Messy Alphabet used to encrypt original text:{NO_COLOR}\n\t{(','.join(ALPHAB_TO_ENCRYPT))}")
    print(f"{FR_GREEN}Encrypted text:{NO_COLOR}\n\t{ENCRYPTED_TEXT}\n")

    messy_alphab  = list('basmiunodpglcer')
    #good_alphabet = list('mcspirabdguolen')

    messy_alphabets = []
    #messy_alphabets.append(ALPHAB_15_TO_ENCRYPT)  
    messy_lines = set(open('z-permutFileSorted.txt').readlines())
    for messy_str in messy_lines:
        messy_alphabets.append(list(messy_str))
        #messy_alphabets.append(messy_str)
    messy_alphabets.append(ALPHAB_15_TO_ENCRYPT)  

    """
    for i in range(10):
        messy_alphabets.append(messy_alphab)
    messy_alphabets.append(ALPHAB_15_TO_ENCRYPT)       
    messy_lines = set(open('z-permutFileSorted.txt').readlines())    
    i=0
    for messy_str in messy_lines:
        if i % 10 == 0:
            print(f"messy_str: {messy_str} --- mod {i%10}")
        i += 1
    """


    print("\n-----------------------------------------------------------------------\n")

    #alphabets = [(messy_alphabets[i],event) for i in range(len(messy_alphabets))]    
    alphabets = [(messy_alphabets[i]) for i in range(len(messy_alphabets))]    
    #print(f"alphabets list: {alphabets}\n")
    print(f"{FR_GREEN}alphabets list length: {len(alphabets)}{NO_COLOR}\n")


    target = MY_TEXT.casefold()              # <-- worker finding this value triggers massacre
    found_event = Event()
    
    pool = [Process(target=decipher, args=(alphab, target, found_event))
            for alphab in alphabets]

    print(f"Max Number of CPU's: {cpu_count()}\n")
    #print(f"List of processes: {pool}\n")
    print(f"Number of pool processes: {len(pool)}\n")
    #print("\n-----------------------------------------------------------------------\n")

    pause()
    os.system('cls')
    print(f'\n{FR_GREEN}\t================ "Multiprocess started with pid: {os.getpid()}"" ================\n{NO_COLOR}')
    print(f'{FR_YELL}\n\t--- started "{len(alphabets)}" processes at "{datetime.now()}" ---{NO_COLOR}\n')

    # time
    inicio = time.time()   

    for p in pool:
        p.start()
    
    found_event.wait()              # <- blocks until condition met

    print(f'{FR_YELL}\t--- terminating "{len(pool)}" processes at "{datetime.now()}" ---{NO_COLOR}')     

    for p in pool:
        p.terminate()       

    for p in pool:
        p.join()

    print(f'\n\t{FR_GREEN}All processes joined at "{datetime.now()}"{NO_COLOR}')

    print(text)

    # elapsed time
    elapsed_time = "{:.2f}".format(time.time()-inicio)
    print(f'\n\t{FR_YELL}================ Elapsed time: "{elapsed_time}" ================={NO_COLOR}\n\n')

