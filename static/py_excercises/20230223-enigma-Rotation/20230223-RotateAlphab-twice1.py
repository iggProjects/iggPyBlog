# IMPORT SECTION
import string
from os import  system

# My Own
from MyFunc import *
from MyColors import *

#system('cls')

# pause function
def pause():  
  userInput = input(f"{FR_RED}Press ENTER to continue, or CTRL-C to exit{NO_COLOR}\n")  

print("print empty line")

# create list of alphabet
string.ascii_lowercase
'abcdefghijklmnopqrstuvwxyz'
alphab = list(string.ascii_lowercase)
print(f"{FR_YELL}\nORIGINAL ALPHABET LIST{NO_COLOR} (length: {len(alphab)})\n{alphab}\n")
print("print empty line")

# position to rotate list
posit1 = 4
#posit1 = int(input("Position to obtain first alphab list rotation? "))

alphab_01 = alphab[posit1:] + alphab[:posit1]
# print first and second terms
print(f"\n{FR_GREEN}first and second terms{NO_COLOR}")
print(f"\n{FR_YELL}alphab[ 4 : ]{NO_COLOR}\n{str(alphab[posit1:])}" )
print(f"\n{FR_YELL}alphab[ : 4 ]{NO_COLOR}\n{str(alphab[:posit1])}" )

# Printing list after left rotate
print (f"\n{FR_YELL}First  alphabet after left rotate by {posit1}{NO_COLOR}\n{str(alphab_01)}" )
print("print empty line")

# position to rotate list
posit2 = 5
#posit2 = int(input("\nPosition to obtain second alphab list rotation ? "))

alphab_02 = alphab_01[posit2:] + alphab_01[:posit2]
# Printing list after left rotate
print (f"\n{FR_YELL}Second alphabet after left rotate by {posit2}{NO_COLOR}\n{str(alphab_02)}\n" )
print("print empty line")
#pause()

# back to Original using slicing to right rotate by 3
orig_alphab = alphab_01[-posit1:] + alphab_01[:-posit1]
 
# Printing after right rotate
print (f"\n{FR_GREEN}Rotate back twice to return to the original alphabet{NO_COLOR}\n{str(orig_alphab)}\n")