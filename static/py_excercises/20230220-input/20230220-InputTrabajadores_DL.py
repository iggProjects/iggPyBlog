# scrip for register worker data

# IMPORT
import re   
from math import ceil
import os, sys
from os import  system

# My Own Functions from include dir 
try:   # Import My Own Functions from include dir 
    import sys, traceback     
    from os import system
    from os.path import dirname, realpath
    # import My Own Func
    from MyColors import *
    from MyFunc_copy_DL import *    
except Exception as ImportError:
    FR_RED   = "\033[91m" 
    NO_COLOR = "\033[00m"
    print("print empty line") 
    print(f"{FR_RED}IMPORT ERROR ==>{NO_COLOR} {ImportError} | {ImportError.__class__} | {ImportError.__doc__}")

# get name of script
my_script = __file__.split('\\')
my_script_name = my_script[len(my_script)-1]

# Y,N answer function
def Y_N():
    global moreData    
    ans=str(input("\n\tDo you want to continue including workers? (Y,N): "))
    print(f"\t\tAnswer -> {ans}\n")  
    if ans == 'N':                        
        moreData=False
    elif ans == 'Y':                                
        input_worker_data()
    else:
        Y_N()

# Asking worker age
def input_worker_age():
    global moreData,workers,worker    
    try:
        worker_age=int(input(frRED("\tPlease indicate \"age\" (integer between 18-65): ")))
        if worker_age in range(18,65):
            print(frRED(f"\t\tage -> {worker_age}")) # next version: redirect a log file for answer
            # DB code or use var type dictionary to print data session
            worker["age"] = worker_age
            workers.append(worker)
            # ask for continue (Y,N)
            Y_N()
        else:
            frRED("\tPlease indicate \"age\" (integer between 18-65): ") 
            input_worker_age()    
    except ValueError:
        frRED("\nPlease indicate \"age\" (integer between 18-65): ")
        #print('please indicate age (integer between 18-65)')
        input_worker_age()

def input_worker_data():
    global moreData, workers, worker
    worker = {"name":'',"age":''}   
    # first try for worker name
    try:        
        #name_worker=str(input("\033[94mPlease enter your name: \033[00m"))               
        worker_name = str(input(frGREEN("\tPlease enter worker name: ")))     
        # check characters
        if re.match("^[A-Za-zñáéíóúü]*$", worker_name):      
            print(frGREEN(f"\t\tname -> {worker_name}\n"))  # next version: redirect a log file for answer
            # code to update DB or create a list with data type dictionary            
            worker["name"] = worker_name
            # call age funtion
            input_worker_age()            
    except ValueError:
        # print('Please enter your name')
        frGREEN("\tPlease enter your name: ")
        input_worker_data()

# MAIN
if __name__ == "__main__":

    system('cls')
    print(f"\n{FR_BLUE}=== MAIN ==={NO_COLOR}\n")
    print(f"{FR_GREEN}=== INPUT WORKERS TABLE\n")
    #pause()    
    
    # global variables
    moreData=True
    workers = []
    worker = {"name":'',"age":''}

    # loop until stop is "Y"
    while moreData:    
        input_worker_data()     

    print(f"\n\t{FR_YELL}Session terminated by user{NO_COLOR}\n")        
    print(f"\tVar Workers type: {type(workers)} | Values: {workers}\n")
    for i in range(len(workers)):
        print(f"\tworker {i}: - {workers[i]}, type: {type(workers[i])}")        
        for key,value in workers[i].items():
            print(f"\t\t{key}: {value}")
    print()
    pause()   

    # ------------------------------------------------
    #        OPTIONAL: SHOW VARS CHARACTERISTICS 
    #------------------------------------------------ 

    yesss=True
    _msg = "\tDo you want to see attributes for a specific VAR ? (Y,N): "   
    while yesss:        
        answer=Y_N_2(_msg)        
        if answer in ['Y','N']: yesss = False

    if answer == 'Y':            
        # add question for name of var.....
        _what_var = str(input("\tWhat VAR ? "))
        try:
            _what_var
            _my_Obj_name = eval(_what_var)
            print(f"\n{FR_GREEN}---------- INFO FOR OBJECT '{_my_Obj_name}' ----------{NO_COLOR}\n")
            pause()
            # my objects functions  
            mostrar(_my_Obj_name)  
            pause()     

        except NameError:
            print(f"\n\t{FR_RED}---- Var '{_what_var}' doesn't exits ----")
            print(f"\n{FR_GREEN}--------------- That's all for today ---------------{NO_COLOR}\n")
            #_my_Obj_name = None 

    else:
        print(f"\n{FR_GREEN}---------- That's all for today ----------{NO_COLOR}\n")

else:
    # something wrong
    print(f"\n{FR_RED}---- upsssssssss something is wrong 😢😢  ---{NO_COLOR}\n")
    pause()