#!/usr/bin/python3
import numpy as np
import os, sys, traceback
import time

#
# Constantes
#
ITERAC = 500
DORMIR= 0.1

#
# Funciones
#

# Pauso la ejecucion
def pausar():
	userInput = input('Presiona ENTER para continuar CTRL-C para salir. ');

# Muestro la Matriz
def mostrar_matriz(matriz):
	os.system('cls')                           # Ejecuto el comando 'clear' del OS
	X, Y = matriz.shape                          # Dimensiones de la matriz
	for y in range(0, Y):
		for x in range(0, X):
			if matriz[x,y] == 1:
				print(f"\033[0;91m{int(matriz[x,y])}\033[0m", end =" ")
			else:
				print(f"\033[0;37m{int(matriz[x,y])}\033[0m", end =" ")
		print()

# Creo matriz a partir de un archivo si es suministrado
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
		matriz = np.random.randint(2, size=(nX, nY))		# Matriz de aleatorios
	
	return matriz

#
# Programa
#
n=1										# Numero Iteraciones
nX, nY = os.get_terminal_size()		# Obtengo COLUMNAS y LINEAS de la consola
print(f"\nterminal columns, lines-----> {os.get_terminal_size()}\n")
nX, nY = int(nX/2), (nY-2)				# Ajusto por espacios e indicador de iteraciones

# Intento capturar nombre de archivo de la llamada
try:
	archivo = sys.argv[1]
except:
	archivo = 'NO_ARCHIVO'

matriz = crear_matriz(archivo)			# Obtengo la matriz
mostrar_matriz(matriz)

# pausa()

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
	# time.sleep(DORMIR)
	n+=1
