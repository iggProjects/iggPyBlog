
# IMPORT SECTION
# My Own Functions from include dir 
try:   # Import My Own Functions from include dir 
	import sys, traceback
	import platform
	import numpy as np 
	from os import system
	from os.path import dirname, realpath
	# import My Own Func
	from MyColors import *
	from MyFunc_copy_DL import *    

except Exception as ImportError:
    FR_RED   = "\033[91m" 
    NO_COLOR = "\033[00m"
    print("print empty line") 
    print(f"{FR_RED}IMPORT ERROR ==>{NO_COLOR} {ImportError} | {ImportError.__class__} | {ImportError.__doc__}")

def mostrar_matriz(matriz,msg):
	X, Y = matriz.shape                                   # Dimensiones de la matriz
	print(f"{FR_GREEN}{msg}")
	print(f"{NO_COLOR}")
	for y in range(0, Y):
		for x in range(0, X):
			print(f"\t{int(matriz[x,y])}", end =" ")
		print()
	print()	# 	
	pause()	


#
# ---------- MAIN ----------
#

if __name__ == "__main__":

	try:

		clear_console_screen()	

		print("\n-------------------------- MAIN -------------------------------------\n")
		print(f"{FR_YELL}\t======= MATRIX WITH NUMPY METHODS   ======={NO_COLOR}\n")

		my_script = __file__.split('\\')
		my_script_name = my_script[len(my_script)-1]
		#print(f".....my_script_name: {my_script_name}")
		print()

		nX, nY = 8, 8

		matriz = np.arange(nX*nY).reshape(nX, nY)
		msg = " Matriz inicial de nX= " + str(nX) + " cols y nY= " + str(nY) + " rows | numpy: matriz = np.arange(nX*nY).reshape(nX, nY) "
		mostrar_matriz(matriz,msg)

		m0 = matriz[ 0:int(nX/2), 0:int(nY/2) ]
		mostrar_matriz(m0, " m0 = matriz[ 0:int(nX/2), 0:int(nY/2) ]")

		m1 = matriz[ int(nX/2):nX, 0:int(nY/2) ]
		mostrar_matriz(m1, " m1 = matriz[ int(nX/2):nX, 0:int(nY/2) ]")

		m2 = matriz[ 0:int(nX/2), int(nY/2):nY ]
		mostrar_matriz(m2," m2 = matriz[ 0:int(nX/2), int(nY/2):nY ]")

		m3 = matriz[ int(nX/2):nX, int(nY/2):nY ]
		mostrar_matriz(m3," m3 = matriz[ int(nX/2):nX, int(nY/2):nY ]")

		der = m1[ [0], : ]
		mostrar_matriz(der, " derecha = m1[ [0], : ]")

		izq = m1[ [int(nX/2)-1], : ]
		mostrar_matriz(izq, " izquierda = m1[ [int(nX/2)-1], : ]")

		m0e = np.vstack( (izq, m0, der) )
		mostrar_matriz(m0e, " m0 expandida fase 1 = np.vstack( (izq, m0, der) )")

		bot = np.vstack(
			( [m3[int(nX/2)-1, 0]], m2[ :, [0] ], [m3[0, 0]] )
		)
		mostrar_matriz(bot, " bot = np.vstack( ( [m3[int(nX/2)-1, 0]], m2[ :, [0] ], [m3[0, 0]] ) )")

		top = np.vstack(
			( [m3[int(nX/2)-1, int(nY/2)-1]], m2[ :, [int(nY/2)-1] ], [m3[0, int(nY/2)-1]] )
		)
		mostrar_matriz(top, " top = np.vstack( ( [m3[int(nX/2)-1, int(nY/2)-1]], m2[ :, [int(nY/2)-1] ], [m3[0, int(nY/2)-1]] ) )")

		m0e = np.hstack( ( top, m0e, bot) )
		mostrar_matriz(m0e, " m0e expandida = np.hstack( ( top, m0e, bot) )")

		print(f"\n{FR_YELL}======== that's all ========{NO_COLOR}\n")
		pause()

	except Exception as Argument:
		error_msg = "ERROR IN <" + my_script_name + ">. SEE server_messages.txt !"
		write_traceback_info(Argument,traceback,my_script_name) 
		pause()       


else:
    # something wrong
    print(frRED("\n---- ******  ----\n"))
    pause()	
