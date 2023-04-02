#!/usr/bin/python3
import numpy as np
import os, sys, traceback
import time

#
# Constantes
#
ITERAC = 100
DORMIR= 0.0

#
# Funciones
#

# Pauso la ejecucion
def pausar():
	userInput = input('Presiona ENTER para continuar CTRL-C para salir. ');

# Forzo a que el numero sea par quitando uno cuando son impares
def parificar(numero):
	if (numero % 2 ) == 1: numero -= 1
	return numero

# Muestro la Matriz
def mostrar_matriz(matriz):
	os.system('cls')                                    # Ejecuto el comando 'clear' del OS
	X, Y = matriz.shape                                   # Dimensiones de la matriz
	for y in range(0, Y):
		for x in range(0, X):
			if matriz[x,y] == 1:
				print(f"\033[0;91m{int(matriz[x,y])}\033[0m", end =" ")
			else:
				print(f"\033[0;37m{int(matriz[x,y])}\033[0m", end =" ")
		print()

# Creo matriz a partir de una archivo si es suministrado
def crear_matriz(nombre_archivo):
	global nX, nY
	matriz = np.zeros((nX, nY))					# Inicializo la matriz con ceros
	x, y = 0, 0

	if isinstance(nombre_archivo, str) and os.path.isfile(nombre_archivo):
		try:
			with open(nombre_archivo) as archivo:
				for linea in archivo:
					for num in linea.split():
						# print(f"->{num}<- ({x}, {y})")
						matriz[x,y] = int(num)
						x += 1
						if x > (nX-1): break
					print()
					x = 0
					y += 1
					if y > (nY-1): break
		except Exception:
			traceback.print_exc()
			pausar()
	else:
		matriz = np.random.randint(2, size=(nX, nY))										# Matriz de aleatorios
	
	return matriz

# Calculo la evolucion de la matriz
def calcular_matriz(matriz):
	X, Y = matriz.shape
	# Copio la matriz para poner en ella los cambios
	matrizTemp = np.copy(matriz)

	# Recorro la matriz para aplicar reglas a la matrizTemp
	for x in range(0, X):
		for y in range(0, Y):
			# Numero de Vecinos
			nVecinos = matriz[	(x-1), (y-1) ] 		\
							 + matriz[	(x), 	(y-1) ] 		\
							 + matriz[	(x+1)%X, (y-1) ] 		\
							 + matriz[	(x-1), (y) ] 			\
							 + matriz[	(x+1)%X, (y) ] 			\
							 + matriz[	(x-1), (y+1)%Y ] 		\
							 + matriz[	(x), 	(y+1)%Y ] 		\
							 + matriz[	(x+1)%X, (y+1)%Y ]

			# Regla 1: celda muerta (0) con 3 vecinas revive (1)
			if matriz[x,y] == 0 and nVecinos == 3:
				matrizTemp[x,y] = 1

			# Regla 2: celda viva (1) con mas de 3 vecinas o menos de 2 muere (2)
			elif matriz[x,y] == 1 and ( nVecinos < 2 or nVecinos > 3 ):
				matrizTemp[x,y] = 0

	return matrizTemp

#
# Programa
#

if __name__ == '__main__':

	n=1																								# Numero Iteraciones
	# nX, nY = os.get_terminal_size(0)									# Obtengo COLUMNAS y LINEAS de la consola
	# nX, nY = parificar(int(nX/2)), parificar(nY-2)		# Ajusto por espacios e indicador de iteraciones
	nX, nY = 2000, 2000

	print(f"\nPlaying LifeGame with {nX} cols, {nY} rows and {ITERAC} iterations\n ")
	pausar()


	# Intento capturar nombre de archivo de la llamada
	try:
		nX, nY = int(sys.argv[1]), int(sys.argv[1])
		archivo = 'NO_ARCHIVO'
	except:
		archivo = 'NO_ARCHIVO'

	matriz = crear_matriz(archivo)								# Obtengo la matriz
	# mostrar_matriz(matriz)

	# pausar()

	# Iteraciones del programa
	while n <= ITERAC:

		# Calculo la iteracion de la matriz
		matriz = calcular_matriz(matriz)

		# Muestro la nueva cara de la matriz
		# mostrar_matriz(matriz)
		print(f"Iteraciones: {n} de {ITERAC} ({nX}, {nY})")
		time.sleep(DORMIR)
		n+=1
