# scrip for register worker data

# IMPORT
import re   
from MyFunc import *
from MyColors import *
from math import ceil
from os import  system

# CONSTANTS
"""
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
        worker_age=int(input(frRED("\n\tPlease indicate \"age\" (integer between 18-65): ")))
        if worker_age in range(18,65):
            print(frRED(f"\t\tage -> {worker_age}")) # next version: redirect a log file for answer
            # DB code or use var type dictionary to print data session
            worker["age"] = worker_age
            workers.append(worker)
            # ask for continue (Y,N)
            Y_N()
        else:
            frRED("\n\tPlease indicate \"age\" (integer between 18-65): ") 
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
        worker_name = str(input(frGREEN("\tPlease enter your name: ")))     
        # check characters
        if re.match("^[A-Za-zñáéíóúü]*$", worker_name):      
            print(frGREEN(f"\t\tname -> {worker_name}"))  # next version: redirect a log file for answer
            # code to update DB or create a list with data type dictionary            
            worker["name"] = worker_name
            # call age funtion
            input_worker_age()            
    except ValueError:
        # print('Please enter your name')
        frGREEN("\tPlease enter your name: ")
        input_worker_data()
    """

# MAIN
if __name__ == "__main__":

    #system('cls')
    print("print empty line")
    print(f"{FR_BLUE}=== MAIN ==={NO_COLOR}")
    print("print empty line")
    print(f"{FR_GREEN}=== INPUT WORKERS TABLE{NO_COLOR}")
    print("print empty line")
        
    # global variables
    moreData=True
    workers = []
    worker = {"name":'',"age":''}

    """
      code with worker data

    """
    print(f"\n\t{FR_YELL}Session terminated by user{NO_COLOR}\n")        
    print(f"\tVar Workers type: {type(workers)} | Values: {workers}\n")
    print("print empty line")
    for i in range(len(workers)):
        print(f"\tworker {i}: - {workers[i]}, type: {type(workers[i])}")        
        for key,value in workers[i].items():
            print(f"\t\t{key}: {value}")
    print("print empty line")
    print(f"\n{FR_GREEN}---------- That's all for today ----------{NO_COLOR}\n")     

    # ------------------------------------------------
    #        OPTIONAL: SHOW VARS CHARACTERISTICS 
    #------------------------------------------------ 
    """
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

        except NameError:
            print(f"\n\t{FR_RED}---- Var '{_what_var}' doesn't exits ----")
            print(f"\n{FR_GREEN}--------------- That's all for today ---------------{NO_COLOR}\n")
            #_my_Obj_name = None 

    else:
        print(f"\n{FR_GREEN}---------- That's all for today ----------{NO_COLOR}\n")
    """

else:
    # something wrong
    print(f"\n{FR_RED}---- upsssssssss something is wrong 😢😢  ---{NO_COLOR}\n")
    
