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
#old_alphab = list(string.ascii_lowercase)
print(f"{FR_YELL}\nORIGINAL ALPHABET LIST{NO_COLOR}\n{alphab}\n")
#print(f"{FR_YELL}old alphabet list ➡  {NO_COLOR}{old_alphab}\n")

# position to rotate list
posit = int(input("Position to make alphab list rotation ? "))
#print(f"\t{FR_GREEN}posit: {posit}{NO_COLOR}")  

# printing original list
print (f"\n{FR_GREEN}Original alphabet\n{str(alphab)}{NO_COLOR}")
 
# using slicing to left rotate by 2
print(f"\n\t from posit {posit} to end: {alphab[posit:]}") 
print(f"\t from 0 to {posit} posit:  {alphab[:posit]}\n") 

new_alphab = alphab[posit:] + alphab[:posit]
 
# Printing list after left rotate
print (f"{FR_YELL}New alphabet after left rotate by 3{NO_COLOR}\n{str(new_alphab)}" )
 
# back to Original using slicing to right rotate by 3
orig_alphab = new_alphab[-posit:] + new_alphab[:-posit]
 
# Printing after right rotate
print (f"\nAlphabet list after right inverse rotate (-{posit}) (back to original)\n{str(orig_alphab)}\n")


"""
def rotate_list(lst, n):
    return list(reversed(lst[-n:])) + lst[:-n]
 
my_list = [1, 2, 3, 4, 5]
# printing original list
print ("Original list : " + str(my_list))
  
rotated_list = rotate_list(my_list, 2)
print(rotated_list)"""