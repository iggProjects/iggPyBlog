import string
#import MyColors

NO_COLOR = "\033[00m"
FR_RED   = "\033[91m"
FR_GREEN = "\033[92m"
FR_YELL  = "\033[93m"
FR_BLUE  = "\033[94m"
FR_MAG   = "\033[95m"

# initializing list
test_list = [1, 2, 3, 4, 5, 6, 7, 8]

# position to rotate list
posit = int(input("Position to make list rotation ? "))
print(f"posit: {posit}")  

# printing original list
print ("\nOriginal list : " + str(test_list))
 
# using slicing to left rotate by 2
print(f"\n\t following 2nd posit: {test_list[posit:]}") 
print(f"\t from 0 to 2nd posit:  {test_list[:posit]}\n") 

test_list = test_list[posit:] + test_list[:posit]
 
# Printing list after left rotate
print ("\nList after left rotate by 3 : " + str(test_list))
 
# using slicing to right rotate by 3
# back to Original
test_list = test_list[-posit:] + test_list[:-posit]
 
# Printing after right rotate
print ("\nList after right rotate by 3(back to original) : "  + str(test_list) + "\n")