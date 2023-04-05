# https://superfastpython.com/multiprocessing-pool-stop-all-tasks/
# SuperFastPython.com
# example of safely stopping all tasks in the process pool

from time import sleep
from multiprocessing import Event
from multiprocessing import Manager
from multiprocessing.pool import Pool
from os import system

NO_COLOR = "\033[00m"
FR_RED   = "\033[91m"
FR_GREEN = "\033[92m"
FR_YELL  = "\033[93m"
FR_BLUE  = "\033[94m"
FR_MAG   = "\033[95m"
 
# task executed in a worker process
def task(identifier, event):    
    print(f'{FR_GREEN}From Task:{NO_COLOR} Task {identifier} running', flush=True)

    # safely stop the issued tasks
    """
    if identifier == 3:
        print(f"\n\t{FR_RED}Event call with identifier = {identifier}")
        print(f'\tSafely stopping all tasks{NO_COLOR}\n')
        event.set()
    """    
    # report all done
    print(f'\t\tTask {identifier} Done', flush=True)
    #print(f'\t\tTask {identifier} Stopped', flush=True)
 
# protect the entry point
if __name__ == '__main__':
    # clean screen
    system('cls')
    # create the manager
    with Manager() as manager:
        # create the shared event
        event = manager.Event()
        # create and configure the process pool
        with Pool() as pool:
            # prepare arguments
            items = [(i,event) for i in range(10)]
            print()
            for item in items:
                print(f'{FR_YELL}From Main:{NO_COLOR} Task {item} running', flush=True)            
            # issue tasks asynchronously
            print()
            result = pool.starmap_async(task, items)
            # wait a moment
            sleep(1)
            print()
            """
            # safely stop the issued tasks
            print(f'{FR_MAG}Safely stopping all tasks{NO_COLOR}\n')
            event.set()
            # wait for all tasks to stop
            result.wait()
            """            
            print(f'\n{FR_RED}=== ALL TASKS STOPED ==={NO_COLOR}\n')