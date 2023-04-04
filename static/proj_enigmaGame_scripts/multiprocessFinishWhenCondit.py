# script example with terminating all processes

import random
import multiprocessing
import sys
import time
from os import  system

NO_COLOR = "\033[00m"
FR_RED   = "\033[91m"
FR_GREEN = "\033[92m"
FR_YELL  = "\033[93m"
FR_BLUE  = "\033[94m"
FR_MAG   = "\033[95m"

def generate_number():
    return random.choice(range(20))

def f(event):    
    while True:
        x = generate_number()        
        if x != 9:
            print(f"Value is {x}")
        else:
            print(f"{FR_YELL}Value is {x} and I Got what I am searching for !!! 😎😎😎{NO_COLOR}")
            #system('cls')
            print(f"Event ---> {event}\n\n")
            event.set()
        time.sleep(2)

if __name__ == '__main__':

    jobs = []
    #Create Event
    event = multiprocessing.Event()

    #Create ten processes with 1 CPU
    for i in range(10):
        p = multiprocessing.Process(target=f,args=(event,))
        p.start()
        jobs.append(p)

    # Check whether event is set or not, and When set close all child processes
    while True:
        if event.is_set():
            print("======= Exiting all child processess ======")            
            for i in jobs:
                print(f"Job i name: {i.name} pid: {i.pid}  ||| type = {type(i)}")
                print(f"Job i {i}")
                #Terminate each process
                i.terminate()
            #Terminating main process
            sys.exit(1)
        time.sleep(1)
        
        
    
