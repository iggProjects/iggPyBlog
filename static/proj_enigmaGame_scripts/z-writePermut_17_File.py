#
# IMPORT SECTION
#
from MyFunc import *
from MyColors import *
import os
from os import system
import string, random, time

#
# ---------- COURSE EXCERCISE ----------
#

if __name__ == "__main__":

    # time
    inicio = time.time()
    system('cls')
    print(f"\n{FR_GREEN}---------- main ----------{NO_COLOR}\n")

    # alphab = 'abcdefghijklmnopqrstuvwxyz'
    # substr size 15, of alphabet chars chosen to create permutations
    alphab_17 = 'abcdefgilmnoprstu'
    alphab_17_list = list(alphab_17)
    numb_alphab = 0
    alphab_with_char_conflict = 0
    num_chars_equal = 0

    # delete if exists  
    if os.path.exists("z-permutFile.txt"):
        os.remove("z-permutFile.txt")
        print(f"{FR_GREEN}........ old z-permutFile.txt deleted")    

    if os.path.exists("z-permutFileSorted.txt"):
        os.remove("z-permutFileSorted.txt")
        print(f"{FR_GREEN}........ old z-permutFileSorted.txt deleted")    


    while numb_alphab < 500000:
    #while numb_alphab < 500000:    

        alp = list(alphab_17)
        random.shuffle(alp)
        
        # discard permutations that keep the character in place
        for i in range(17):
            if alp[i] == alphab_17_list[i]:
                #print(f"\t{i+1}: {''.join(alp)} | {''.join(alphab_15_list)}")
                num_chars_equal +=1
        #print()       

        if num_chars_equal == 0:
            alp = ''.join(alp)
            alp = alp + '\n'
            permutFile = open("z-permutFile.txt", "a")
            permutFile.write(alp)
            permutFile.close()
            numb_alphab += 1
        else:
            alphab_with_char_conflict += 1    

        num_chars_equal = 0              
    
    # delete duplicated lines and sort
    uniqlines = set(open('z-permutFile.txt').readlines())
    uniqlines = sorted(uniqlines)
    #print(f"uniqlines type is {type(uniqlines)}")
    open('z-permutFileSorted.txt', 'w').writelines(uniqlines)

    # time  
    elapsed_time = "{:.2f}".format(time.time()-inicio)
    print(f"\n{FR_GREEN}\tTotal new alphabets generated: {numb_alphab}{NO_COLOR}\n")
    print(f"\n{FR_GREEN}\tTotal alphabets discarded by conflict in character position: {alphab_with_char_conflict}{NO_COLOR}\n")
    
    print(f"\n================  Elapsed time: {elapsed_time}  =================\n\n")
    

else:
    # something wrong
    print(f"\n{FR_RED}---- upsssssssss something is wrong 😢😢  ---{NO_COLOR}\n")
    pause()