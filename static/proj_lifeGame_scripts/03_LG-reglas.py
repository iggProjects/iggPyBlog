#!/usr/bin/python3
import numpy as np
import os
import time

os.system('cls')

# Constantes

# Colors
NO_COLOR = "\033[00m"
FR_GREEN = "\033[92m"
FR_RED   = "\033[91m"
FR_BLUE  = "\033[94m"
FR_YELL  = "\033[93m"
FR_MAG   = "\033[95m"

# 
ITERAC = 100
nX = 12
nY = 12
yExt = 2*nY + 1
# nX, nY = os.get_terminal_size(0)
# nX, nY = int(nX/2)-5, (nY-5)

#
# Funciones
#
def pausar(i):
	userInput = input(f"\nIteración No: {i}, matriz {nX} x {nY}\nPresiona ENTER para continuar CTRL-C para salir\n")

def mostrar_matriz(matriz):
	# os.system('clear')
	X, Y = matriz.shape
	for x in range(0, X):
		for y in range(0, Y):
			if matriz[x,y] == 1:
				print(f"\033[0;91m{int(matriz[x,y])}\033[0m", end =" ")
			elif matriz[x,y] == 0:
				print(f"\033[0;37m{int(matriz[x,y])}\033[0m", end =" ")
			elif matriz[x,y] == 99999:
				print(f"\033[0;32m{int(matriz[x,y])}\033[0m", end =" ")
			else:
				print(f"\033[0;37m{int(matriz[x,y])}\033[0m", end =" ")
				 	 	
		print()

#
# MAIN
#

matriz  = np.random.randint(2, size=(nX, nY))
matriz_ext = np.zeros((nX,yExt))

for x in range(0,nX):
	for y in range(0,nY):
		matriz_ext[x,y] = matriz[x,y]

		nVecinos = matriz[ x-1, y-1 ]    \
						 + matriz[ x, y-1 ]    \
						 + matriz[ (x+1)%(nX), y-1 ]    \
						 + matriz[ x-1, y ]      \
						 + 0 * matriz[ x, y ]      \
						 + matriz[ (x+1)%nX, y ]      \
						 + matriz[ x-1, (y+1)%nY ]    \
						 + matriz[ x,   (y+1)%nY ]    \
						 + matriz[ (x+1)%nX, (y+1)%nY ]
		
		matriz_ext[x,y+nY+1] = nVecinos

for x in range (0,nX):
	matriz_ext[x,nY] = 99999 

n=1
while n <= ITERAC:
	# pausar(n)
	matrizTemp = np.copy(matriz_ext)
	# mostrar_matriz(matrizTemp)
	# print()

	for x in range(0, nX):
		for y in range(0, nY):

			if matriz_ext[x,y] == 0 and matriz_ext[x,y+nY+1] == 3:
				matrizTemp[x,y] = 1

			elif matriz_ext[x,y] == 1 and ( matriz_ext[x,y+nY+1]  < 2 or matriz_ext[x,y+nY+1] > 3 ):
				matrizTemp[x,y] = 0
	
				
	for x in range(0, nX):
		for y in range(0, nY):

			nVecinos = matrizTemp[ (x-1)%nX, (y-1)%nY ]    \
							 + matrizTemp[ x, (y-1)%nY ]    \
							 + matrizTemp[ (x+1)%(nX), (y-1)%nY ]    \
							 + matrizTemp[ (x-1)%nX, y ]      \
							 + 0 * matrizTemp[ x, y ]      \
							 + matrizTemp[ (x+1)%nX, y ]      \
							 + matrizTemp[ (x-1)%nX, (y+1)%nY ]    \
							 + matrizTemp[ x,   (y+1)%nY ]    \
							 + matrizTemp[ (x+1)%nX, (y+1)%nY ]
		
			matrizTemp[x,y+nY+1] = nVecinos

	matriz_ext = np.copy(matrizTemp)
	print(f"\n{FR_YELL}  Matriz Game of Life{NO_COLOR}   -----    {FR_GREEN}Matriz Num Vecinos{NO_COLOR}")
	mostrar_matriz( matriz_ext )
	#print(f"Iteraciones: {n} de {ITERAC} ({nX}, {nY}) ")
	#time.sleep(2)
	if n < 5:
		pausar(n)
	else:
		print(f"Iteración No: {n}\nmatriz {nX} x {nY}\n")	
	n += 1

print(f"\n\033[0;93mTotal iteraciones Game of Life: {ITERAC}\033[0m\nmatriz {nX} x {nY}\n")
	
print("FIN\n")
