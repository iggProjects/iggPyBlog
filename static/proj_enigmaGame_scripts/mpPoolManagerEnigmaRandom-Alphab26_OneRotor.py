# https://superfastpython.com/multiprocessing-pool-stop-all-tasks/
# SuperFastPython.com
# example of safely stopping all tasks in the process pool

"""  
    
    THIS SCRIPT IS FOR .............

"""

# IMPORT SECTION

try:   # Import My Own Functions from include dir 
    import sys, traceback, string, time
    import numpy as np   
    from os.path import dirname, realpath
    from os import scandir
    from random import randrange
    from datetime import datetime
    from multiprocessing import Event
    from multiprocessing import Manager, cpu_count
    from multiprocessing.pool import Pool


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

def decipher(alphab1, event):

    if event.is_set():
        return
    else:
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

        if MY_TEXT.casefold() == decoded_text:
            print()
            print(f"\t{FR_YELL}------ BINGO ------ BINGO ------ BINGO ------ BINGO ------ BINGO ------ BINGO -------")
            print()
            print(f'\t{FR_GREEN}Parent Process "{os.getppid()}" | Child Process "{os.getpid()}" --> THE SOLUTION WAS FOUND !{NO_COLOR}') 
            print()
            print(f"\t\t{FR_RED}{ENCRYPTED_TEXT} ==> {decoded_text} {NO_COLOR}")            
            print(f'\t\t{FR_GREEN}Correct Alphabet Decoder: {NO_COLOR}{(" ".join(alphab1))}', flush=True)            
            print()            
            print(f"\t\033[2;33;41m-------- STOP PROCESS STARTED --------{NO_COLOR}")
            print()
            event.set()

#
# ---------- MAIN ----------
#

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

        print(f'{FR_YELL}\t--- reading file of sub alphab str started at "{datetime.datetime.now()}" ---{NO_COLOR}')

        messy_alphabets = []    
        messy_lines = set(open("static/proj_enigmaGame_scripts/temp/z-permutFileSorted.txt").readlines())
        for messy_str in messy_lines:
            messy_alphabets.append(messy_str)
        messy_alphabets.append(ALPHAB_TO_ENCRYPT)
        m_alp = '{:,}'.format(len(messy_alphabets)).replace(',','.')    

        print(f"\t\tFirst messy_alphabets[0] ===> {messy_alphabets[0]}")
        print(f'{FR_YELL}\t--- reading file process finished at "{datetime.datetime.now()}" ---{NO_COLOR}')  
        print(f"\t\tLast messy_alphabets[{len(messy_alphabets)-1}] ===> {messy_alphabets[len(messy_alphabets)-1]}")
        print()
        print(f'{FR_YELL}\t--- CHECKING "{m_alp} ALPHABETS" BEGAN AT "{datetime.datetime.now()}" ---{NO_COLOR}')  
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

                # case not solution found
                if not event.is_set():
                    print(f"{FR_RED}\t===================> SOLUTION NOT FOUND ! <==================={NO_COLOR}")
                    print()

                # elapsed time
                elapsed_time = "{:.2f}".format(time.time()-inicio)
                print(f"\t{FR_YELL}================  Elapsed time: {elapsed_time} seconds ================={NO_COLOR}")
                print()
                print()

    except Exception as Argument:
        error_msg = "ERROR IN <" + my_script_name + ">. SEE server_messages.txt !"
        write_log_file("my_messages.txt",error_msg)
        write_traceback_info_1(Argument,traceback,my_script_name)
        pause()     
    
else:
    # something wrong
    print(frRED("---- new thread ----"))
