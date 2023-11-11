# https://superfastpython.com/multiprocessing-pool-stop-all-tasks/
# SuperFastPython.com
# example of safely stopping all tasks in the process pool

"""  
    
    THIS SCRIPT IS FOR .............


"""
# IMPORT SECTION

try:   # Import My Own Functions from include dir 
    import sys, traceback, time, string
    import numpy as np   
    from time import sleep
    from datetime import datetime
    from multiprocessing import Event
    from multiprocessing import Manager, cpu_count
    from multiprocessing.pool import Pool
    from random import randrange

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


#
# ---------- MAIN ----------
#

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
  userInput = input(f"{FR_RED}Press ENTER to continue, or CTRL-C to exit{NO_COLOR}\n")  

def decipher(alphab1, event):

    #print(f"decipher: alphab1-> {alphab1}")

    if event.is_set():
        return
    else:  
        #print(f"decipher: alphab1-> {alphab1}")
                
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
            print(f'\t\t{FR_GREEN}Correct Alphabet Decoder: {NO_COLOR}{(",".join(alphab1))}', flush=True)
            print(f"\n\t{FR_YELL}-------------------------------------------------------------------------------------")
            print(f"\n\t\033[2;33;41m-------- STOP PROCESS STARTED --------{NO_COLOR}\n")
            event.set()

# protect the entry point
if __name__ == '__main__':

    try:

        clear_console_screen()

        my_script = __file__.split('\\')
        my_script_name = my_script[len(my_script)-1]
        print()
        write_log_file("my_messages.txt","IN '" + my_script_name + "'")
        print()

        print(f"{FR_GREEN}---------- MAIN ----------{NO_COLOR}")
        print()
        inicio = time.time()

        print(f'\n{FR_GREEN}\t================ "Multiprocess started with pid: {os.getpid()}"" ================\n{NO_COLOR}')
        print(f'{FR_YELL}\n\t--- reading file of sub alphab str started at "{datetime.datetime.now()}" ---{NO_COLOR}\n')

        messy_alphabets = []
        #messy_alphabets.append(ALPHAB_15_TO_ENCRYPT)          
        messy_lines = set(open(basedir + "/static/proj_enigmaGame_scripts/temp/z-permutFileSorted.txt").readlines())
        for messy_str in messy_lines:
            #messy_alphabets.append(list(messy_str))
            messy_alphabets.append(messy_str)
        messy_alphabets.append(ALPHAB_TO_ENCRYPT)
        m_alp = '{:,}'.format(len(messy_alphabets)).replace(',','.')    

        print(f"\tFirst messy_alphabets[0] ===> {messy_alphabets[0]}")
        print(f"\tLast messy_alphabets[{len(messy_alphabets)-1}] ===> {messy_alphabets[len(messy_alphabets)-1]}")
        
        print(f'{FR_YELL}\t--- reading file process finished at "{datetime.datetime.now()}" ---{NO_COLOR}\n')  

        print(f"{FR_GREEN}\tOriginal Alphabet:{NO_COLOR}\n\t\t{(','.join(ORIG_ALPHAB))}")
        print(f"{FR_GREEN}\tOriginal text:{NO_COLOR}\n\t\t{MY_TEXT}")
        print(f"{FR_GREEN}\tEncrypted text:{NO_COLOR}\n\t\t{ENCRYPTED_TEXT}")
        print(f"{FR_GREEN}\tMax Number of CPU's:{NO_COLOR} {cpu_count()}\n")
        
        print(f'{FR_YELL}\t--- CHECKING "{m_alp} ALPHABETS" BEGAN AT "{datetime.datetime.now()}" ---{NO_COLOR}\n')    
        
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
    print(frRED("---- new thread ----"))
