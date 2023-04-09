#
# IMPORT SECTION
#
from MyFunc import *
from MyColors import *
from os import system
import string, random, time

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

    # time
    inicio = time.time()
    system('cls')
    print(f"\n{FR_GREEN}---------- main ----------{NO_COLOR}\n")

    alphab = list('abcdefghijklmnopqrstuvwxyz')
    numb_alphab = 0
    alphab_list = []
    alphab_list.append(alphab)
    print(f"first alphab: {alphab_list[0]}\n")
    alphab_list.append(['-----alphabet-----'])    

    for i in range(26):        
        first_alphab = alphab[i:] + alphab[:i]
        #alphab_list.append(first_alphab)
        print(f"list for: {first_alphab}")
        for j in range(26):   
            second_alphab = first_alphab[j+1:] + first_alphab[:j+1]
            #second_alphab = alphab_list[i][j+1:] + alphab_list[i][:j+1]
            alphab_list.append(second_alphab)
            print(f"\t2nd list: {''.join(second_alphab)}")
        numb_alphab += 26
        alphab_list.append(['------------'])    
    
    print(f"{FR_YELL}new alphabets : {numb_alphab}{NO_COLOR}\n")
    # Printing list after left rotate
    #for i in alphab_list:
    #    print (f"{FR_YELL}alphabet after rotation{NO_COLOR}: {''.join(i)}" )

    for i in range(len(alphab_list)):
        alp = ''.join(alphab_list[i])
        #alp = ''.join(random.choices(string.ascii_lowercase, k=26))
        rotationFile = open("z-rotationFile.txt", "a")
        alp = alp+'\n'
        rotationFile.write(alp)
        #permutFile.close()
        #numb_alphab += 1
        #print(f"\t{numb_alphab}")

    # time  
    elapsed_time = "{:.2f}".format(time.time()-inicio)
    print(f"\n{FR_GREEN}\tTotal new alphabets generated: {numb_alphab}{NO_COLOR}\n")    
    print(f"\n================  Elapsed time: {elapsed_time}  =================\n\n")
    

else:
    # something wrong
    print(f"\n{FR_RED}---- upsssssssss something is wrong 😢😢  ---{NO_COLOR}\n")
    pause()