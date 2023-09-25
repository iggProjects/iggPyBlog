"""
 MY FUNCTIONS FOR:

   - see objects types, methods and attributes,
   - view objectS info in matrix form
   - time functions like pause, ......  
   - printing colors options
   - decisions functions
   - use HELP function
   - write in log files, like "comments log", "errors log"
   - OS most used functions
   - MODULES info

"""
#
# IMPORT LIBRERIES OR YOUR OWN FUNCTIONS 
#

# to write in log files
import datetime
from os.path import dirname
# import logging configuration
from static.include.config_logging import *
# import My own colors
from static.include.MyColors import *

# function to write in logFile
def write_log_file(logFile,msg):

    try:
        # path to log file
        up2_dir = dirname(dirname(__file__))
        logFile_path = up2_dir + "/logFiles/" + logFile
        # creating/opening a file
        f = open(logFile_path, "a") 
        # write in file        
        f.write('%s | %s\n' % (datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3],msg))      
        # close file
        f.close()
    except Exception as Argument:
        print(f"Error {Argument}")
        logging.exception(f"{Argument} | exception from 'write_log_file()' ")

def write_traceback_info(Argum,TraceList,script): 
               
        traceback_formatted = TraceList.format_exc().replace('"','').replace(',',' | ')
        traceback_lines = traceback_formatted.split('\n')
        print("print empty line")        
        print(frRED(f"====================== ERROR FOUND ======================"))
        print("print empty line")
        for line in traceback_lines:
            #if ('File' or 'line' or 'Module') in line:
            if 'line' in line:
                for field in line.split('|'):
                   if 'line' in field:
                      line_numb = field

        print(frRED(f"FILE: <{script}>"))
        print("print empty line")
        print(f"\t{FR_GREEN}code in{line_numb}:{traceback_lines[len(traceback_lines)-3]}{NO_COLOR}")        
        print(f"\t{FR_BLUE}{Argum} | {Argum.__class__} | {Argum.__doc__}{NO_COLOR}")
        print("print empty line")

        """
        for line in traceback_lines:
            if ('File' or 'line') in line:
                print(f"{line}")  


        print("print empty line")
        print(f"{FR_BLUE}===> {Argum} | {Argum.__class__} | {Argum.__doc__} <==={NO_COLOR}")
        print("print empty line")
        """
        print(frRED(f"\t\tSEE 'server_messages.txt' file OR Contact Web Admin !"))
        logging.exception(f"{Argum} | exception from '0-prototype-colors.py()': ")

def write_traceback_info_1(Argum,TraceList,script): 
               
        traceback_formatted = TraceList.format_exc().replace('"','').replace(',',' | ')
        traceback_lines = traceback_formatted.split('\n')
        print()        
        print(frRED(f"====================== ERROR FOUND ======================"))
        print()
        print()
        for line in traceback_lines:
            #if ('File' or 'line' or 'Module') in line:
            if 'line' in line:
                for field in line.split('|'):
                   if 'line' in field:
                      line_numb = field

        print(frRED(f"FILE: <{script}>"))
        print()
        print(f"\t{FR_GREEN}code in{line_numb}:{traceback_lines[len(traceback_lines)-3]}{NO_COLOR}")        
        print(f"\t{FR_BLUE}{Argum} | {Argum.__class__} | {Argum.__doc__}{NO_COLOR}")
        print()
        print(frRED(f"===> SEE 'server_messages.txt' file OR Contact Web Admin !"))
        print()
        logging.exception(f"{Argum} | exception from '0-prototype-colors.py()': ")


#
# TIME FUNCTIONS
#

# pause function
def pause():  
  userInput = input(f"{FR_MAG}Press ENTER to continue, or CTRL-C to exit{NO_COLOR}\n")  
        
#
# DECISIONS FUNCTIONS
#        

def Y_N(msg):       
    ans=str(input(msg))    
    if ans == 'Y' or ans == 'N': 
        return ans        
    else:
        Y_N(msg)

def Y_N_1(msg):        
    ans=str(input(msg))    
    if ans == 'Y':         
        return 'Y'        
    elif ans == 'N':
        return 'N'
    else:
        Y_N(msg)

def Y_N_2(msg):
    return str(input(msg))

#
# PRINT VARS 
#

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
      print(f"line: {str(i+1).rjust(3)} --> {line}")
      line=[]  
  else:
    print(frRED(f"\nWarning FROM matrix_view(): Object '{obj_l_t}' in not list neither tupla !\n" )) 

#
# SHOW LIBRARY INFO
#

# List Library Methods
# search name of module to abbreviate the print info
def library_methods(my_lib):
  for method in dir(my_lib):
    LIB_method = method
    print(f"{FR_GREEN}{str(my_lib)}.method --> {NO_COLOR}´{LIB_method}")
  print()  

#
# SHOW OBJECTS INFO
#

# Show attributes and methods avalaible for "obj"
def mostrar(obj):      

  if type(obj) in ['list','dict']:
    print(f"Object elements view in matrix form (6 columns by row)\n")
    matrix_view(obj,6)

  # obj type and mem dir
  print(f"Object type is {type(obj)} and mem dir is: {id(obj)}\n")
  # obj attributes
  # attributes = [attr for attr in dir(obj) if not attr.startswith('__')]
  attr_meth = [attr for attr in dir(obj)]
  # print attributes and methods in matrix form
  print(f"Object assigned attributes and methods are:\n")
  matrix_view(attr_meth,6)
  print()
  prBG("-----------------END MOSTRAR OBJECT TYPE AND ATTRIB-METHODS-----------------",17)    
  print()
  
