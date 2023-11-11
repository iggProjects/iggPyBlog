"""  
    
    THIS SCRIPT IS FOR .............

"""
# IMPORT SECTION

try:   # Import My Own Functions from include dir 
    import sys, traceback, time
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
    print() 
    print(f"{FR_RED}IMPORT ERROR ==>{NO_COLOR} {ImportError} | {ImportError.__class__} | {ImportError.__doc__}")

#
# ---------- MAIN ----------
#

#
# CONSTANTS
#
ITERAC = 200
DORMIR= 0.005

#
# Funciones
#

# Pauso la ejecucion
def pausar():
	userInput = input('Presiona ENTER para continuar CTRL-C para salir. ');

# Forzo a que el numero sea par quitando uno cuando son impares
def parificar(numero):
	if (numero % 2 ) == 1: numero -= 1
	return numero

# Muestro la Matriz
def mostrar_matriz(matriz,msg):
	#print(f"\n{FR_YELL}{msg}{NO_COLOR}\n")
	clear_console_screen()
	X, Y = matriz.shape                                   # Dimensiones de la matriz
	for y in range(0, Y):
		for x in range(0, X):
			if matriz[x,y] == 1:
				print(f"{FR_RED}{int(matriz[x,y])}{NO_COLOR}", end =" ")
			else:
				print(f"\033[0;37m{int(matriz[x,y])}{NO_COLOR}", end =" ")
		print()

# Creo matriz a partir de una archivo si es suministrado
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
		matriz = np.random.randint(2, size=(nX, nY))										# Matriz de aleatorios
	
	return matriz

# Calculo la evolucion de la matriz
def calcular_matriz(matriz):	
	X, Y = matriz.shape
	# Copio la matriz para poner en ella los cambios
	matrizTemp = np.copy(matriz)

	# Recorro la matriz para aplicar reglas a la matrizTemp
	for x in range(1, X-1):
		for y in range(1, Y-1):
			# Numero de Vecinos
			nVecinos = matriz[	(x-1), (y-1) ] 		\
							 + matriz[	(x), 	(y-1) ] 		\
							 + matriz[	(x+1), (y-1) ] 		\
							 + matriz[	(x-1), (y) ] 			\
							 + matriz[	(x+1), (y) ] 			\
							 + matriz[	(x-1), (y+1) ] 		\
							 + matriz[	(x), 	(y+1) ] 		\
							 + matriz[	(x+1), (y+1) ]

			# Regla 1: celda muerta (0) con 3 vecinas revive (1)
			if matriz[x,y] == 0 and nVecinos == 3:
				matrizTemp[x,y] = 1

			# Regla 2: celda viva (1) con mas de 3 vecinas o menos de 2 muere (2)
			elif matriz[x,y] == 1 and ( nVecinos < 2 or nVecinos > 3 ):
				matrizTemp[x,y] = 0

	return matrizTemp

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
# MAIN
#

if __name__ == '__main__':
		
	try:

		clear_console_screen()
	
		my_script = __file__.split('\\')
		my_script_name = my_script[len(my_script)-1]
		write_log_file("my_messages.txt","IN '" + my_script_name + "'")

		n=1												 # contador Iteraciones
		#nX, nY = os.get_terminal_size()				 # Windows Obtengo COLUMNAS y LINEAS de la consola
		#nX, nY = os.get_terminal_size(0)				 # Linux   Obtengo COLUMNAS y LINEAS de la consola
		#nX, nY = parificar(int(nX/2)), parificar(nY-2)	 # Ajusto por espacios e indicador de iteraciones

		nX, nY = 26,13

		# Intento capturar nombre de archivo de la llamada
		try:
			archivo = sys.argv[1]
		except:
			archivo = 'NO_ARCHIVO'

		matriz = crear_matriz(archivo)								# Obtengo la matriz
		mostrar_matriz(matriz,"Matriz Inicial")
		print(f"{FR_GREEN}MATRIZ INICIAL{NO_COLOR}")
		pausar()

		# Registro hora-seg inicio
		inicio = time.time()

		# Iteraciones del programa
		while n <= ITERAC:
			# particiono la matriz
			m0 = matriz[ 0:int(nX/2), 0:int(nY/2) ]
			m1 = matriz[ int(nX/2):nX, 0:int(nY/2) ]
			m2 = matriz[ 0:int(nX/2), int(nY/2):nY ]
			m3 = matriz[ int(nX/2):nX, int(nY/2):nY ]

			# Expando las matrices
			m0e = expandir_matriz(m0, m1, m2, m3)
			m1e = expandir_matriz(m1, m0, m3, m2)
			m2e = expandir_matriz(m2, m3, m0, m1)
			m3e = expandir_matriz(m3, m2, m1, m0)

			# Calculo la iteracion de la matriz
			m0e = calcular_matriz(m0e)
			m1e = calcular_matriz(m1e)
			m2e = calcular_matriz(m2e)
			m3e = calcular_matriz(m3e)

			# contraigo las matricez
			m0 = contraer_matriz(m0e)
			m1 = contraer_matriz(m1e)
			m2 = contraer_matriz(m2e)
			m3 = contraer_matriz(m3e)

			# Recombino las matrices particionadas
			matriz = np.hstack( (np.vstack( (m0,m1) ), np.vstack( (m2,m3) )) )
			# Print cada 10 iteraciones
			if n % 10 == 0:
				mostrar_matriz(matriz,"Nueva cara Matriz")
				print(f"Iteraciones: {n} de {ITERAC} | Matriz {nX} x {nY}")
			time.sleep(DORMIR)
			n+=1

		elapsed_time = "{:.2f}".format(time.time()-inicio)
		print(f"\n{FR_GREEN}   Elapsed Time: {elapsed_time} seconds{NO_COLOR}\n")
		print(f"\n{FR_YELL}   ----------THAT's ALL----------\033[0m\n")

	except Exception as Argument:
		error_msg = "ERROR IN <" + my_script_name + ">. SEE server_messages.txt !"
		write_log_file("my_messages.txt",error_msg)
		write_traceback_info_1(Argument,traceback,my_script_name)
	
else:
    # something wrong
    print(frRED("---- ****** ----"))
