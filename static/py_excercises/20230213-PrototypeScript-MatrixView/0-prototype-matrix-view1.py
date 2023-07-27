
"""  
THIS SCRIPT IS FOR..................

"""
# IMPORT SECTION
#from MyFunc import *
from MyColors import *
from os import  system

# CONSTANTS
# Colors
NO_COLOR = "\033[00m"
FR_RED   = "\033[91m"
FR_GREEN = "\033[92m"
FR_YELL  = "\033[93m"
FR_BLUE  = "\033[94m"
FR_MAG   = "\033[95m"

# print 'lists-tuples' in matrix form
def matrix_view(obj_l_t,n_cols):
  if 'list' in str(type(obj_l_t)) or 'tuple' in str(type(obj_l_t)):  # cambiar la pregunta
    import math
    matrix_rows=math.ceil(len(obj_l_t)/n_cols)
    line=[]
    i=0
    for i in  range(matrix_rows):    
      for j in range(n_cols):
        if i*n_cols+j<len(obj_l_t):
          line.append(str(obj_l_t[i*n_cols+j]))
      print(f"\t{NO_COLOR}line: {i+1} => {' ; '.join(line)}")
      line=[]  
  else:
    print("Warning FROM matrix_view(): Object '{obj_l_t}' in not  list neither tupla !" ) 

#
# ---------- MAIN ----------
#

if __name__ == "__main__":

    print("print empty line")
    print(f"{FR_GREEN}=== MAIN")    
    print("print empty line")
    sqr_var = [i*i for i in range(100)]
    print(f"{FR_BLUE}=== list of first hundred numbers squared")
    print("print empty line")
    matrix_view(sqr_var,20)
    print("print empty line")
    print(f"{FR_GREEN}=== That's all for today")

else:
    # something wrong
    print("=== upsssssssss something is wrong ===")
    