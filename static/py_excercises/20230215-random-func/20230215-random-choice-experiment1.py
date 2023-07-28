"""  
    Testing reliability of the random function

    We will make a thousand executions of the random function in the interval 1 to 10 to verify the probability that a certain number will come out

"""
#
# IMPORT SECTION
#
import random

from MyFunc import *
from MyColors import *
from os import  system

# CONSTANTS
# Colors
NO_COLOR = "\033[00m"
FR_RED   = "\033[91m"
FR_GREEN = "\033[92m"
FR_YELL  = "\033[93m"
FR_BLUE  = "\033[94m"
FR_MAG   = "\033[95m"


#
# ---------- COURSE EXCERCISE ----------
#

if __name__ == "__main__":

    print("print empty line")
    print(f"{FR_GREEN}=== MAIN")
    print("print empty line")
    print(f"An experiment to check random function, simulating a 'dice'")
    print("print empty line")
    my_dice = {'1':0,'2':0,'3':0,'4':0,'5':0,'6':0}

    ideal_perc = (1/6)
    #ideal_perc = 100 * (1/6)
    ideal_dice = {'1':ideal_perc,'2':ideal_perc,'3':ideal_perc,'4':ideal_perc,'5':ideal_perc,'6':ideal_perc}
    face_list=list(range(1,7))
    print(f"\tDICE faces: {face_list}")

    for i in range(1,11):
        iterations = 6000 * 2 * i
        #print("my_value: " + my_value)
        for i in range(iterations):        
            face = random.choice(face_list)
            my_dice[str(face)] += 1        

        print("print empty line")   
        print(f"\t{FR_GREEN}Experiment result with {iterations:,d} dice rolls:")
        for key in my_dice:
            #face_perc = "{:.4f}".format(100*(dice[key]/iterations))
            ideal_dice = int( ideal_perc * iterations )
            #ideal_dice = int( (ideal_perc/100) * iterations )
            face_diff = my_dice[key] - ideal_dice
            face_diff_perc = "{:.4f}".format(100 * (face_diff / iterations))
            #face_diff = str(face_diff).center(5)
            face_diff = str(face_diff).rjust(8,' ')
            face_diff_perc = str(face_diff_perc).rjust(7, ' ')
            #result = f"\t\t{key}: my dice: {my_dice[key]} | ideal dice: {ideal_dice} | diff: {face_diff} | in perc: {face_diff_perc} "
            #print(f"{result}")
            print(f"\t\t{key}: my dice: {my_dice[key]} | ideal dice: {ideal_dice} | diff: {face_diff}  ({face_diff_perc}%) ")
        
        # reset
        my_dice = {'1':0,'2':0,'3':0,'4':0,'5':0,'6':0}   

    print("print empty line")
    print(f"\t{FR_GREEN}---------- That's all for today ----------")


else:
    # something wrong
    print(f"{FR_RED}---- upsssssssss something is wrong ----{NO_COLOR}")
    