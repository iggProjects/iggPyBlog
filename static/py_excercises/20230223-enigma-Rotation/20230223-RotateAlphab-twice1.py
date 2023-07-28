import string
from os import  system
#import MyColors

#system('cls')

NO_COLOR = "\033[00m"
FR_RED   = "\033[91m"
FR_GREEN = "\033[92m"
FR_YELL  = "\033[93m"
FR_BLUE  = "\033[94m"
FR_MAG   = "\033[95m"

# pause function
def pause():  
  userInput = input(f"{FR_RED}Press ENTER to continue, or CTRL-C to exit{NO_COLOR}\n")  

print("print empty line")

# create list of alphabet
string.ascii_lowercase
'abcdefghijklmnopqrstuvwxyz'
alphab = list(string.ascii_lowercase)
print(f"{FR_YELL}\nORIGINAL ALPHABET LIST{NO_COLOR} (length: {len(alphab)})\n\t{alphab}\n")
print("print empty line")

# position to rotate list
posit1 = 4
#posit1 = int(input("Position to obtain first alphab list rotation? "))

alphab_01 = alphab[posit1:] + alphab[:posit1]
# Printing list after left rotate
print (f"\n{FR_YELL}First  alphabet after left rotate by {posit1}{NO_COLOR}\n\t{str(alphab_01)}" )
print("print empty line")

# position to rotate list
posit2 = 5
#posit2 = int(input("\nPosition to obtain second alphab list rotation ? "))

alphab_02 = alphab_01[posit2:] + alphab_01[:posit2]
# Printing list after left rotate
print (f"\n{FR_YELL}Second alphabet after left rotate by {posit2}{NO_COLOR}\n\t{str(alphab_02)}\n" )
print("print empty line")
#pause()

# back to Original using slicing to right rotate by 3
orig_alphab = alphab_01[-posit1:] + alphab_01[:-posit1]
 
# Printing after right rotate
print (f"\n{FR_GREEN}First rotated alphabet list after right inverse rotate (back twice to original){NO_COLOR}\n\t{str(orig_alphab)}\n")