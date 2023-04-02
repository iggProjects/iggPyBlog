#!/usr/bin/python3


import numpy as np
import os, sys, traceback
import time

#
# Constantes
#
ITERAC = 100 
DORMIR= 0.05

#
# Funciones
#

# Pauso la ejecucion
def pausar():
	userInput = input('Presiona ENTER para continuar CTRL-C para salir. ');

# Muestro la Matriz
def mostrar_matriz(matriz):
	os.system('cls')                                    # Ejecuto el comando 'clear' del OS
	X, Y = matriz.shape                                   # Dimensiones de la matriz
	for x in range(0, X):
		for y in range(0, Y):
			if matriz[x,y] == 1:
				print(f"\033[0;91m{int(matriz[x,y])}\033[0m", end =" ")
			else:
				print(f"\033[0;37m{int(matriz[x,y])}\033[0m", end =" ")
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
	global nX, nY

	n=1																	# Counter Iteraciones

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
		mostrar_matriz(matriz)
		print(f"Iteraciones: {n} de {ITERAC} ({nX}, {nY})")
		time.sleep(DORMIR)
		n+=1

#
#  MAIN
#	

nY, nX = os.get_terminal_size(0)		# Obtengo COLUMNAS y LINEAS de la consola
# print(f"cols: {os.get_terminal_size(0)[0]} , rows:  {os.get_terminal_size(0)[1]} ")
nX, nY = nX-20, int(nY/4)-1				  	# Ajusto por espacios e indicador de iteraciones

matriz = crear_matriz()

ejecutar_matriz(matriz)
