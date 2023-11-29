# https://stackoverflow.com/questions/28821910/how-to-get-around-the-pickling-error-of-python-multiprocessing-without-being-in?rq=4

import multiprocessing, platform
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

def domath(l):
    return doProduct(int(l[0]),int(l[1]))

if __name__ == '__main__':

    try: 
        
        if platform.system() == 'Windows':
            system('cls')
        elif platform.system() == 'Linux':            
            system('clear')
        else:
            pass  

        print(f"{FR_YELL}List of integer pairs{NO_COLOR}")
        _lst = [(x, y) for x in range(1,10) for y in range(11)]
        print(_lst)
        print()
        print(f"{FR_MAG}Running MP Pool{NO_COLOR}")
        print()
        pool1 = multiprocessing.Pool(3)
        result_list= pool1.map(domath, _lst)
        print()
        print(f"{FR_YELL}RESULT: LIST OR PAIR PRODUCTS{NO_COLOR}")
        print(result_list)
        print()
        
    except Exception as Argument:        
        print(f"ERROR from MAIN: <{Argument}>")

else:
    print("new ....")