# IMPORT SECTION
import string
from os import  system

# My Own Color Constants
NO_COLOR = "\033[00m"
FR_RED   = "\033[91m"
FR_GREEN = "\033[92m"
FR_YELL  = "\033[93m"
FR_BLUE  = "\033[94m"
FR_MAG   = "\033[95m"

def alphab_jump(alph,k):
  # jump value -k to rotate list    
  return alph[-k:] + alph[:-k]

if __name__ == "__main__":

  print("print empty line")

  # create list of alphabet
  string.ascii_lowercase 
  'abcdefghijklmnopqrstuvwxyz'
  alphab = list(string.ascii_lowercase)
  print(f"{FR_YELL}\nORIGINAL ALPHABET LIST{NO_COLOR} (length: {len(alphab)})\n{alphab}\n\n")
  #print("print empty line")
  
  # list of all alphabets with rotation by 1 to right position
  alphab_list = []  
  for jump in range(27):        
    print(jump)     
    alphab_list.append(alphab_jump(alphab,jump))
    print(alphab_list[jump])

   
  