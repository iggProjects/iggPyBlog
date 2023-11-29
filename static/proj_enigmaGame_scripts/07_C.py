# https://stackoverflow.com/questions/28821910/how-to-get-around-the-pickling-error-of-python-multiprocessing-without-being-in?rq=4

import multiprocessing, platform, time
from os import system

NO_COLOR = "\033[00m"
FR_RED   = "\033[91m"
FR_GREEN = "\033[92m"
FR_YELL  = "\033[93m"
FR_BLUE  = "\033[94m"
FR_MAG   = "\033[95m"

def doProduct(a,b):
    prod=0
    for i in range(a):
        for j in range(b):
            prod += 1
    return prod

def domath1(l):
    try:

        if l[1] % 2000 == 0:        
            if multiprocessing.current_process().name == "SpawnPoolWorker-1":
                print(f"{NO_COLOR}\t{multiprocessing.current_process().name} ==> {int(l[0])}*{int(l[1])} = {doProduct(int(l[0]),int(l[1]))}")
            elif multiprocessing.current_process().name == "SpawnPoolWorker-2":
                print(f"{FR_YELL}\t\t{multiprocessing.current_process().name} ==>{NO_COLOR} {int(l[0])}*{int(l[1])} = {doProduct(int(l[0]),int(l[1]))}")
            elif multiprocessing.current_process().name == "SpawnPoolWorker-3":
                print(f"{FR_GREEN}\t\t\t{multiprocessing.current_process().name} ==>{NO_COLOR} {int(l[0])}*{int(l[1])} = {doProduct(int(l[0]),int(l[1]))}")
            else:
                print(f"{FR_RED}\t\t\t\t{multiprocessing.current_process().name} ==>{NO_COLOR} {int(l[0])}*{int(l[1])} = {doProduct(int(l[0]),int(l[1]))}")
        else:
            pass

    except Exception as Argument:        
        print(f"\tSpawnPoolWorker-4 | ERROR from domath1: <{Argument}>")            

def printPairs(listPairs,nCPU):
    with multiprocessing.Pool(nCPU) as pool:
        print(f"\t{FR_MAG}===== pool : {pool} ====={NO_COLOR}")
        pool.map(domath1,listPairs)


if __name__ == '__main__':

    try: 
        
        if platform.system() == 'Windows':
            system('cls')
        elif platform.system() == 'Linux':            
            system('clear')
        else:
            pass

        # time
        inicio = time.time()
        print(f"{FR_RED}Process start at:{NO_COLOR} {inicio}{NO_COLOR}")
        print()

        _lst = [(x, y) for x in range(1,11) for y in range(100001)]
       
        printPairs(_lst,multiprocessing.cpu_count())

        print()
        elapsed_time = "{:.2f}".format(time.time()-inicio)        
        print(f"{FR_RED}Elapsed Time:{NO_COLOR} {elapsed_time} seconds{NO_COLOR}")
        print(f"{FR_RED}Number of CPUs:{NO_COLOR} {multiprocessing.cpu_count()}{NO_COLOR}")


    except Exception as Argument:        
        print(f"ERROR from MAIN: <{Argument}>")

else:
    print(f"new thread: {multiprocessing.current_process().name}")