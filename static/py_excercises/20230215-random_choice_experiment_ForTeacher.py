"""  
    Testing reliability of the random function

    We will make a thousand executions of the random function in the interval 1 to 10 to verify the probability that a certain number will come out

"""
#
# IMPORT SECTION
#
import random

from MyFunc_ForTeacher import *
from Colors_ForTeacher import *

#
# ---------- COURSE EXCERCISE ----------
#

if __name__ == "__main__":
    print(f"\n{FR_GREEN}---------- main ----------{NO_COLOR}\n")
    pause()

    list=list(range(1,11))
    print(list)
    pause()
    my_value = random.choice(list)
    print(f"my_value:  {my_value}")
    i=1
    #print("my_value: " + my_value)
    while my_value != 5:
        i += 1
        my_value = random.choice(list)
        print(f"attempt {i}, value:  {my_value}")

    print(frGREEN(f"\nattempt {i} , my_value:  {my_value}\n"))

    
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

    else:
        print(f"\n{FR_GREEN}---------- That's all for today 👌 ----------{NO_COLOR}\n")

else:
    # something wrong
    print(f"\n{FR_RED}---- upsssssssss something is wrong 😢😢  ---{NO_COLOR}\n")
    pause()