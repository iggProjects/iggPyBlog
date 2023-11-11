#!/usr/bin/python3

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

try:   # Import My Own Functions from include dir 
    import sys, traceback
    import numpy as np   
    from os.path import dirname, realpath
    from os import scandir
    # get parent up 2 from __file__ path: 'static path'   
    up2_dir = dirname(dirname(dirname(realpath(__file__))))
    # insert path in sys.path
    sys.path.append(up2_dir)
    # get parent up 3 from __file__ path: 'static parent path'       
    up3_dir = dirname(dirname(dirname(dirname(realpath(__file__)))))
    # insert path in sys.path
    sys.path.append(up3_dir)
    # import My Own Func
    from static.include.MyFunc import *
    from static.include.MyColors import *
except Exception as ImportError:
    FR_RED   = "\033[91m" 
    NO_COLOR = "\033[00m"
    print("print empty line") 
    print(f"{FR_RED}IMPORT ERROR ==>{NO_COLOR} {ImportError} | {ImportError.__class__} | {ImportError.__doc__}")

#
# FUNC
#

# Muestro la Matriz
def mostrar_matriz(matriz,msg):
	#print(f"{FR_BLUE}{msg}")
	#print(f"{NO_COLOR}")
	X, Y = matriz.shape                                   # Dimensiones de la matriz
	for x in range(0, X):
		for y in range(0, Y):
			if matriz[x,y] == 1:
				print(f"{int(matriz[x,y])}", end =" ")
			else:
				print(f"{int(matriz[x,y])}", end =" ")
		print()
	print("print empty line") 		

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
						# 

					for num in linea.split():
						print(f"elemento ({x}, {y}) de la matriz: {num}")
						matriz[x,y] = int(num)
						y += 1
						if y > (nY-1): break

					# print()
					y = 0

		except Exception:
			traceback.print_exc()			 
			
		print(f"file with {lines} lines")		# 	

	else:
		matriz = np.random.randint(2, size=(nX, nY))
	
	return matriz

# CONSTANTS
ITERAC = 100
DORMIR= 0.01

#
# ---------- MAIN ----------
#

if __name__ == "__main__":
	
	try:
		
		my_script = __file__.split('\\')
		my_script_name = my_script[len(my_script)-1]
		write_log_file("my_messages.txt","IN '" + my_script_name + "'")

		n=1										# Contador Iteraciones
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
		print(f"MATRIZ INICIAL--{nX}x{nY}")
		mostrar_matriz(matriz, "")					# muestro matriz inicial
		#print(F"\n\t{FR_YELL}MATRIZ INICIAL ALEATORIA (0 Y 1){NO_COLOR}\n")
		#print(F"\t{FR_GREEN}M Se mostrará la matriz cada 20 iteraciones{NO_COLOR}\n")


		# Iteraciones del programa
		while n <= ITERAC:
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
			if n % 10 == 0:
				
				print(f"Iter-{n}/{ITERAC}, Matriz-{nX}x{nY}")
				mostrar_matriz(matriz,"")
				
			n+=1

		print(f"{FR_GREEN}---------- That's all for today ----------{NO_COLOR}")

	except Exception as Argument:
		error_msg = "ERROR IN <" + my_script_name + ">. SEE server_messages.txt !"
		write_log_file("my_messages.txt",error_msg)
		write_traceback_info_1(Argument,traceback,my_script_name)        
    
else:
    # something wrong
    print(frRED("---- ****** ----"))
