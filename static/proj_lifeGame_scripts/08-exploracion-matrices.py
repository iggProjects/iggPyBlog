#!/usr/bin/python3
#  vstack
#  		https://numpy.org/doc/1.18/reference/generated/numpy.vstack.html
#			https://www.geeksforgeeks.org/numpy-vstack-in-python/
#			https://www.w3resource.com/numpy/manipulation/vstack.php
#			https://www.geeksforgeeks.org/numpy-hstack-in-python/
#
#  arange
#			https://www.geeksforgeeks.org/numpy-arange-python/	
#
#  extract sub matriz
#			https://mail.python.org/pipermail/tutor/2010-July/077020.html
#			https://stackoverflow.com/questions/509211/understanding-slice-notation 
#


import numpy as np
import os

# Colors
NO_COLOR = "\033[00m"
FR_GREEN = "\033[92m"
FR_RED   = "\033[91m"
FR_BLUE  = "\033[34m"

# Pauso la ejecucion
def pausar():
	userInput = input('\tPresiona ENTER para continuar CTRL-C para salir.')

# Muestro la Matriz
def mostrar_matriz(matriz,msg):
	X, Y = matriz.shape                                   # Dimensiones de la matriz
	print(f"\n{FR_GREEN}{msg}{NO_COLOR}\n")
	for y in range(0, Y):
		for x in range(0, X):
			if matriz[x,y] == 1:
				print(f"\t\033[0;91m{int(matriz[x,y])}\033[0m", end =" ")
			else:
				print(f"\t\033[0;37m{int(matriz[x,y])}\033[0m", end =" ")
		print()
	#print()	
	pausar()	


os.system('cls')                                    # Ejecuto el comando 'clear' del OS
nX, nY = 8, 8

matriz = np.arange(nX*nY).reshape(nX, nY)
msg = "Matriz inicial de " + str(nX) + " col y " + str(nY) + " rows"
mostrar_matriz(matriz,msg)

m0 = matriz[ 0:int(nX/2), 0:int(nY/2) ]
mostrar_matriz(m0, "m0")

m1 = matriz[ int(nX/2):nX, 0:int(nY/2) ]
mostrar_matriz(m1, "m1")

m2 = matriz[ 0:int(nX/2), int(nY/2):nY ]
mostrar_matriz(m2,"m2")

m3 = matriz[ int(nX/2):nX, int(nY/2):nY ]
mostrar_matriz(m3,"m3")

der = m1[ [0], : ]
mostrar_matriz(der, "derecha")

izq = m1[ [int(nX/2)-1], : ]
mostrar_matriz(izq, "izquierda")

m0e=np.vstack( (izq, m0, der) )
mostrar_matriz(m0e, "m0 expandida fase 1")

bot = np.vstack(
	( [m3[int(nX/2)-1, 0]], m2[ :, [0] ], [m3[0, 0]] )
)
mostrar_matriz(bot, "bot")

top = np.vstack(
	( [m3[int(nX/2)-1, int(nY/2)-1]], m2[ :, [int(nY/2)-1] ], [m3[0, int(nY/2)-1]] )
)
mostrar_matriz(top, "top")

m0e = np.hstack( ( top, m0e, bot) )
mostrar_matriz(m0e, "m0e expandida")

#print()
#mostrar_matriz( np.vstack( (m0,m1) ) )
#print()
#mostrar_matriz( np.vstack( (m2,m3) ) )
#print()
#
#matriz = np.hstack( (np.vstack( (m0,m1) ), np.vstack( (m2,m3) )) )
#mostrar_matriz(matriz)
