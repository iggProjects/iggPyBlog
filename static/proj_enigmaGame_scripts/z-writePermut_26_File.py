#
# IMPORT SECTION
#
import os
from os import system
import string, random, time
from datetime import datetime

# CONSTANTS
NUM_ALPHAB = 200000

# Colors
NO_COLOR = "\033[00m"
FR_RED   = "\033[91m"
FR_GREEN = "\033[92m"
FR_YELL  = "\033[93m"
FR_BLUE  = "\033[94m"
FR_MAG   = "\033[95m"

# pause function
def pause():  
  userInput = input(f"{FR_RED}Press ENTER to continue, or CTRL-C to exit{NO_COLOR}\n")  

# place thousands separator
def place_comma(numb):
    # thousands separated with dot
    return format(numb,',d').replace(",",".")
    #return ("{:.}".format(numb))

#
# ---------- MAIN ----------
#

if __name__ == "__main__":

    # time
    inicio = time.time()
    system('cls')
    print(f"\n{FR_GREEN}=== MAIN ==={NO_COLOR}\n")
    print(f"\n{FR_GREEN}=== process generating permutations of 'abcdefghijklmnopqrstuvwxyz' start at {NO_COLOR}{datetime.now()} {FR_GREEN}{NO_COLOR}\n")

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

    # delete z-permutFile.txt
    if os.path.exists("z-permutFile.txt"):
        os.remove("z-permutFile.txt")
        print(f"\t== z-permutFile.txt deleted\n")   

    # time  
    elapsed_time = (time.time()-inicio)
    #elapsed_time = "{:..2f}".format(time.time()-inicio)
    alphab_per_seconds = (numb_alphab + alphab_with_char_conflict)/(time.time()-inicio)
    alphab_per_seconds_format = place_comma(int(alphab_per_seconds))
    #alphab_per_seconds_format = "{:,.2f}".format(alphab_per_seconds)

    print(f"\n{FR_GREEN}\tNumber of new alphabets in z-permutFileSorted.txt:{NO_COLOR} {place_comma(numb_alphab)}\n")
    print(f"\n{FR_GREEN}\tTotal alphabets discarded by conflict in character position:{NO_COLOR} {place_comma(alphab_with_char_conflict)}\n")
    print(f"\n{FR_GREEN}=== process generating alphabets stoped at {NO_COLOR}{datetime.now()}\n")
    print(f"\n{FR_GREEN}===  Elapsed time in seconds:{NO_COLOR} {str(elapsed_time).replace('.',',')}\n")
    
    print(f"\n{FR_GREEN}===  Total Alphabets per Seconds:{NO_COLOR} {alphab_per_seconds_format}\n\n")
    


else:
    # something wrong
    print(f"\n{FR_RED}---- upsssssssss something is wrong 😢😢  ---{NO_COLOR}\n")
    pause()