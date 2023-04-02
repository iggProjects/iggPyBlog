#!/usr/bin/python3
import numpy as np
import os

# Muestro la Matriz
def mostrar_matriz(matriz):
	# os.system('cls')                                    # Ejecuto el comando 'clear' del OS
	X, Y = matriz.shape                                   # Dimensiones de la matriz
	for y in range(0, Y):
		for x in range(0, X):
			if matriz[x,y] == 1:
				print(f"\033[0;91m{int(matriz[x,y])}\033[0m", end =" ")
			else:
				print(f"\033[0;37m{int(matriz[x,y])}\033[0m", end =" ")
		print()

nX, nY = 6, 6

matriz = np.arange(nX*nY).reshape(nX, nY)
mostrar_matriz(matriz)

print("Matriz 0")
m0 = matriz[ 0:int(nX/2), 0:int(nY/2) ]
mostrar_matriz(m0)
# print("Matriz 1")
m1 = matriz[ int(nX/2):nX, 0:int(nY/2) ]
# mostrar_matriz(m1)
# print("Matriz 2")
m2 = matriz[ 0:int(nX/2), int(nY/2):nY ]
# mostrar_matriz(m2)
# print("Matriz 3")
m3 = matriz[ int(nX/2):nX, int(nY/2):nY ]
# mostrar_matriz(m3)
print()
izq = m1[ [0], : ]
mostrar_matriz(izq)
print()
der = m1[ [int(nX/2)-1], : ]
mostrar_matriz(der)
print()
m0e=np.vstack( (der, m0, izq) )
mostrar_matriz(m0e)

print()
top = np.vstack(
	( [m3[int(nX/2)-1, 0]], m2[ :, [0] ], [m3[0, 0]] )
)
mostrar_matriz(top)

print()
fon = np.vstack(
	( [m3[int(nX/2)-1, int(nY/2)-1]], m2[ :, [int(nY/2)-1] ], [m3[0, int(nY/2)-1]] )
)
mostrar_matriz(fon)
print()
m0e = np.hstack( ( fon, m0e, top) )
mostrar_matriz(m0e)

#print()
#mostrar_matriz( np.vstack( (m0,m1) ) )
#print()
#mostrar_matriz( np.vstack( (m2,m3) ) )
#print()
#
#matriz = np.hstack( (np.vstack( (m0,m1) ), np.vstack( (m2,m3) )) )
#mostrar_matriz(matriz)
