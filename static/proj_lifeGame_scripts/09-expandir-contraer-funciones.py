#!/usr/bin/python3
import numpy as np

# Muestro la Matriz
def mostrar_matriz(matriz):
	# os.system('cls')
	X, Y = matriz.shape
	for y in range(0, Y):
		for x in range(0, X):
			if matriz[x,y] == 1:
				print(f"\033[0;91m{int(matriz[x,y])}\033[0m", end =" ")
			else:
				print(f"\033[0;37m{int(matriz[x,y])}\033[0m", end =" ")
		print()

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
nX, nY = 6, 6

matriz = np.arange(nX*nY).reshape(nX, nY)
mostrar_matriz(matriz)

# particiono la matriz
m0 = matriz[ 0:int(nX/2), 0:int(nY/2) ]
m1 = matriz[ int(nX/2):nX, 0:int(nY/2) ]
m2 = matriz[ 0:int(nX/2), int(nY/2):nY ]
m3 = matriz[ int(nX/2):nX, int(nY/2):nY ]

print("Matrices partidas")
mostrar_matriz(m0)
print()
mostrar_matriz(m1)
print()
mostrar_matriz(m2)
print()
mostrar_matriz(m3)
print()

# Expando las matrices
m0e = expandir_matriz(m0, m1, m2, m3)
m1e = expandir_matriz(m1, m0, m3, m2)
m2e = expandir_matriz(m2, m3, m0, m1)
m3e = expandir_matriz(m3, m2, m1, m0)

print("Matrices expandidas")
mostrar_matriz(m0e)
print()
mostrar_matriz(m1e)
print()
mostrar_matriz(m2e)
print()
mostrar_matriz(m3e)
print()

# contraigo las matricez
m0c = contraer_matriz(m0e)
m1c = contraer_matriz(m1e)
m2c = contraer_matriz(m2e)
m3c = contraer_matriz(m3e)

print("Matrices contraidas")
mostrar_matriz(m0c)
print()
mostrar_matriz(m1c)
print()
mostrar_matriz(m2c)
print()
mostrar_matriz(m3c)
print()

print("Matriz completa")
matrizFinal = np.hstack( (np.vstack( (m0c, m1c) ), np.vstack( (m2c, m3c) )) )
mostrar_matriz(matrizFinal)
