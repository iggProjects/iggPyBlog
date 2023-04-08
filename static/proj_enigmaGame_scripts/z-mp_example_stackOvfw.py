# https://stackoverflow.com/questions/54224989/killing-a-multiprocessing-process-when-condition-is-met

import os, time
from datetime import datetime
from multiprocessing import Process, Event, cpu_count

# CONSTANTS
# Colors
NO_COLOR = "\033[00m"
FR_RED   = "\033[91m"
FR_GREEN = "\033[92m"
FR_YELL  = "\033[93m"
FR_BLUE  = "\033[94m"
FR_MAG   = "\033[95m"

def worker(range_, target, found_event):      
    print(f'\n\t{FR_GREEN}pid: {os.getpid()} {NO_COLOR} started at "{datetime.now()}"')
    for x in range_:
        if x == target:
            print(f'\n\t{FR_YELL}--- PID: "{os.getpid()}" FOUND TARGET AT "{datetime.now()}" ---{NO_COLOR}')
            found_event.set()

#
#  MAIN
#

if __name__ == "__main__":

    os.system('cls')
    
    # time
    inicio = time.time()
    print(f'\n{FR_GREEN}======  "Multiprocess started with pid: {os.getpid()}" ======\n{NO_COLOR}')

    print(f"\nmodel\n\tpool = [Process(target=worker, args=(range_, target, found_event))  for range_ in ranges]\n")


    N_WORKERS = 32

    step = int(200e6)
    ranges = [range(x, x + step)            # change `range` to `xrange` for Python 2
              for x in range(0, N_WORKERS * step, step)]
                                            # range(0, 200.000.000), ..., range(800.000.000, 1.000.000.000)]
    #print(f"ranges: {ranges}\n")
    print(f"ranges length: {len(ranges)}\n")

    target = 100000                             # <-- worker finding this value triggers massacre
    #target = int(250e6)                     # <-- worker finding this value triggers massacre
    found_event = Event()
    
    pool = [Process(target=worker, args=(range_, target, found_event))
            for range_ in ranges]

    print(f"Max Number of CPU's: {cpu_count()}\n")
    #print(f"List of processes: {pool}\n")
    print(f"Number of pool processes: {len(pool)}\n")
    print("\n-----------------------------------------------------------------------\n")

    for p in pool:
        p.start() 
    
    print(f'{FR_YELL}\n\t--- started "{len(ranges)}" processes at "{datetime.now()}" ---{NO_COLOR}')
    
    found_event.wait()              # <- blocks until condition met

    numb_proc_finished = 0
    for p in pool:
        numb_proc_finished += 1
        p.terminate()       
    print(f'{FR_YELL}\t--- terminating "{numb_proc_finished}" processes at "{datetime.now()}" ---{NO_COLOR}')     

    for p in pool:
        p.join()

    print(f'\n\t{FR_GREEN}All processes joined at "{datetime.now()}"{NO_COLOR}')

    # elapsed time
    elapsed_time = "{:.2f}".format(time.time()-inicio)
    print(f'\n{FR_YELL}================  Elapsed time: "{elapsed_time}"  ================={NO_COLOR}\n\n')

