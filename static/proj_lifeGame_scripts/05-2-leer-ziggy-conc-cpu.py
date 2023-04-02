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
SLEEP= 0.01

#
# Funciones
#

# Pausa ejecucion
def pausar():
	userInput = input('Presiona ENTER para continuar CTRL-C para salir. ');

# Creo matriz a partir de una archivo si es suministrado
def crear_matriz():
	global nX, nY
	matriz = np.zeros((nX, nY))						# Inicializo la matriz con ceros
	matriz = np.random.randint(2, size=(nX, nY))
	return matriz

# Muestro las 4 Matriz (games)
def show_4_matrix(mat1,mat2,mat3,mat4):
	global nX,nY 
  
	# Ejecuto el comando 'clear' del OS
	os.system('cls') 
	
	X, Y = nX, nY

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
				print(f"\033[0;34m*\033[0m", end ="")
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
				if mat4[x-X-1,y-Y-1] == 1:
					print(f"\033[0;91m{int(mat4[x-X-1,y-Y-1])}\033[0m", end ="")
				else:
					print(f"\033[0;37m{int(mat4[x-X-1,y-Y-1])}\033[0m", end ="")
		print()

#
#  Ejecuto matriz (game) según reglas
#

def exec_game_iter(matriz):
	global nX,xY,msg_text,msg_array,nIter
	
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
	
  # try to control event pf equal matrixes
	if np.array_equal(matriz,matrizTemp):
		mess = 'game reach equality '
		msg_array = np.append(msg_array,mess)
		matriz = 9 * np.ones([nX,nY])
	else:	
		# Copio matrizTemp en matriz para la proxima iteracion
		matriz = np.copy(matrizTemp)
	
	return matriz

# Execute 4 matrixes (games) simultaneously 
def exec_4_game(game):
	global nX, nY, nIter,base_print,msg_text,msg_array

	matriz1 = crear_matriz()
	matriz2 = crear_matriz()
	matriz3 = crear_matriz()
	matriz4 = crear_matriz()

	n=1
	while n<= nIter:	  

		matriz1 = exec_game_iter(matriz1)
		matriz2 = exec_game_iter(matriz2)
		matriz3 = exec_game_iter(matriz3)
		matriz4 = exec_game_iter(matriz4)

		if (n % base_print == 0):
			#show_4_matrix(matriz1,matriz2,matriz3,matriz4)
			print(f"n-> {n} | cpu name {multiprocessing.current_process().name} |  mp name {multiprocessing.Process().name}")
		
		n+=1

	msg_text = msg_text + ' Game ' + str(game)  + ' finished | '
	print(f"Set {game} finished | {nIter} of iterations for each game, total games: 4, total iterat {nIter*4}")

# FUNCTION POOL FOR MULTIPROCESSING  #
######################################
def exec_games(list_g,n_iterat,n_cpu):
	global msg_array
	with multiprocessing.Pool(n_cpu) as pool:
		pool.map(exec_4_game,list_g)


##############################################################
#                         MAIN                               # 
##############################################################

if __name__ == '__main__':

	# COLUMNS & LINES console screen
	# IN WINDOWS DELETE 0 in "...size(0)"
	# nY, nX = os.get_terminal_size(0)		
	# print(f"cols: {os.get_terminal_size(0)[0]} , rows:  {os.get_terminal_size(0)[1]} ")
	# Ajusto por espacios e indicador de iteraciones
	# nX, nY = nX-22, int(nY/2)-1				  

	nX, nY = 180, 800

	# PARAMETERS 

	# number of SET's, each of one of four games (matrixs)
	nGames = int(sys.argv[1])
	# number of iterations in each game
	nIter = int(sys.argv[2])
	# number of CPU in multiprocessing call
	nCPU = int(sys.argv[3])

	# msg_array is for record events like equal matrix iteration
	# msg_text is for record finished game info

	msg_array = []
	msg_text  = 'Games record-> '

	# base_print for control of prints
	base_print = int(nIter/10) 

	# time
	inicio = time.time()

	# parameter for multiporcessing call
	list_games = [(x+1) for x in range(0,nGames)]

	print(f"\n-----Playing LifeGame -----\n ")
	print(f"\n\t.... with matrix of {nX} cols, {nY} rows ")
	print(f"\n\t.... games: {len(list_games)} | iterat: {nIter} | cpu's: {nCPU}\n ")
	pausar()	

	# CALL MULTIPROCESSING
	exec_games(list_games,nIter,nCPU)

	# BALANCE
	print(f"\n----------BALANCE----------\n")

	print(f"Sets executed: {list_games[nGames-1]} | Games executed: {list_games[nGames-1]*4}\n\tEach game (matrix) includes {nIter} iterations of game of life of a matrix with {nX} rows y {nY} cols in one quadrant of the screen,\n\tand only {int(nIter/base_print)} print screens for each game (matrix)")

	print(f"\nmessage: {msg_text}")
	print(f"\nAprox of operations: ???")

	print(f"Duración: {time.time()-inicio}")
