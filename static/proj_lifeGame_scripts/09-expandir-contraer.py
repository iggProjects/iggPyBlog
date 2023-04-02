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

print("Matriz 0")
mostrar_matriz(m0)

# EXTENDER MATRIZ
izq = m1[ [0], : ]
der = m1[ [int(nX/2)-1], : ]
top = np.vstack(
	( [m3[int(nX/2)-1, 0]], m2[ :, [0] ], [m3[0, 0]] )
)
fon = np.vstack(
	( [m3[int(nX/2)-1, int(nY/2)-1]], m2[ :, [int(nY/2)-1] ], [m3[0, int(nY/2)-1]] )
)
m0e = np.vstack( (der, m0, izq) )
m0e = np.hstack( (fon, m0e, top) )
print("Matriz 0 extendida")
mostrar_matriz(m0e)

# CONTRAER
X, Y = m0e.shape
m0c = m0e[  1:(X-1), 1:(Y-1) ]
print("Matriz 0 contraida")
mostrar_matriz(m0)

# RECOMPONGO LA MATRIZ COMPLETA
print("Matriz completa")
matriz = np.hstack( (np.vstack( (m0c,m1) ), np.vstack( (m2,m3) )) )
mostrar_matriz(matriz)
