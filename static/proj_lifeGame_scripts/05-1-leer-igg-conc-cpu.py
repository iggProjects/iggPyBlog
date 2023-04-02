#!/usr/bin/python3

#
# One Game of Life executed in four quadrants, one at a time, without multiprocessint
#

import numpy as np
import os, sys, traceback
import time

#
# Constantes
#
ITERAC = 50 
DORMIR= 0.5

#
# Funciones
#

# Pauso la ejecucion
def pausar():
	userInput = input('Presiona ENTER para continuar CTRL-C para salir. ');

# Muestro la Matriz
def mostrar_matriz(matriz,loc):
	os.system('cls')                                    # Ejecuto el comando 'clear' del OS
	X, Y = matriz.shape                                   # Dimensiones de la matriz
	matriz_Ext = np.zeros((2*X+1, 2*Y+1))					# Inicializo la matriz con ceros
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

n = 1  # iteration counter
#nY, nX = os.get_terminal_size(0)		# Linux Obtengo COLUMNAS y LINEAS de la consola
nY, nX = os.get_terminal_size()		    # Windows Obtengo COLUMNAS y LINEAS de la consola
# print(f"cols: {os.get_terminal_size(0)[0]} , rows:  {os.get_terminal_size(0)[1]} ")
nX, nY = nX-22, int(nY/2)-1				  	# Ajusto por espacios e indicador de iteraciones
print(nX,nY)
pausar()

print(f"-----------BALANCE--------------")
inicio = time.time()

matriz = crear_matriz()

ejecutar_matriz(matriz)

print(f"Duración: {time.time()-inicio}")

print(f"Iteraciones: {n-3} de {ITERAC} | 4 matrices de {nX} filas y {nY} columnas")
