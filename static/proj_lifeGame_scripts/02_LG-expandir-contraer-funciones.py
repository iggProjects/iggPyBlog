#!/usr/bin/python3
import numpy as np
from os import system

# Colors
NO_COLOR = "\033[00m"
FR_GREEN = "\033[92m"
FR_RED   = "\033[91m"
FR_BLUE  = "\033[94m"
FR_YELL  = "\033[93m"
FR_MAG   = "\033[95m"

# Pauso la ejecucion
def pausar():
	userInput = input("\tPresiona ENTER para continuar CTRL-C para salir.")

# Muestro la Matriz
def mostrar_matriz(matriz,msg):	
	print(f"\n{FR_YELL}{msg}{NO_COLOR}\n")
	X, Y = matriz.shape
	for y in range(0, Y):
		for x in range(0, X):
			if matriz[x,y] == 1:
				print(f"\t\033[0;91m{int(matriz[x,y])}\033[0m", end =" ")
			else:
				print(f"\t\033[0;37m{int(matriz[x,y])}\033[0m", end =" ")
		print()
	pausar()

# Expando una matriz
def expandir_matriz(m0, m1, m2, m3):          # matriz, izq, der, top, fon
	# determino: izq, der, top, fon
	izq = m1[ [0], : ]
	der = m1[ [int(nX/2)-1], : ]
	top = np.vstack(
		( [m3[int(nX/2)-1, 0]], m2[ :, [0] ], [m3[0, 0]] )
	)
	fon = np.vstack(
		( [m3[int(nX/2)-1, int(nY/2)-1]], m2[ :, [int(nY/2)-1] ], [m3[0, int(nY/2)-1]] )
	)

	# Reconfiguro la matriz "horizontalmente"
	m0 = np.vstack( (der, m0, izq) )
	# Reconfiguro la matriz "verticalmente"
	m0 = np.hstack( (fon, m0, top) )
	return m0

# Contraigo la matriz
def contraer_matriz(matriz):
	X, Y = matriz.shape
	matriz = matriz[ 1:(X-1), 1:(Y-1) ]
	return matriz
#
#
#

system('cls')

nX, nY = 6, 6

matriz = np.arange(nX*nY).reshape(nX, nY)
mostrar_matriz(matriz,"Matriz inicial")

# particiono la matriz
m0 = matriz[ 0:int(nX/2), 0:int(nY/2) ]
m1 = matriz[ int(nX/2):nX, 0:int(nY/2) ]
m2 = matriz[ 0:int(nX/2), int(nY/2):nY ]
m3 = matriz[ int(nX/2):nX, int(nY/2):nY ]

print(f"{FR_MAG}\n============== Matrices partidas ==============={NO_COLOR}\n")

mostrar_matriz(m0,"Matriz m0:  matriz[ 0:int(nX/2), 0:int(nY/2) ]")
print()
mostrar_matriz(m1,"Matriz m1:  matriz[int(nX/2):nX, 0:int(nY/2) ]")
print()
mostrar_matriz(m2,"Matriz m2:  matriz[ 0:int(nX/2), int(nY/2):nY ]")
print()
mostrar_matriz(m3,"Matriz m3:  matriz[ int(nX/2):nX, int(nY/2):nY ]")
print()

# Expando las matrices
m0e = expandir_matriz(m0, m1, m2, m3)
m1e = expandir_matriz(m1, m0, m3, m2)
m2e = expandir_matriz(m2, m3, m0, m1)
m3e = expandir_matriz(m3, m2, m1, m0)

print(f"{FR_MAG}\n====== Matrices expandidas ======\n{NO_COLOR}")
mostrar_matriz(m0e,"m0e: expandir_matriz(m0, m1, m2, m3)")
print()
mostrar_matriz(m1e,"m1e: expandir_matriz(m1, m0, m3, m2)")
print()
mostrar_matriz(m2e,"m2e: expandir_matriz(m2, m3, m0, m1)")
print()
mostrar_matriz(m3e,"m3e: expandir_matriz(m3, m2, m1, m0)")
print()

# contraigo las matricez
m0c = contraer_matriz(m0e)
m1c = contraer_matriz(m1e)
m2c = contraer_matriz(m2e)
m3c = contraer_matriz(m3e)

print(f"{FR_MAG}\n====== Matrices contraidas ======\n{NO_COLOR}")
mostrar_matriz(m0c,"m0c: contraer_matriz(m0e)")
print()
mostrar_matriz(m1c,"m1c: contraer_matriz(m1e)")
print()
mostrar_matriz(m2c,"m2c: contraer_matriz(m2e)")
print()
mostrar_matriz(m3c,"m3c: contraer_matriz(m3e)")
print()

print(f"{FR_GREEN}\n====== MATRIZ FINAL COMPLETA ======\n{NO_COLOR}")
matrizFinal = np.hstack( (np.vstack( (m0c, m1c) ), np.vstack( (m2c, m3c) )) )
mostrar_matriz(matrizFinal,"Matriz Final: np.hstack( (np.vstack( (m0c, m1c) ), np.vstack( (m2c, m3c) )) )")

print(f"\n{FR_YELL}======== that's all ========{NO_COLOR}\n")