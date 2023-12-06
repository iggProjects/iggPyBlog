# https://stackoverflow.com/questions/28821910/how-to-get-around-the-pickling-error-of-python-multiprocessing-without-being-in?rq=4

# IMPORT SECTION
try:   # Import My Own Functions from include dir 
	import sys, traceback, multiprocessing, platform, time
	import numpy as np
	import multiprocessing
	import time
	import sys
	from os import system	
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
    print("print empty line") 
    print(f"{FR_RED}IMPORT ERROR ==>{NO_COLOR} {ImportError} | {ImportError.__class__} | {ImportError.__doc__}")


# MY FUNCT
def doProduct(a,b):
    prod=0
    for i in range(a):
        for j in range(b):
            prod += 1
    return prod

def domath1(l):
    try:

        if l[1] % NPRINT == 0:        
            if "PoolWorker-1" in multiprocessing.current_process().name:
                print(f"{FR_MAG}....{multiprocessing.current_process().name} ==> {int(l[0])}*{int(l[1])} = {doProduct(int(l[0]),int(l[1]))}")
            elif "PoolWorker-2" in multiprocessing.current_process().name:
                print(f"{FR_GREEN}........{multiprocessing.current_process().name} ==> {int(l[0])}*{int(l[1])} = {doProduct(int(l[0]),int(l[1]))}")
            elif "PoolWorker-3" in multiprocessing.current_process().name:
                print(f"{FR_BLUE}............{multiprocessing.current_process().name} ==> {int(l[0])}*{int(l[1])} = {doProduct(int(l[0]),int(l[1]))}")
            elif "PoolWorker-4" in multiprocessing.current_process().name:
                print(f"{FR_RED}................{multiprocessing.current_process().name} ==> {int(l[0])}*{int(l[1])} = {doProduct(int(l[0]),int(l[1]))}")
            else:
                print(f"{NO_COLOR}..................{multiprocessing.current_process().name} ==> {int(l[0])}*{int(l[1])} = {doProduct(int(l[0]),int(l[1]))}")
        else:
            pass

    except Exception as Argument:        
        print(f"\tERROR from domath1: <{Argument}>")            

def printPairs(listPairs,nCPU):
    with multiprocessing.Pool(nCPU) as pool:
        print(f"\t{FR_MAG}===== pool : {pool} =====")
        pool.map(domath1,listPairs)

# CONSTANTS
# print every 'NPRINT' times
NPRINT = 10000

if __name__ == '__main__':

    try: 
        
        # time
        inicio = time.time()
        print("print empty line")
        print(f"{FR_RED}Process start at: {inicio}")
        print("print empty line")

        my_script = __file__.split('\\')
        my_script_name = my_script[len(my_script)-1]
        write_log_file("my_messages.txt","IN '" + my_script_name + "'")

        _lst = [(x, y) for x in range(1,11) for y in range(100001)]
       
        printPairs(_lst,multiprocessing.cpu_count())

        print("print empty line")
        elapsed_time = "{:.2f}".format(time.time()-inicio)      
        print(f"{FR_BLUE}List of pairs processed:  _lst = [(x, y) for x in range(1,11) for y in range(100001)]")  
        print(f"{FR_BLUE}List of pairs printed:  every {NPRINT} in each series")
        print(f"{FR_BLUE}Series: (1,x) (2,x) (3,x) (4,x) (5,x) (6,x) (7,x) (8,x) (9,x) (10,x) with x in interval [1..100.001]")
        print("print empty line") 
        print(f"{FR_RED}Elapsed Time: {elapsed_time} seconds")
        print(f"{FR_RED}Number of CPUs: {multiprocessing.cpu_count()}")


    except Exception as Argument:
        error_msg = "ERROR IN <" + my_script_name + ">. SEE server_messages.txt !"
        write_log_file("my_messages.txt",error_msg)
        write_traceback_info_1(Argument,traceback,my_script_name)

else:
    print("print empty line") 
    print(f"{FR_RED}=== new thread: {multiprocessing.current_process().name}")