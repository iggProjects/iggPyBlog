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
SLEEP= 0.2
NX = 20
NY = 40
NITER= 500
MSG_TEXT  = 'Games record-> '
BASE_PRINT = int(NITER/10)


#
# Funciones
#

# Pausa ejecucion
def pausar():
	userInput = input('\t ---- Presiona ENTER para continuar CTRL-C para salir ----\n')

def print_args(**kwargs):
	for arg_name in kwargs:
		return kwargs[arg_name], arg_name
	
# Creo matriz a partir de una archivo si es suministrado
def crear_matriz():	
	#print(f"......from crear_matriz() NX: {NX} , NY: {NY}")
	matriz = np.zeros((NX, NY))					 	# Inicializo la matriz con ceros
	matriz = np.random.randint(2, size=(NX, NY))
	return matriz

def mostrar_matriz(matriz):
	#os.system('cls')                                    # Ejecuto el comando 'clear' del OS
	X, Y = matriz.shape                                   # Dimensiones de la matriz
	for x in range(0, X):
		for y in range(0, Y):
			if matriz[x,y] == 1:
				print(f"\033[0;91m{int(matriz[x,y])}\033[0m", end ="")
			else:
				print(f"\033[0;37m{int(matriz[x,y])}\033[0m", end ="")
		print()


# Muestro las 4 Matrices (games)
def show_4_matrix(mat1,mat2,mat3,mat4):
  
	# Ejecuto el comando 'clear' del OS
	#os.system('cls')
	print() 
	
	X, Y = NX, NY

	for x in range(0, 2*X+1):
		for y in range(0, 2*Y+1):
			
			# matriz1  (1er cuadrante)
			if x<X and y<Y:
				if mat1[x,y] == 1:
					print(f"\033[0;91m{int(mat1[x,y])}\033[0m", end ="")
				else:
					print(f"\033[0;37m{int(mat1[x,y])}\033[0m", end ="")
			
			#separación entre matrices 1 y 2
			if y == Y:
				print(f"\033[0;34m\033[0m", end =" ")
			
			# matriz2	(2do cuadrante)	
			if ( x<X ) and ( y > Y ):
				if mat2[x,(y-Y-1)] == 1:
					print(f"\033[0;91m{int(mat2[x,y-Y-1])}\033[0m", end ="")
				else:
					print(f"\033[0;37m{int(mat2[x,y-Y-1])}\033[0m", end ="")

			# línea entre matrices 1 y 2 con 3 y 4
			if x == X:
				print(f"\033[0;34m\033[0m", end =" ")
			
			# matriz3 (3er cuadrante)
			if ( x>X ) and ( y<Y ):
				if mat3[x-X-1,y] == 1:					
					print(f"\033[0;91m{int(mat3[x-X-1,y])}\033[0m", end ="")
				else:					
					print(f"\033[0;37m{int(mat3[x-X-1,y])}\033[0m", end ="")	

			#matriz4 (4to cuadrante)
			if ( x>X ) and ( y>Y ):
				if mat4[x-X-1,y-Y-1] == 1:
					print(f"\033[0;91m{int(mat4[x-X-1,y-Y-1])}\033[0m", end ="")
				else:
					print(f"\033[0;37m{int(mat4[x-X-1,y-Y-1])}\033[0m", end ="")
			
		print()
		#time.sleep(SLEEP)

#
#  Ejecuto matriz (game) según reglas
#

def exec_game_iter(matriz,name):
	
	# Copio la matriz para poner en ella los cambios
	matrizTemp = np.copy(matriz)

	# Recorro la matriz para aplicar reglas a la matrizTemp
	for x in range(0, NX):
		for y in range(0, NY):
			# Numero de Vecinos
			nVecinos = matriz[	(x-1)%NX, (y-1)%NY ] 		\
							 + matriz[	(x)%NX, 	(y-1)%NY ] 		\
							 + matriz[	(x+1)%NX, (y-1)%NY ] 		\
							 + matriz[	(x-1)%NX, (y)%NY ] 			\
							 + matriz[	(x+1)%NX, (y)%NY ] 			\
							 + matriz[	(x-1)%NX, (y+1)%NY ] 		\
							 + matriz[	(x)%NX, 	(y+1)%NY ] 		\
							 + matriz[	(x+1)%NX, (y+1)%NY ]

			# Regla 1: celda muerta (0) con 3 vecinas revive (1)
			if matriz[x,y] == 0 and nVecinos == 3:
				matrizTemp[x,y] = 1
			
			# Regla 2: celda viva (1) con mas de 3 vecinas o menos de 2 muere (2)
			elif matriz[x,y] == 1 and ( nVecinos < 2 or nVecinos > 3 ):
				matrizTemp[x,y] = 0
	
  # try to control event pf equal matrixes
	if np.array_equal(matriz,matrizTemp):
		if multiprocessing.current_process().name == "SpawnPoolWorker-1":
			#mostrar_matriz(matriz)
			print(f"\t\033[0;93cpu name {multiprocessing.current_process().name} - process {multiprocessing.Process().name} ==> game reach equality with matriz {name} ===\033[0m")
		matriz = 9 * np.ones([NX,NY])
	else:	
		# Copio matrizTemp en matriz para la proxima iteracion
		matriz = np.copy(matrizTemp)
	
	return matriz

