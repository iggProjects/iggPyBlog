# https://superfastpython.com/multiprocessing-pool-stop-all-tasks/
# SuperFastPython.com
# example of safely stopping all tasks in the process pool

from time import sleep
from multiprocessing import Event
from multiprocessing import Manager
from multiprocessing.pool import Pool
from os import system
from random import randrange

NO_COLOR = "\033[00m"
FR_RED   = "\033[91m"
FR_GREEN = "\033[92m"
FR_YELL  = "\033[93m"
FR_BLUE  = "\033[94m"
FR_MAG   = "\033[95m"
 
# task executed in a worker process
def task(identifier, event):    
    print(f'From Task: {FR_GREEN}Task {identifier} running{NO_COLOR}', flush=True)   
    while not event.is_set():
        number = randrange(150)
        print(f"\t{identifier} -- {number}")
        if number == 22:
            print(f'{FR_MAG}\t==== From Task {identifier}, number {number} call event.set() process{NO_COLOR}', flush=True)
            sleep(1)
            #print(f'\t\n==== From Task: {FR_GREEN}Task {identifier} call event.set() ====\n{NO_COLOR}', flush=True)
            # safely stop the issued tasks
            print(f'{FR_MAG}\tTask {identifier} stopping...{NO_COLOR}', flush=True)
            print(f'\t\tTask {identifier} Stopped', flush=True)
            event.set()
            break

# protect the entry point
if __name__ == '__main__':
    # clean screen
    system('cls')
    # create the manager
    with Manager() as manager:
        # create the shared event
        event = manager.Event()
        print(f'\n{FR_YELL}From Main - With Manager() as manager:{NO_COLOR}\n\tevent -> {event}\n', flush=True)

        # create and configure the process pool
        # Note: if you do not put a valid number of CPU's, Pool() assume the maximum of PC 
        with Pool() as pool:   

            # prepare arguments
            items = [(i,event) for i in range(8)]
            print(f'{FR_YELL}From Main - With Pool() as pool:{NO_COLOR}\n\tpool -> {pool}\n', flush=True)
            for item in items:
                print(f'{FR_YELL}From Main{NO_COLOR}: Task {item} running', flush=True)    
            print()

            # issue tasks asynchronously
            result = pool.starmap_async(task, items)

            # safely stop the issued tasks
            #if event.is_set():
            sleep(2)
            print(f'\n{FR_MAG}Safely stopping all tasks{NO_COLOR}\n')
            #event.set()
            
            # wait for all tasks to stop            
            print(f'\n{FR_RED}=== ALL TASKS STOPED ==={NO_COLOR}\n')
            result.wait()
                    
