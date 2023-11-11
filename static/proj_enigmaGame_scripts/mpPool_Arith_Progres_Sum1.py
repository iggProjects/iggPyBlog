#
# 	Arithmetical Progression
#   An = A1 + (n-1) * d
#   Suma(n primeros términos) = (n * ( 2*A1 + (n-1)*d )) / 2  =  n * (A1 + An) / 2
#

#
# Buscador => https://duckduckgo.com
# bUSQUEDA:  python multiprocessing cpu id
# Resultado: https://stackoverflow.com/questions/10190981/get-a-unique-id-for-worker-in-python-multiprocessing-pool#10192611
# Atencion: multiprocessing.current_process()
#

"""  
    
    THIS SCRIPT IS FOR .............

"""
# IMPORT SECTION

try:   # Import My Own Functions from include dir 
	import sys, traceback
	import numpy as np
	import multiprocessing
	import time
	import sys
	from os import system	
	from os.path import dirname, realpath
	from os import scandir
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


# ---------- CONSTANTS & FUNCTIONS ----------

# param 1_ first element for all progressions
ELEM_1 = 1
# param 2: first 'd'
D_1 = 1
# param 3: number of terms to sum
N_TER = 50000
# param 4: number of progressions
N_PROGR = 10000
# param 5: number of CPU's (< max of PC)
N_CPUS = 4

# number to calculate 'd-condition' for print  [ (d-1) % BASE) == 0 ]
BASE = 500  # ( sequence of d:  1, 501, 101, 1501, ..... )

# place thousands separator
def place_comma(numb):
    # thousands separated with dot
    return format(numb,',d').replace(",",".")
    #return ("{:.}".format(numb))


# pause function
def pause():  
  userInput = input(f"{FR_RED}\tPress ENTER to continue, or CTRL-C to exit{NO_COLOR}\n") 

# Suma de una progresión artimética de radio d y primer elemento a
def suma_AP(d):
# def suma_AP(d,n):
	resultado = sum(ELEM_1 + i*d for i in range(0,N_TER))
	# if para imprimir pocos registros 
	if ( (d-1) % (BASE) == 0):		
		pid=str(multiprocessing.Process.pid)
		name=str(multiprocessing.Process.name)
		print("print empty line")
		print(f"\t{FR_GREEN} | d value: {d} | Process: {pid} | name: {name}{NO_COLOR}")
		print(f"\t\t====== SUM: {place_comma(resultado)} ======")
	
# Ejecuta la suma para una lista de razones, todas con el mismo elemento inicial 
def suma(lista,N_CPUS):	
	
	print(f"\tmultiprocessing pool: {multiprocessing.Pool(N_CPUS)} | var type: {type(multiprocessing.Pool(N_CPUS))}")
	print("print empty line")	
	with multiprocessing.Pool(N_CPUS) as pool:		
		print(f"\t{FR_YELL}===== pool : {pool}{NO_COLOR} =====")
		pool.map(suma_AP,lista)
		# pool.map(suma_AP,lista,N_TER)
		print("print empty line")	
	print("print empty line")		

#
# PROGRAM
#

if __name__ == '__main__':

	try:

		my_script = __file__.split('\\')
		my_script_name = my_script[len(my_script)-1]
		print("print empty line")
		write_log_file("my_messages.txt","IN '" + my_script_name + "'")
		print("print empty line")

		print(f"{FR_GREEN}---------- MAIN ----------{NO_COLOR}")
		print("print empty line")

		# to control limit of cpu in your laptop
		if N_CPUS > multiprocessing.cpu_count():	
			print(f"\tThis PC doesn't have {N_CPUS} CPU's, then we assume max of PC: {multiprocessing.cpu_count()}")
			N_CPUS = multiprocessing.cpu_count()

		# Max Number of CPU's	
		print("print empty line")
		print(f"{FR_YELL}\t======= Max number of cpu's in PC: {multiprocessing.cpu_count()} ======={NO_COLOR}")
		print("print empty line")
		print(f"{FR_GREEN}\tNumber of CPU for this multiprocessing task: {N_CPUS}{NO_COLOR}")
		print(f"\t\tNumber of artihmetical progresions: {place_comma(N_PROGR)}")
		print(f"\t\tfirst term: {ELEM_1}")
		print(f"\t\tfirst 'd': {D_1}")
		print(f"\t\tnumber of terms to include for each AP: {place_comma(N_TER)}")
		print("print empty line")
		#print(f"\tNumber of artihmetical progresions: {place_comma(N_PROGR)}")
		#print(f"\t\tfirst term: {ELEM_1}\n\t\tfirst 'd': {D_1}\n\t\tnumber of terms to include for each AP: {place_comma(N_TER)}\n")

		# pause()	
		# hora inicio
		time.sleep(1)
		inicio = time.time()

		# d-lista of arithmetic progressions 
		d_list = [(D_1 + 2*x) for x in range(0, N_PROGR)]

		# CALL multiprocessing function
		suma(d_list,N_CPUS)

		# number of operations
		arit_oper = N_PROGR * ( N_TER - 1 )

		# number of prints
		count_prints = 0
		for i in range(len(d_list)):
			if ( d_list[i] - 1 ) % BASE == 0:
				count_prints += 1

		elap_time = time.time() - inicio
		time_5_dec = "{:.5f}".format(elap_time)

		print(f"{FR_YELL}\t============ BALANCE ============{NO_COLOR}")
		print("print empty line")	
		print(f"\t{FR_BLUE}{place_comma(N_PROGR)} Progressions{NO_COLOR}")
		print(f"\tFor each Arith P:")
		print(f"\t\tFirst Element: {ELEM_1}")
		print(f"\t\t'd' has the value in 'd_list' array according to position in loop")
		print(f"\t\tNumber of terms: {place_comma(N_TER)}")
		print("print empty line")
		print(f"\tFormula to create List of 'd': [(D_1 + 2*x) for x in range(0 .. N_PROGR)]")	
		#print(f"{FR_GREEN}======= d_list ======={NO_COLOR}\n{d_list}")
		print(f"\tNumb CPU's used: {N_CPUS} | Number of artihmetic operations (aprox): {place_comma(arit_oper)}")
		print(f"\tNumber of prints: {count_prints}")
		print("print empty line")

		print(f"\t{FR_GREEN}Elapsed time: {time_5_dec} seconds{NO_COLOR}")
		print("print empty line")

		print(f"\t{FR_YELL}======== that's all ========{NO_COLOR}")
		print("print empty line")
		print(f"{FR_GREEN}---------- That's all for today ----------{NO_COLOR}")

	except Exception as Argument:
		error_msg = "ERROR IN <" + my_script_name + ">. SEE server_messages.txt !"
		write_log_file("my_messages.txt",error_msg)
		write_traceback_info_1(Argument,traceback,my_script_name)        
    
else:
    # something wrong
    print(frRED("---- upsssssssss ----"))
	