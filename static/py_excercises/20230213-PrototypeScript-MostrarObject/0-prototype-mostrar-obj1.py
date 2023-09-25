
"""  
THIS SCRIPT IS FOR..................

"""
# IMPORT SECTION
try:   # Import My Own Functions from include dir 
    import sys, traceback     
    from os.path import dirname, realpath
    # get parent up 2 from __file__ path: 'static path'   
    up2_dir = dirname(dirname(dirname(realpath(__file__))))
    # insert path in sys.path
    sys.path.append(up2_dir)
    # get parent up 3 from __file__ path: 'static parent path'       
    up3_dir = dirname(dirname(dirname(dirname(realpath(__file__)))))
    # insert path in sys.path
    sys.path.append(up3_dir)
    # import My Own Func
    from static.include.MyFunc import *
    from static.include.MyColors import *
except Exception as ImportError:
    FR_RED   = "\033[91m" 
    NO_COLOR = "\033[00m"
    print("print empty line") 
    print(f"{FR_RED}IMPORT ERROR ==>{NO_COLOR} {ImportError} | {ImportError.__class__} | {ImportError.__doc__}")

"""
# CONSTANTS FOR COLORS
NO_COLOR = "\033[00m"
FR_RED   = "\033[91m"
FR_GREEN = "\033[92m"
FR_YELL  = "\033[93m"
FR_BLUE  = "\033[94m"
FR_MAG   = "\033[95m"
"""
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
          line.append(obj_l_t[i*n_cols+j])
      print(f"\t{NO_COLOR}line: {i+1} => {' ; '.join(line)}")
      line=[]  
  else:
    print("Warning FROM matrix_view(): Object '{obj_l_t}' in not  list neither tupla !" ) 

# Show attributes and methods avalaible for "obj"
def mostrar(obj):      

  if 'list' in str(type(obj)) or 'tuple' in str(type(obj)):
    print(f"{FR_BLUE}Object elements view in matrix form (4 columns by row)")
    matrix_view(obj,4)

  print("print empty line")
  # obj type and mem dir
  print(f"Object type is {type(obj)} and mem dir is: {id(obj)}")
  print("print empty line")
  # obj attributes
  # attributes = [attr for attr in dir(obj) if not attr.startswith('__')]
  attr_meth = [attr for attr in dir(obj)]
  # print attributes and methods in matrix form
  print(f"{FR_BLUE}Object assigned attributes and methods are:")
  matrix_view(attr_meth,8)
  print("print empty line")
  print("=== END 'MOSTRAR' OBJECT TYPE AND ATTRIB-METHODS")    
  print("print empty line")


#
# ---------- MAIN ----------
#

if __name__ == "__main__":

    try:
       	# get name of script
        my_script = __file__.split('\\')
        my_script_name = my_script[len(my_script)-1]
        write_log_file("my_messages.txt","IN '" + my_script_name + "'")
        print("print empty line")
        print(f"{FR_GREEN}=== MAIN")
        print("print empty line")
        print(f"{FR_BLUE}=== Show Object Info")
        print("print empty line")        
        print(f"{FR_BLUE}Object: variable 'colors_str' = ['\\033[91m - Red' ; '\\033[92m - Green' ; '\\033[93m - Yellow' ; '\\033[94m - Blue' ; '\\033[95m - Magenta']")
        colors_str=['\\033[91m - Red','\\033[92m - Green','\\033[93m - Yellow','\\033[94m - Blue','\\033[95m - Magenta']
        print("print empty line")
        mostrar(colors_str)            
        print(f"{FR_GREEN}=== That's all for today")

    except Exception as Argument:
        error_msg = "ERROR IN <" + my_script_name + ">. SEE server_messages.txt !"
        write_log_file("my_messages.txt",error_msg)
        write_traceback_info(Argument,traceback,my_script_name)        

    
else:
    # something wrong
    print("=== upsssssssss something is wrong  ===")
    