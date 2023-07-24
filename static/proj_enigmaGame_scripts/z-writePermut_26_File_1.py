#
# IMPORT SECTION
#
from MyFunc import *
from MyColors import *
import os
from os import system
import string, random, time
from datetime import datetime

# CONSTANTS
NUM_ALPHAB = 50000

# place thousands separator
def place_comma(numb):
    # thousands separated with dot
    return format(numb,',d').replace(",",".")
    #return ("{:.}".format(numb))

# MAIN
if __name__ == "__main__":

    # time
    inicio = time.time()
    #system('cls')
    print(f"{FR_GREEN}=== main")
    print("print empty line")
    print(f"{FR_GREEN}=== process generating permutations of \'abcdefghijklmnopqrstuvwxyz\' start at {datetime.now()}")
    print("print empty line")

    alphab_26 = 'abcdefghijklmnopqrstuvwxyz'
    alphab_26_list = list(alphab_26)
    numb_alphab = 0
    alphab_with_char_conflict = 0
    num_chars_equal = 0

    # delete if exists  
    if os.path.exists("z-permutFile.txt"):
        os.remove("z-permutFile.txt")
        print(f"\told z-permutFile.txt deleted")    

    if os.path.exists("z-permutFileSorted.txt"):
        os.remove("z-permutFileSorted.txt")
        print(f"\told z-permutFileSorted.txt deleted")    


    while numb_alphab < NUM_ALPHAB:

        alp = list(alphab_26)
        random.shuffle(alp)
        
        # discard permutations that keep the character in place
        for i in range(26):
            if alp[i] == alphab_26_list[i]:
                #print(f"{i+1}: {''.join(alp)} | {''.join(alphab_15_list)}")
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

    # delete z-permutFile.txt
    if os.path.exists("z-permutFile.txt"):
        os.remove("z-permutFile.txt")
        print(f"\tz-permutFile.txt deleted")
        print("print empty line")   

    # time
    elapsed_time = (time.time()-inicio)
    #elapsed_time = "{:.2f}".format(time.time()-inicio)
    alphab_per_seconds = (numb_alphab + alphab_with_char_conflict)/(time.time()-inicio)
    alphab_per_seconds_format = place_comma(int(alphab_per_seconds))
    #alphab_per_seconds_format = "{:,.0f}".format(alphab_per_seconds)

    print(f"{FR_GREEN}\tNumber of new alphabets in z-permutFileSorted.txt: {numb_alphab}")
    print(f"{FR_GREEN}\tTotal alphabets discarded by conflict in character position: {alphab_with_char_conflict}")
    print("print empty line")
    print(f"{FR_GREEN}=== process generating alphabets stoped at {datetime.now()}")
    print("print empty line")
    print(f"\tElapsed time in seconds: {str(elapsed_time).replace(',','.')}")
    print("print empty line")
    print(f"\tTotal Alphabets per Seconds: {alphab_per_seconds_format}")
    print("print empty line")
    print(f"{FR_GREEN}=== That\'s All")
    
else:
    # something wrong
    print(f"{FR_RED}---- upsssssssss something is wrong 😢😢  ---")
    pause()