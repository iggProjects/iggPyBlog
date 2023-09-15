# scrip for register worker data

# IMPORT
import re   
from MyFunc import *
from MyColors import *
from math import ceil
import os, sys
from os import  system

# include root path in sys.path
ROOT_DIR = os.path.abspath(os.curdir)
# check in what server is app
if "iggWebNz" in ROOT_DIR:              # pythonanywhere  
    ROOT_DIR = ROOT_DIR + "/mysite"
else:                                   # working in localhost server
    pass 
sys.path.insert(1, ROOT_DIR)

# import "My Own Funct" from root path
from MyFunc import *

# CONSTANTS


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
    
