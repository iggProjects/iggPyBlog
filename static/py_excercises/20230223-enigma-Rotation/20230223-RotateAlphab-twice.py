import string
from os import  system
#import MyColors

system('cls')

NO_COLOR = "\033[00m"
FR_RED   = "\033[91m"
FR_GREEN = "\033[92m"
FR_YELL  = "\033[93m"
FR_BLUE  = "\033[94m"
FR_MAG   = "\033[95m"

# create list of alphabet
string.ascii_lowercase
'abcdefghijklmnopqrstuvwxyz'
alphab = list(string.ascii_lowercase)
print(f"{FR_YELL}\nORIGINAL ALPHABET LIST{NO_COLOR} (length: {len(alphab)})\n{alphab}\n")

# position to rotate list
posit = int(input("Position to make alphab list rotation ? "))

# printing original list
print (f"\n{FR_GREEN}Original alphabet{NO_COLOR}\n{str(alphab)}")

alphab_01 = alphab[posit:] + alphab[:posit]
# Printing list after left rotate
print (f"\n{FR_YELL}First  alphabet after left rotate by {posit}{NO_COLOR}\n{str(alphab_01)}" )

alphab_02 = alphab_01[posit:] + alphab_01[:posit]
# Printing list after left rotate
print (f"{FR_YELL}Second alphabet after left rotate by {posit}{NO_COLOR}\n{str(alphab_02)}" )

# back to Original using slicing to right rotate by 3
orig_alphab = alphab_01[-posit:] + alphab_01[:-posit]
 
# Printing after right rotate
print (f"\nAlphabet list after right inverse rotate (-{posit}) (back to original)\n{str(orig_alphab)}\n")