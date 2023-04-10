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
ORIG_ALPHAB = list(string.ascii_lowercase)      # in list mode
ALPHAB = list(string.ascii_lowercase)
MY_TEXT = 'abcdef ghijk lmnopq KAIXO TEACHER'

ALPHAB_TO_ENCRYPT  = ['j', 'h', 'm', 'a', 'r', 'e', 'd', 'i', 'q', 'o', 't', 'c', 'g', 'f', 's', 'p', 'u', 'n', 'z', 'v', 'k', 'w', 'y', 'l', 'x', 'b']     
ENCRYPTED_TEXT = 'jhmare diqot cgfspu tjqls vrjmirn'

# FUNCIONS SECTION

def decipher(alphab1, target, found_event):  
    print(f"sub alphab list: {alphab1}")
    #print(f'\n\t{FR_GREEN}parent process: {os.getppid()}, {FR_YELL}child pid: {os.getpid()} {NO_COLOR} started at "{datetime.now()}"\n') 

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
        """
        text = "\t{FR_YELL}------ BINGO ------ BINGO ------ BINGO ------ BINGO ------ BINGO ------ BINGO ------\n"    
        text += "\t{FR_GREEN}In the PID process \"{os.getpid()}\" the solution was found !{NO_COLOR}\n"
        text += "\t{FR_GREEN}Decoded text is correct: {NO_COLOR}{decoded_text}\n"
        text += "\t{FR_GREEN}Correct Alphabet Decoder: {NO_COLOR}{(','.join(alphab1))}'\n"    
        text += "\t{FR_GREEN}Encrypted text: {NO_COLOR}{ENCRYPTED_TEXT}\n"    
        """        
        print(f"{FR_YELL}\t------ BINGO ------ BINGO ------ BINGO ------ BINGO ------ BINGO ------ BINGO ------\n")
        print(f'\t{FR_GREEN}Parent Process {os.getppid()}, {FR_YELL}in the Child Process "{os.getpid()}"{NO_COLOR} the solution was found !"') 
        print(f"\t\t{FR_YELL}{os.getpid()}{NO_COLOR} Decoded text is correct: {decoded_text}")        
        print(f'\t\t{FR_YELL}{os.getpid()}{NO_COLOR} Correct Alphabet Decoder: {(",".join(alphab1))}', flush=True)   
        print(f"\t\t{FR_YELL}{os.getpid()}{NO_COLOR} Encrypted text: {ENCRYPTED_TEXT}")     
        print(f"\n\t\033[2;33;41m-------- STOP PROCESS STARTED --------{NO_COLOR}\n")
        found_event.set() 

        
    else: 
        sleep(0.0001)       
        #print(f'{FR_GREEN}\n\tDecode text failed: {NO_COLOR}{decoded_text}')

    
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

    messy_alphab1 = ['w', 'n', 'y', 'x', 'o', 'v', 'r', 'l', 'u', 'z', 'q', 'a', 'b', 'm', 'd', 'h', 'f', 'c', 's', 't', 'k', 'e', 'g', 'i', 'p', 'j']
    messy_alphab2 = ['n', 'w', 'y', 'x', 'o', 'v', 'r', 'l', 'u', 'z', 'q', 'a', 'b', 'm', 'd', 'h', 'f', 'c', 's', 't', 'k', 'e', 'g', 'i', 'p', 'j']

    messy_alphabets = []
    messy_alphabets.append(ALPHAB_TO_ENCRYPT)   
    for i in range(100):
        messy_alphabets.append(messy_alphab1)
    #messy_alphabets.append(ALPHAB_TO_ENCRYPT)   


    print("\n-----------------------------------------------------------------------\n")

    #alphabets = [(messy_alphabets[i],event) for i in range(len(messy_alphabets))]    
    alphabets = [(messy_alphabets[i]) for i in range(len(messy_alphabets))]    
    #print(f"alphabets list: {alphabets}\n")
    print(f"{FR_GREEN}alphabets list length: {len(alphabets)}{NO_COLOR}\n")

    target = MY_TEXT.casefold()              # <-- worker finding this value triggers massacre
    #target = int(250e6)                     # <-- worker finding this value triggers massacre
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

    # time
    inicio = time.time()   

    for p in pool:
        p.start() 
    
    print(f'{FR_YELL}\n\t--- started "{len(alphabets)}" processes at "{datetime.now()}" ---{NO_COLOR}\n')
    
    found_event.wait()              # <- blocks until condition met

    numb_proc_finished = 0
    for p in pool:
        numb_proc_finished += 1
        p.terminate()       
    print(f'{FR_YELL}\t--- terminating "{numb_proc_finished}" processes at "{datetime.now()}" ---{NO_COLOR}')     

    for p in pool:
        p.join()

    print(f'\n\t{FR_GREEN}All processes joined at "{datetime.now()}"{NO_COLOR}')

    print(text)

    # elapsed time
    elapsed_time = "{:.2f}".format(time.time()-inicio)
    print(f'\n\t{FR_YELL}================ Elapsed time: "{elapsed_time}" ================={NO_COLOR}\n\n')

