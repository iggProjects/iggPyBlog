#!/usr/bin/python3
import numpy as np
import multiprocessing as mp
import sys

##############################################################
#                         FUNC                               #
##############################################################

#
#  Ejecuto matriz (game) según reglas
#
def exec_game_iter(matriz):
	# Hacer lo que quieras hacer con las matrices y las reglas
	return matriz


#
# Ejecuta las matrices individuales, en exec_games paso la lista, no tengo porque crearlas aqui.
# en este caso game debe ser la matriz a ejecutar.
#
def exec_4_games(game):
	global n_iter
	n=1
	game_comp = crear_matriz()					# Uso la funcion crear_matriz para que la matriz de comparacion tenga las 
																			# mismas caracteristicas
	while n <= n_iter: 
		game_comp = exec_game_iter(game)
		if game == game_comp:							# Comparo las matrices, si son iguales rompo el bucle
			break
		else:
			game = game_comp								# Preparo la matriz para la siguiente iteracion
		n+=1

	return n														# Retorno el numero de iteraciones completas hasta que se cumple la comparacion 
																			# de matrices

#
# Pool para MP
#
def exec_games(list_games, n_cpu):
	with mp.Pool(n_cpu) as pool:
		return pool.map(exec_4_games, list_games)			# Al terminar todos los procesos retorna una lista con los Ns
																									# de cada proceso

##############################################################
#                         MAIN                               #
##############################################################
# number of iterations in each game
nIter = int(sys.argv[1])

matriz1 = crear_matriz()
matriz2 = crear_matriz()
matriz3 = crear_matriz()
matriz4 = crear_matriz()

# Llamo a MP
exec_games([matriz1, matriz2, matriz3, matriz4], 4)