# Execute 4 matrixes (games) simultaneously 
def exec_4_game(game):
	
	print(f"Set-> {game} | cpu name {multiprocessing.current_process().name} |  mp name {multiprocessing.Process().name}\n")
	 
	matriz1 = crear_matriz()
	matriz2 = crear_matriz()
	matriz3 = crear_matriz()
	matriz4 = crear_matriz()

	n=1
	while n <= NITER:	  
	# while n<= nIter or [CONDICION DE MATRIZ IDENTICA ENTRE DOS ITER]:	  

		matriz1 = exec_game_iter(matriz1,'matriz1')
		matriz2 = exec_game_iter(matriz2,'matriz2')
		matriz3 = exec_game_iter(matriz3,'matriz3')
		matriz4 = exec_game_iter(matriz4,'matriz4')

		if ( (multiprocessing.current_process().name == "SpawnPoolWorker-1") and (n % BASE_PRINT == 0) ):
			print(f"\033[0;93mPrinting only for cpu name {multiprocessing.current_process().name} - mp process {multiprocessing.Process().name} | iteration-> {n}\033[0m")
			show_4_matrix(matriz1,matriz2,matriz3,matriz4)
			time.sleep(SLEEP)			
		n+=1

	print(f"\033[0;93m\n{multiprocessing.current_process().name} ===> Set {game} finished\033[0m | {NITER} of iterations for each game | total games: 4, total iterat {NITER*4}")
	
	#return n


# FUNCTION POOL FOR MULTIPROCESSING  #
######################################
def exec_games(list_g,n_cpu):
	
	#print(f"\n......from exec_games() NX: {NX} , NY: {NY}\n\n")
	with multiprocessing.Pool(n_cpu) as pool:
		pool.map(exec_4_game,list_g)


##############################################################
#                         MAIN                               # 
##############################################################

# COLUMNS & LINES console screen
# NY, NX = os.get_terminal_size(0)		
# print(f"cols: {os.get_terminal_size(0)[0]} , rows:  {os.get_terminal_size(0)[1]} ")
# Ajusto por espacios e indicador de iteraciones
# NX, NY = NX-22, int(NY/2)-1				  

if __name__ == '__main__':

	os.system('cls')

	# READ PARAMETERS 
	# number of SET's, each of one of four games (matrixs)
	nSets = int(sys.argv[1])
	# number of CPU in multiprocessing call
	nCPU = int(sys.argv[2])


	# parameter for multiporcessing call
	list_games = [(x+1) for x in range(0,nSets)]

	print(f"\n\033[0;93m----------- Starting Life Game Series ----------- \033[0m\n ")
	print(f"\t.... Number of Sets of 4 simultaneous 'life game' (matrix): {len(list_games)}\n\t.... Iterations for each game: {NITER}\n\t.... number of cpu's participating: {nCPU} ....")
	print(f"\t.... matrices of {NX} cols, {NY} rows ....")
	print(f"\t.... Printing only for first process ....\n")
	#print(f"\t{list_games}")
	pausar()	
	# time
	inicio = time.time()


	# CALL MULTIPROCESSING
	exec_games(list_games,nCPU)

	# BALANCE
	print(f"\n\033[0;93m ----------BALANCE----------\033[0m\n")
	print(f"\tNumber of cpu's participating: {nCPU}")
	print(f"\tSets executed: {list_games[nSets-1]}\n\tGames executed: {list_games[nSets-1]*4}")
	print(f"\tEach game (matrix) includes {NITER} iterations of game of life\n\t\twith a matrix of {NX} x {NY} in each quadrant of the screen,\n\t\tand only {int(NITER/BASE_PRINT)} print screens for each game (matrix)\n\t\tof the first process")
	#print(f"\tAprox of operations: ???")
	
	elapsed_time = "{:.2f}".format(time.time()-inicio)
	print(f"\tElapsed Time: {elapsed_time} seconds")
	print(f"\n\033[0;93m ----------THAT's ALL----------\033[0m\n")