# Show elements looking at dir(obj)
def ver_objetos(obj):
	enum=1
	si_color='\033[0;91m'
	no_color='\033[0m'
	print(si_color + 'TIPO:' + no_color, str(type(obj)) , '\n')
	for elemento in dir(obj):
		ver='obj.' + elemento
		print(str(si_color + 'Elemento: ' + str(enum) + ' ' + no_color + ver))
		if 'method' in str(eval(ver)):
			print('\tMetodo --> ', eval(ver))
		else:
			print('\tAtribu --> ', eval(ver))
			print('\tTipo --> ', type(eval(ver)), '\n')
		enum=enum+1


# More specific info for objects
def ver_elementos(obj, todo=True):
  enum=1
  print_count = 1
  si_color='\033[0;91m'
  no_color='\033[0m'
  # Coloreado Purpura \033[0;95m
  numb_elem=len(dir(obj))
  #print(f"object '{obj}' type '{type(obj)}' has {numb_elem} elements") 
  print(si_color + 'TIPO: ' + no_color + str(type(obj)) + '\n')
  print(si_color + 'DOC: ' + no_color + type(obj).__doc__ + '\n')
  
  for elemento in dir(obj):
    if todo == False and '_' in elemento:
      pass
    else:
      ver='obj.' + elemento      
      # Coloreado Rojo \033[0;91m
      si_color='\033[0;91m'
      print(si_color + 'Elemento ' + str(enum) + ': ' + no_color + ver + ' || '+ str(eval(ver)))      
      if 'method' in str(eval(ver)):
        # Coloreado Amarillo \033[0;93m
        si_color='\033[0;93m'
        descripcion='Metodo'
      elif 'function' in str(eval(ver)):
        # Coloreado Azul \033[0;94m
        si_color='\033[0;94m'
        descripcion='Funcion'
      elif 'class' in str(eval(ver)):
        # Coloreado Cyan \033[0;96m
        si_color='\033[0;96m'
        descripcion='Clase '
      else:
        # Coloreado Verde \033[0;92m
        si_color='\033[0;92m'
        descripcion='Atribu'

      print(si_color + descripcion + ' --> ' + no_color + str(eval(ver)) )
      print(si_color + 'Tipo   --> ' + no_color + str(type(eval(ver))) )
      print(si_color + 'Doc    --> ' + no_color + str(eval(ver).__doc__) + '\n')
      enum=enum+1
      print_count += 1
      if print_count == 11:
          print_count = 1
          pause()

def help_obj_method(obj):
    print(help(type(obj)))    

def desc_obj_method(obj,todo=True):
    
    method_founded = False
    enum=1
    print_count = 1
    si_color = '\033[0;91m'
    no_color = '\033[0m'
    descripcion = ''
    ver = ''
    print(si_color + 'TIPO: ' + no_color + str(type(obj)) + '\n')
    print(si_color + 'DOC: ' + no_color + type(obj).__doc__ + '\n')
    
    obj_method = str(input(frRED(f"what method of object '{obj}' you want to see?" )))
    #obj_method = str(input(Colors.frRED(f"what method of object '{obj}' you want to see?" )))
    print()
    #obj_method = str(input(f"what method of object '{obj}' you want to see? "))
    #print(Colors.frGREEN(f"\n\tobj method selected --> '{obj_method}'\n"))

    for elemento in dir(obj):
      if todo == False and '_' in elemento:
        pass
      else:       
        #print(f"\nelemento: {elemento} -- type {type(elemento)}\n")  
        #if obj_method in dir(elemento):
        if obj_method in elemento:     
          method_founded = True     
          ver='obj.' + elemento      
          # Coloreado Rojo \033[0;91m
          si_color='\033[0;91m'
          
          if 'method' in str(eval(ver)):
            # Coloreado Amarillo \033[0;93m
            si_color='\033[0;93m'
            descripcion='Metodo'
          elif 'function' in str(eval(ver)):
            # Coloreado Azul \033[0;94m
            si_color='\033[0;94m'
            descripcion='Funcion'
          elif 'class' in str(eval(ver)):
            # Coloreado Cyan \033[0;96m
            si_color='\033[0;96m'
            descripcion='Clase '
          else:
            # Coloreado Verde \033[0;92m
            si_color='\033[0;92m'
            descripcion='Atribu'

          #Colors.frGREEN(f"elemento {str(enum)}: {str(eval(ver))} \n")
          print(si_color + str(enum) + ': ' + ver + no_color + '\n')        
          # print(si_color + str(enum) + ': ' + ver + ' || ' + str(eval(ver)) + no_color + '\n')        
          print(si_color +  descripcion + ' --> ' + no_color + str(eval(ver)) )
          print(si_color +  'Tipo   --> ' + no_color + str(type(eval(ver))) )
          print(si_color +  'Doc    --> ' + no_color + str(eval(ver).__doc__) + '\n')
          enum=enum+1
          print_count += 1
          if print_count == 11:
              print_count = 1
              pause()

        else: 
           pass          
    
    if not method_founded:      
      print(frRED("\nthere is no such method 🙄\n"))
      #print(Colors.frRED("\nthere is no such method 🙄\n"))

# checking related classes in a composite class 
def relatedClasses(clas):   

    print(f"----- analysis of related classes with class {clas} -----")
    for clas_rel in clas.__mro__:
        print(f"{FR_GREEN}\trelated class --> {clas_rel}\n")
    print(f"{NO_COLOR}----- end analysis -----\n")    


# Print Exception Hierrachy
def classtree(cls, indent=0):
    print('.' * indent, cls.__name__)
    for subcls in cls.__subclasses__():
        classtree(subcls, indent + 3)

#
#  LOG FILES FUNCTIONS
#


#
#  OS FUNCTIONS
#
