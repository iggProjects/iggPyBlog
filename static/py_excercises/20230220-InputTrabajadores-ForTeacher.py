# scrip for register worker data

# IMPORT
import re   
from MyFunc_ForTeacher import *
from Colors_ForTeacher import *
from math import ceil

# Y,N answer function
def Y_N():
    global moreData    
    ans=str(input("\nDo you want to continue including workers? (Y,N): "))
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
        worker_age=int(input(frRED("\nPlease indicate \"age\" (integer between 18-65): ")))
        if worker_age in range(18,65):
            print(frRED(f"\t\tage entered -> {worker_age}")) # next version: redirect a log file for answer
            # DB code or use var type dictionary to print data session
            worker["age"] = worker_age
            workers.append(worker)
            # ask for continue (Y,N)
            Y_N()
        else:
            frRED("\nPlease indicate \"age\" (integer between 18-65): ") 
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
        worker_name = str(input(frGREEN("Please enter your name: ")))     
        # check characters
        if re.match("^[A-Za-zñáéíóúü]*$", worker_name):      
            print(frGREEN(f"\t\tname -> {worker_name}"))  # next version: redirect a log file for answer
            # code to update DB or create a list with data type dictionary            
            worker["name"] = worker_name
            # call age funtion
            input_worker_age()            
    except ValueError:
        # print('Please enter your name')
        frGREEN("Please enter your name: ")
        input_worker_data()

# MAIN
if __name__ == "__main__":
    # global variables
    moreData=True
    workers = []
    worker = {"name":'',"age":''}

    # loop until stop is "Y"
    while moreData:    
        input_worker_data()     

    print("\nsession terminated by user\n")        
    print(f"Workers is {type(workers)}:\n\t{workers}\n")
    for i in range(len(workers)):
        print(f"{workers[i]}, and data type is: {type(workers[i])}")
        print(f"\tworker {i}:")
        for key,value in workers[i].items():
            print(f"\t\t{key}: {value}")

    # ------------------------------------------------
    #          SHOW VARS CHARACTERISTICS 
    #------------------------------------------------ 

    yesss=True   
    while yesss:
        _msg = "Do you want to see attributes for a specific VAR ? (Y,N): "
        answer=Y_N_2(_msg)        
        if answer in ['Y','N']: yesss = False

    if answer == 'Y':            
        # add question for name of var.....
        _what_var = str(input("What VAR ? "))
        try: 
            _what_var
            _my_Obj_name = eval(_what_var)
            print(f"\n{FR_GREEN}---------- INFO FOR OBJECT '{_my_Obj_name}' ----------{NO_COLOR}\n")
            pause()
            # my objects functions  
            mostrar(_my_Obj_name)       

        except NameError:
            print(f"\n\t{FR_RED}---- Var '{_what_var}' doesn't exits 🙄🙄  ----")
            print(f"\n{FR_GREEN}--------------- That's all for today 👌 ---------------{NO_COLOR}\n")
            #_my_Obj_name = None 

    else:
        print(f"\n{FR_GREEN}---------- That's all for today 👌 ----------{NO_COLOR}\n")

else:
    # something wrong
    print(f"\n{FR_RED}---- upsssssssss something is wrong 😢😢  ---{NO_COLOR}\n")
    pause()
