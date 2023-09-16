# IMPORT SECTION
import os, sys, string
from os import  system

# Include root path in sys.path
ROOT_DIR = os.path.abspath(os.curdir)
sys.path.insert(1, ROOT_DIR)

# Import My Own Funct in root path
from MyFunc import *

# pause function
def pause():  
  userInput = input(f"{FR_RED}Press ENTER to continue, or CTRL-C to exit{NO_COLOR}\n")  


if __name__ == "__main__":

    system('cls')

    # create list of alphabet
    string.ascii_lowercase
    'abcdefghijklmnopqrstuvwxyz'
    alphab = list(string.ascii_lowercase)
    print(f"{FR_YELL}\nORIGINAL ALPHABET LIST{NO_COLOR} (length: {len(alphab)})\n\t{str(alphab).replace(',','')}\n")

    # position to rotate list
    posit1 = int(input("Number to obtain first alphab list rotation? "))

    # print first and second terms
    print(f"\n{FR_GREEN}first and second terms{NO_COLOR}")
    print(f"\n{FR_YELL}alphab[ posit1 : ]{NO_COLOR}\n\t{str(alphab[posit1:])}" )
    print(f"\n{FR_YELL}alphab[ : posit1 ]{NO_COLOR}\n\t{str(alphab[:posit1])}" )

    alphab_01 = alphab[posit1:] + alphab[:posit1]
    # Printing list after left rotate
    #print (f"\n{FR_YELL}First  alphabet after left rotate by {posit1}{NO_COLOR}\n\t{str(alphab_01).replace(',','')}" )
    print (f"\n{FR_YELL}First  alphabet after left rotate by {posit1} (formula: alphab[4:] + alphab[:4])\n\t{str(alphab_01).replace(',','')}{NO_COLOR}" )
    # position to rotate list
    posit2 = int(input("\nNumber to obtain second alphab list rotation ? "))

    alphab_02 = alphab_01[posit2:] + alphab_01[:posit2]
    # Printing list after left rotate
    print (f"\n{FR_YELL}Second alphabet after left rotate by {posit2}{NO_COLOR}\n\t{str(alphab_02).replace(',','')}\n" )
    pause()

    # back to Original using slicing to right rotate by 3
    orig_alphab = alphab_01[-posit1:] + alphab_01[:-posit1]
    
    # Printing after right rotate
    print (f"\n{FR_GREEN}Rotate back twice to return to the original alphabet{NO_COLOR}\n\t{str(orig_alphab).replace(',','')}\n")

else:
    # something wrong
    print(frRED("---- upsssssssss something is wrong ---"))
    pause()    