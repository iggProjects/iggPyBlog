#
# One Game of Life executed in four quadrants, one at a time, without multiprocessint
#

"""  
    
    THIS SCRIPT IS FOR .............

"""
"""  
    
    THIS SCRIPT IS FOR .............

"""
# IMPORT SECTION
# My Own Functions from include dir 
try:   # Import My Own Functions from include dir 
	import sys, traceback, time
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

#
# CONSTANTS
#
ITERAC = 20 
DORMIR= 0.5

#
# FUNC
#

# Pauso la ejecucion
def pausar():
	userInput = input('Presiona ENTER para continuar CTRL-C para salir. ');

# Muestro la Matriz
def mostrar_matriz(matriz,loc):
	clear_console_screen()
	X, Y = matriz.shape                                 # Dimensiones de la matriz
	matriz_Ext = np.zeros((2*X+1, 2*Y+1))				# Inicializo la matriz con ceros
	print(f"\n{FR_BLUE}ITERACIÓN {n} \ ROTANDO MATRIZ de 0 y 1 POR CUADRANTE{NO_COLOR}")
	if loc == 1:
		for x in range(0, 2*X+1):
			for y in range(0, 2*Y+1):
				if x<X and y<Y:
					if matriz[x,y] == 1:
						print(f"\033[0;91m{int(matriz[x,y])}\033[0m", end ="")
					else:
						print(f"\033[0;37m{int(matriz[x,y])}\033[0m", end ="")
				else:
					if x == X or y == Y:
						print(f"", end =" ")
					else:	
						print(f"\033[0;37m{int(matriz_Ext[x,y])}\033[0m", end ="")
			print()
	
	if loc == 2:
		for x in range(0, 2*X+1):
			for y in range(0, 2*Y+1):
				if x<X and y<Y:
					print(f"\033[0;37m{int(matriz_Ext[x,y])}\033[0m", end ="")
				if x == X or y == Y:
					print(f"", end =" ")
				if ( x<X ) and ( y > Y ):
					if matriz[x,(y-Y-1)] == 1:
						print(f"\033[0;91m{int(matriz[x,y-Y-1])}\033[0m", end ="")
					else:
						print(f"\033[0;37m{int(matriz[x,y-Y-1])}\033[0m", end ="")
				if ( x>X ) and ( y<Y ):
					print(f"\033[0;37m{int(matriz_Ext[x-X-1,y])}\033[0m", end ="")
				if ( x>X ) and ( y>Y ):
					print(f"\033[0;37m{int(matriz_Ext[x-X-1,y-Y-1])}\033[0m", end ="")
			print()

	if loc == 4:
		for x in range(0, 2*X+1):
			for y in range(0, 2*Y+1):
				if x<X and y<Y:
					print(f"\033[0;37m{int(matriz_Ext[x,y])}\033[0m", end ="")
				if x == X or y == Y:
					print(f"", end =" ")
				if ( x<X ) and ( y > Y ):
					print(f"\033[0;37m{int(matriz_Ext[x,y-Y-1])}\033[0m", end ="")
				if ( x>X ) and ( y<Y ):
					if matriz[x-X-1,y] == 1:
						print(f"\033[0;91m{int(matriz[x-X-1,y])}\033[0m", end ="")
					else:
						print(f"\033[0;37m{int(matriz[x-X-1,y])}\033[0m", end ="")
				if ( x>X ) and ( y>Y ):
					print(f"\033[0;37m{int(matriz_Ext[x-X-1,y-Y-1])}\033[0m", end ="")
			print()

	if loc == 3:
		for x in range(0, 2*X+1):
			for y in range(0, 2*Y+1):
				if x<X and y<Y:
					print(f"\033[0;37m{int(matriz_Ext[x,y])}\033[0m", end ="")
				if x == X or y == Y:
					print(f"", end =" ")
				if ( x<X ) and ( y > Y ):
					print(f"\033[0;37m{int(matriz_Ext[x,y-Y-1])}\033[0m", end ="")
				if ( x>X ) and ( y<Y ):
					print(f"\033[0;37m{int(matriz_Ext[x-X-1,y])}\033[0m", end ="")
				if ( x>X ) and ( y>Y ):
					if matriz[x-X-1,y-Y-1] == 1:
						print(f"\033[0;91m{int(matriz[x-X-1,y-Y-1])}\033[0m", end ="")
					else:
						print(f"\033[0;37m{int(matriz[x-X-1,y-Y-1])}\033[0m", end ="")
			print()


