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

def alphab_jump(alph,k,msg):
  # jump valur to rotate list
  jump = -k  
  alphab_j = alph[jump:] + alph[:jump]
  # print first and second terms
  """
  print(f"{FR_GREEN}first and second terms{NO_COLOR}")
  print(f"{FR_YELL}alphab[ {jump} : ]{NO_COLOR}\n{str(alphab[jump:])}" )
  print(f"{FR_YELL}alphab[ : {jump} ]{NO_COLOR}\n{str(alphab[:jump])}" )  
  """
  print(f"{FR_GREEN}{msg}: {NO_COLOR}\n{str(alphab_j)}" )
  return alphab_j


if __name__ == "__main__":

  print("print empty line")
  alphab_1 = ""

  # create list of alphabet
  string.ascii_lowercase 
  'abcdefghijklmnopqrstuvwxyz'
  alphab = list(string.ascii_lowercase)
  print(f"{FR_YELL}\nORIGINAL ALPHABET LIST{NO_COLOR} (length: {len(alphab)})\n{alphab}")
  print("print empty line")

  jump=1
  msg = "Rotate + " + str(jump)
  new_alphab = alphab_jump(alphab,jump, msg)
  print("print empty line")
  print("print empty line")

  # back to Original using slicing to right rotate by jump
  print(f"{FR_YELL}RETURN TO ORIGINAL ALPHABET{NO_COLOR}")
  msg = "Rotate - " + str(jump)
  alphab_jump(new_alphab,-jump,msg)
  