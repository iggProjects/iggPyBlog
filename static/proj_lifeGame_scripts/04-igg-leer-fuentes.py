#!/usr/bin/python3

# https://stackoverflow.com/questions/7618858/how-to-to-read-a-matrix-from-a-given-file
# https://numpy.org/doc/stable/reference/generated/numpy.loadtxt.html
# https://stackoverflow.com/questions/40955656/how-does-python-split-function-works/40955737
# https://www.geeksforgeeks.org/python-os-path-isfile-method/
# https://docs.python.org/3/library/os.html
# https://gist.github.com/jtriley/1108174

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
	userInput = input('Presiona ENTER para continuar CTRL-C para salir. ')

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
def crear_matriz(nombre_archivo):
	global nX, nY
	matriz = np.zeros((nX, nY))					# Inicializo la matriz con ceros
	x, y, lines = 0, 0, 0
  
	if isinstance(nombre_archivo, str) and os.path.isfile(nombre_archivo):
		try:
			with open(nombre_archivo) as archivo:
				for linea in archivo:
					lines += 1
					x += 1
					if x > (nX-1): break

					if (lines % 10 == 0 ):
						try:
							print(f"line number : {lines} ->\n{linea}")
						except Exception:
							traceback.print_exc()
						pausar()

					for num in linea.split():
						print(f"elemento ({x}, {y}) de la matriz: {num}")
						matriz[x,y] = int(num)
						y += 1
						if y > (nY-1): break

					# print()
					y = 0

		except Exception:
			traceback.print_exc()
			pausar()
			
		print(f"file with {lines} lines")
		pausar()	

	else:
		matriz = np.random.randint(2, size=(nX, nY))
		print(f"Matriz aleatorios")
		pausar()								# Matriz de aleatorios
	
	return matriz

#
# Programa
#

n=1										# Numero Iteraciones
nY, nX = os.get_terminal_size()			# Obtengo COLUMNAS y LINEAS de la consola
print(f"\nterminal columns: {os.get_terminal_size()[0]} , lines: {os.get_terminal_size()[1]}\n")
nX, nY = nX-10, int(nY/3)				# Ajusto por espacios e indicador de iteraciones
# print(f"{nX},{nY}")

pausar()
print(f"{nX},{nY}")
# Intento capturar nombre de archivo de la llamada
try:
	archivo = sys.argv[1]
except:
	archivo = 'NO_ARCHIVO'

matriz = crear_matriz(archivo)								# Obtengo la matriz
mostrar_matriz(matriz)

pausar()

# Iteraciones del programa
while n <= ITERAC:
	# pausar()
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
