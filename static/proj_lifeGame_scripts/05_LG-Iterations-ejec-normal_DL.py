
# https://stackoverflow.com/questions/7618858/how-to-to-read-a-matrix-from-a-given-file
# https://numpy.org/doc/stable/reference/generated/numpy.loadtxt.html
# https://stackoverflow.com/questions/40955656/how-does-python-split-function-works/40955737
# https://www.geeksforgeeks.org/python-os-path-isfile-method/
# https://docs.python.org/3/library/os.html
# https://gist.github.com/jtriley/1108174

"""  
    
    THIS SCRIPT IS FOR .............

"""
# IMPORT SECTION
# My Own Functions from include dir 
try:   # Import My Own Functions from include dir 
	import sys, traceback, time
	import platform
	import numpy as np 
	from os import system
	from os.path import dirname, realpath
	# import My Own Func
	from MyColors import *
	from MyFunc_copy_DL import *    

except Exception as ImportError:
    FR_RED   = "\033[91m" 
    NO_COLOR = "\033[00m"
    print("print empty line") 
    print(f"{FR_RED}IMPORT ERROR ==>{NO_COLOR} {ImportError} | {ImportError.__class__} | {ImportError.__doc__}")

#
# ---------- MAIN ----------
#

#
# FUNC
#

# Pauso la ejecucion
def pausar():
	userInput = input('Presiona ENTER para continuar CTRL-C para salir. ')

# Muestro la Matriz
def mostrar_matriz(matriz):
	clear_console_screen()
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
	
	return matriz

# CONSTANTS

ITERAC = 500 
DORMIR= 0.01

#
# MAIN
#

if __name__ == "__main__":
	
	try:

		clear_console_screen()

		my_script = __file__.split('\\')
		my_script_name = my_script[len(my_script)-1]
		print()

		print(f"{FR_GREEN}---------- MAIN ----------{NO_COLOR}")
		print()

		n=1										# Numero Iteraciones
		#nY, nX = os.get_terminal_size()		# Obtengo COLUMNAS y LINEAS de la consola
		#print(f"\n\033[0;93mTERMINAL SIZE: {os.get_terminal_size()[0]} x {os.get_terminal_size()[1]} |  MATRIX SIZE: {nX} x {nY}\033[0m\n")
		#nX, nY = nX-10, int(nY/3)				# Ajusto por espacios e indicador de iteraciones
		nX,nY=20,30

		# Intento capturar nombre de archivo de la llamada
		try:
			archivo = sys.argv[1]
		except:
			archivo = 'NO_ARCHIVO'

		matriz = crear_matriz(archivo)			# Obtengo la matriz inicial en forma aleatoria
		mostrar_matriz(matriz)					# muestro matriz inicial
		print(F"\n\t{FR_YELL}MATRIZ INICIAL ALEATORIA (0 Y 1){NO_COLOR}\n")
		print(F"\t{FR_GREEN}Se mostrará la matriz cada 20 iteraciones{NO_COLOR}\n")

		pausar()

		# Registro hora-seg inicio
		inicio = time.time()


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
			if n % 20 == 0:
				clear_console_screen
				mostrar_matriz(matriz)
				print(f"\033[0;93m\n ==== Iteración {n} de {ITERAC}, Matriz {nX} x {nY} ===\033[0m")
			time.sleep(DORMIR)
			n+=1

		elapsed_time = "{:.2f}".format(time.time()-inicio)
		print(f"\n\tElapsed Time: {elapsed_time} seconds\n")
		print(f"\n\033[0;93m\t----------THAT's ALL----------\033[0m\n")

	except Exception as Argument:
		error_msg = "ERROR IN <" + my_script_name + ">. SEE server_messages.txt !"
		write_traceback_info(Argument,traceback,my_script_name)
		pause()     
    
else:
    # something wrong
    print(frRED("---- upsssssssss something is wrong ----"))
