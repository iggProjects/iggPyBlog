#!/usr/bin/python3

#
#  4 Games of life to execute, 1 for each quadrant,  without multiprocessing.
#

import multiprocessing 
import numpy as np
import os, sys, traceback
import time

#
# Constantes
#
ITER = 50 
SLEEP= 0.2

#
# Funciones
#

# Pauso la ejecucion
def pausar():
	userInput = input('Presiona ENTER para continuar CTRL-C para salir. ')

# Muestro la Matriz
def show_4_matrix(mat1,mat2,mat3,mat4):
	# global matriz1,matriz2,matriz3,matriz4
	global nX,nY 

	os.system('cls')                                    # Ejecuto el comando 'clear' del OS
	X, Y = nX, nY				                                  # Dimensiones de la matriz
	# X, Y = matriz.shape                                 # Dimensiones de la matriz
	# matriz_Ext = np.zeros((2*X+1, 2*Y+1))								# Inicializo la matriz con ceros

	for x in range(0, 2*X+1):
		for y in range(0, 2*Y+1):
			# matriz1
			if x<X and y<Y:
				if mat1[x,y] == 1:
					print(f"\033[0;91m{int(mat1[x,y])}\033[0m", end ="")
				else:
					print(f"\033[0;37m{int(mat1[x,y])}\033[0m", end ="")
			#separación entre matrices
			if x == X or y == Y:
				print(f"", end =" ")
			# matriz2		
			if ( x<X ) and ( y > Y ):
				if mat2[x,(y-Y-1)] == 1:
					print(f"\033[0;91m{int(mat2[x,y-Y-1])}\033[0m", end ="")
				else:
					print(f"\033[0;37m{int(mat2[x,y-Y-1])}\033[0m", end ="")
			# matriz3
			if ( x>X ) and ( y<Y ):
				if mat3[x-X-1,y] == 1:
					print(f"\033[0;91m{int(mat3[x-X-1,y])}\033[0m", end ="")
				else:
					print(f"\033[0;37m{int(mat3[x-X-1,y])}\033[0m", end ="")
			#matriz4
			if ( x>X ) and ( y>Y ):
				if mat3[x-X-1,y-Y-1] == 1:
					print(f"\033[0;91m{int(mat4[x-X-1,y-Y-1])}\033[0m", end ="")
				else:
					print(f"\033[0;37m{int(mat4[x-X-1,y-Y-1])}\033[0m", end ="")
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

def exec_game(matriz):
	global nY, nY

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

	return matriz

# Execute 4 simultanous games
def exec_4_game(game):
	global nX, nY, n_iter

	print(f"init game {game}")
	pausar()

	matriz1 = crear_matriz()
	matriz2 = crear_matriz()
	matriz3 = crear_matriz()
	matriz4 = crear_matriz()
	print(f"pasé")
	show_4_matrix(matriz1,matriz2,matriz3,matriz4)

	n = 1
	while n <= n_iter:	  
		matriz1 = exec_game(matriz1)
		matriz2 = exec_game(matriz2)
		matriz3 = exec_game(matriz3)
		matriz4 = exec_game(matriz4)

		show_4_matrix(matriz1,matriz2,matriz3,matriz4)
		time.sleep(SLEEP)
		n+=1

	print(f"finished game {game}")
	pausar()	

# FUNCTION POOL FOR PROCESSING
def exec_games(list_g,n_iterat,n_cpu):
	with multiprocessing.Pool(n_cpu) as pool:
		pool.map(exec_4_game,list_g)

#
#  MAIN
#
# 	
if __name__ == '__main__':

	n = 1  # iteration counter
	#nY, nX = os.get_terminal_size(0)			# LINUX Obtengo COLUMNAS y LINEAS de la consola
	#nY, nX = os.get_terminal_size()			    # WINDOWSObtengo COLUMNAS y LINEAS de la consola
	# print(f"cols: {os.get_terminal_size(0)[0]} , rows:  {os.get_terminal_size(0)[1]} ")
	#nX, nY = nX-22, int(nY/2)-1				  	# Ajusto por espacios e indicador de iteraciones
	nX,nY = 20,20
	# print(nX,nY)

	# pausar()

	# PARAMETERS . number of CPU, number of games, number of iterations
	n_games = int(sys.argv[1])
	n_iter = int(sys.argv[2])
	n_CPU = int(sys.argv[3])
	list_games = [(x+1) for x in range(0,n_games)]

	print(f"\n-----Playing LifeGame -----\n ")
	print(f"\n\t.... with matrix of {nX} cols, {nY} rows ")
	print(f"\n\t.... games: {len(list_games)} | iterat: {n_iter} | cpu's: {n_CPU}\n ")
	pausar()	

	# time
	inicio = time.time()

	# CALL MULTIPROCESSING
	exec_games(list_games,n_iter,n_CPU)

	# BALANCE
	print(f"----------BALANCE----------\n")

	print(f"Games {n_games} of {n_iter} iterations | 4 matrixes of {nX} rows y {nY} cols")

	print(f"Duración: {time.time()-inicio}")
