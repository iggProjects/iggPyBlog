
"""  
THIS SCRIPT IS FOR..................

"""
# IMPORT SECTION
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
    lines=[]
    line=[]
    i=0
    for i in  range(matrix_rows):    
      for j in range(n_cols):
        if i*n_cols+j<len(obj_l_t):
          line.append(obj_l_t[i*n_cols+j])
      print(f"line: {i+1} --> {line}")
      line=[]  
  else:
    print("\nWarning FROM matrix_view(): Object '{obj_l_t}' in not  list neither tupla !\n" ) 

# Show attributes and methods avalaible for "obj"
def mostrar(obj):      

  if 'list' in str(type(obj)) or 'tuple' in str(type(obj)):
    print(f"Object elements view in matrix form (8 columns by row)\n")
    matrix_view(obj,4)

  # obj type and mem dir
  print(f"Object type is {type(obj)} and mem dir is: {id(obj)}\n")
  # obj attributes
  # attributes = [attr for attr in dir(obj) if not attr.startswith('__')]
  attr_meth = [attr for attr in dir(obj)]
  # print attributes and methods in matrix form
  print(f"Object assigned attributes and methods are:\n")
  matrix_view(attr_meth,8)
  print()
  print("-----------------END MOSTRAR OBJECT TYPE AND ATTRIB-METHODS-----------------")    
  print()


#
# ---------- MAIN ----------
#

if __name__ == "__main__":

    #system('cls')

    print(f"\n{FR_GREEN}---------- main ----------\n")
    print(f"\n{FR_BLUE}--------------- Show Object Info --------------\n")
    
    print("colors_str = ['\\033[91m - Red','\\033[92m - Green','\\033[93m - Yellow','\\033[94m - Blue','\\033[95m - Magenta']\n")
    print("print colors_str attributes\n")
    colors_str=['\\033[91m - Red','\\033[92m - Green','\\033[93m - Yellow','\\033[94m - Blue','\\033[95m - Magenta']
    mostrar(colors_str)            

    print(f"\n{FR_GREEN}---------- That's all for today ----------{NO_COLOR}\n")

    
else:
    # something wrong
    print("\n---- upsssssssss something is wrong  ----\n")
    