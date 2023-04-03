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
	X, Y = matriz.shape                                   # Dimensiones de la matriz
	for y in range(0, Y):
		for x in range(0, X):
			if matriz[x,y] == 1:
				print(f"\t\033[0;91m{int(matriz[x,y])}\033[0m", end =" ")
			else:
				print(f"\t\033[0;37m{int(matriz[x,y])}\033[0m", end =" ")
		print()
	pausar()	


system('cls')         # Ejecuto el comando 'clear' del OS
nX, nY = 6, 6

matriz = np.arange(nX*nY).reshape(nX, nY)
mostrar_matriz(matriz,"matriz inicial")

print(f"{FR_MAG}\n============== Matrices partidas ==============={NO_COLOR}\n")

m0 = matriz[ 0:int(nX/2), 0:int(nY/2) ]
mostrar_matriz(m0, "m0: matriz[ 0:int(nX/2), 0:int(nY/2) ]")

m1 = matriz[ int(nX/2):nX, 0:int(nY/2) ]
mostrar_matriz(m1, "m1: matriz[ int(nX/2):nX, 0:int(nY/2) ]")


m2 = matriz[ 0:int(nX/2), int(nY/2):nY ]
mostrar_matriz(m2,"m2: matriz[ 0:int(nX/2), int(nY/2):nY")

m3 = matriz[ int(nX/2):nX, int(nY/2):nY ]
mostrar_matriz(m3,"m3: matriz[ int(nX/2):nX, int(nY/2):nY ]")

izq = m1[ [0], : ]
mostrar_matriz(izq,"izq: m1[ [0], : ]")

der = m1[ [int(nX/2)-1], : ]
mostrar_matriz(der,"der: m1[ [int(nX/2)-1], : ]")

#m0e = m1[ [int(nX/2)-1], : ]  ??????
m0e = np.vstack( (izq, m0, der) )
mostrar_matriz(m0e,"m0e: m1[ [int(nX/2)-1], : ]")

top = np.vstack(
	( [m3[int(nX/2)-1, 0]], m2[ :, [0] ], [m3[0, 0]] )
)
mostrar_matriz(top,"top: np.vstack( ( [m3[int(nX/2)-1, 0]], m2[ :, [0] ], [m3[0, 0]] ) )")

bot = np.vstack(
	( [m3[int(nX/2)-1, int(nY/2)-1]], m2[ :, [int(nY/2)-1] ], [m3[0, int(nY/2)-1]] )
)
mostrar_matriz(bot,"bot: np.vstack(( [m3[int(nX/2)-1, int(nY/2)-1]], m2[ :, [int(nY/2)-1] ], [m3[0, int(nY/2)-1]] ))")

m0e = np.hstack( ( top, m0e, bot) )
#m0e = np.hstack( ( fon, m0e, top) )
mostrar_matriz(m0e,"m0e_: np.hstack( ( top, m0e, bot) )")

print(f"\n{FR_YELL}======== that's all ========{NO_COLOR}\n")

#print()
#mostrar_matriz( np.vstack( (m0,m1) ) )
#print()
#mostrar_matriz( np.vstack( (m2,m3) ) )
#print()
#
#matriz = np.hstack( (np.vstack( (m0,m1) ), np.vstack( (m2,m3) )) )
#mostrar_matriz(matriz)