# Creo matriz a partir de una archivo si es suministrado
def crear_matriz():
	global nX, nY
	matriz = np.zeros((nX, nY))					# Inicializo la matriz con ceros
	matriz = np.random.randint(2, size=(nX, nY))
	return matriz

#
#  Ejecuto matriz según reglas
#

def ejecutar_matriz(matriz):
	global n, nX, nY

	# Iteraciones del programa
	while n <= ITERAC:
		# Copio la matriz para poner en ella los cambios
		matrizTemp = np.copy(matriz)

		# Recorro la matriz para aplicar reglas a la matrizTemp
		for x in range(0, nX):
			for y in range(0, nY):
				# Numero de Vecinos
				nVecinos = matriz[	(x-1)%nX, (y-1)%nY ] 		\
								 + matriz[	(x)%nX, 	(y-1)%nY ] 		\
								 + matriz[	(x+1)%nX, (y-1)%nY ] 		\
								 + matriz[	(x-1)%nX, (y)%nY ] 			\
								 + matriz[	(x+1)%nX, (y)%nY ] 			\
								 + matriz[	(x-1)%nX, (y+1)%nY ] 		\
								 + matriz[	(x)%nX, 	(y+1)%nY ] 		\
								 + matriz[	(x+1)%nX, (y+1)%nY ]

				# Regla 1: celda muerta (0) con 3 vecinas revive (1)
				if matriz[x,y] == 0 and nVecinos == 3:
					matrizTemp[x,y] = 1

				# Regla 2: celda viva (1) con mas de 3 vecinas o menos de 2 muere (2)
				elif matriz[x,y] == 1 and ( nVecinos < 2 or nVecinos > 3 ):
					matrizTemp[x,y] = 0

		# Copio matrizTemp en matriz para la proxima iteracion
		matriz = np.copy(matrizTemp)

		# Muestro la nueva cara de la matriz
		mostrar_matriz(matriz,1)
		time.sleep(DORMIR)
		n+=1
		mostrar_matriz(matriz,2)
		time.sleep(DORMIR)
		n+=1
		mostrar_matriz(matriz,3)
		time.sleep(DORMIR)
		n+=1
		mostrar_matriz(matriz,4)
		time.sleep(DORMIR)
		n+=1

#
#  MAIN
#	

if __name__ == "__main__":
	
	try:

		clear_console_screen()

		my_script = __file__.split('\\')
		my_script_name = my_script[len(my_script)-1]

		n = 1  										# iteration counter
		#nY, nX = os.get_terminal_size(0)			# Linux Obtengo COLUMNAS y LINEAS de la consola
		#nY, nX = os.get_terminal_size()		    # Windows Obtengo COLUMNAS y LINEAS de la consola
		#print(f"cols: {os.get_terminal_size()[0]} , rows:  {os.get_terminal_size()[1]} ")

		#nX, nY = int(nX/2) -10 , int(nY/3) - 20	# Ajusto por espacios e indicador de iteraciones

		#print(f"\n\033[0;93mTERMINAL SIZE: {os.get_terminal_size()[0]} x {os.get_terminal_size()[1]} |  MATRIX SIZE: {nX} x {nY}\033[0m\n")
		nX= 15
		nY=40
		print(f"\n\033[0;93mMATRIX SIZE: {nX} x {nY}\033[0m\n")

		pausar()

		inicio = time.time()

		matriz = crear_matriz()

		ejecutar_matriz(matriz)

		print(f"\n{FR_YELL}-----------BALANCE--------------{NO_COLOR}\n")
		print(f"Duración: {time.time()-inicio}")
		print(f"Iteraciones: {n-1} de {ITERAC} | 4 matrices de {nX} filas y {nY} columnas")
		print()

	except Exception as Argument:
		error_msg = "ERROR IN <" + my_script_name + ">. SEE server_messages.txt !"
		write_traceback_info(Argument,traceback,my_script_name)
		pause()     
    
else:
    # something wrong
    print(frRED("---- upsssssssss something is wrong ----"))