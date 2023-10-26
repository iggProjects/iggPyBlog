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
    print() 
    print(f"{FR_RED}IMPORT ERROR ==>{NO_COLOR} {ImportError} | {ImportError.__class__} | {ImportError.__doc__}")


# Muestro la Matriz
def mostrar_matriz(matriz,msg):	
	print(f"\n{FR_YELL}{msg}{NO_COLOR}\n")
	X, Y = matriz.shape
	for y in range(0, Y):
		for x in range(0, X):
			print(f"{int(matriz[x,y])}", end =" ")
		print()
	print()	
	pause()

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

if __name__ == "__main__":

	try:

		clear_console_screen()

		my_script = __file__.split('\\')
		my_script_name = my_script[len(my_script)-1]
		#print(f".....my_script_name: {my_script_name}")
		print()
		write_log_file("my_messages.txt","IN '" + my_script_name + "'")
		print()

		print(f"{FR_GREEN}---------- MAIN ----------{NO_COLOR}")
		print()

		nX, nY = 6, 6

		matriz = np.arange(nX*nY).reshape(nX, nY)
		mostrar_matriz(matriz,"matriz = np.arange(nX*nY).reshape(nX, nY)")

		# particiono la matriz
		m0 = matriz[ 0:int(nX/2), 0:int(nY/2) ]
		m1 = matriz[ int(nX/2):nX, 0:int(nY/2) ]
		m2 = matriz[ 0:int(nX/2), int(nY/2):nY ]
		m3 = matriz[ int(nX/2):nX, int(nY/2):nY ]

		print(f"{FR_MAG}\n============== Matrices partidas ==============={NO_COLOR}\n")

		mostrar_matriz(m0,"Matriz m0:  matriz[ 0:int(nX/2), 0:int(nY/2) ]")
		mostrar_matriz(m1,"Matriz m1:  matriz[int(nX/2):nX, 0:int(nY/2) ]")
		mostrar_matriz(m2,"Matriz m2:  matriz[ 0:int(nX/2), int(nY/2):nY ]")
		mostrar_matriz(m3,"Matriz m3:  matriz[ int(nX/2):nX, int(nY/2):nY ]")

		# Expandimos las matrices m0, m1, m2, m3
		m0e = expandir_matriz(m0, m1, m2, m3)
		m1e = expandir_matriz(m1, m0, m3, m2)
		m2e = expandir_matriz(m2, m3, m0, m1)
		m3e = expandir_matriz(m3, m2, m1, m0)

		print(f"{FR_MAG}\n====== Matrices expandidas ======{NO_COLOR}\n")
		mostrar_matriz(m0e,"m0e: expandir_matriz(m0, m1, m2, m3)")
		mostrar_matriz(m1e,"m1e: expandir_matriz(m1, m0, m3, m2)")
		mostrar_matriz(m2e,"m2e: expandir_matriz(m2, m3, m0, m1)")
		mostrar_matriz(m3e,"m3e: expandir_matriz(m3, m2, m1, m0)")

		# contraemos las matrices m0e, m1e, m2e, m3e
		m0c = contraer_matriz(m0e)
		m1c = contraer_matriz(m1e)
		m2c = contraer_matriz(m2e)
		m3c = contraer_matriz(m3e)

		print(f"{FR_MAG}\n====== Matrices contraidas ======\n{NO_COLOR}")

		mostrar_matriz(m0c,"m0c: contraer_matriz(m0e)")
		mostrar_matriz(m1c,"m1c: contraer_matriz(m1e)")
		mostrar_matriz(m2c,"m2c: contraer_matriz(m2e)")
		mostrar_matriz(m3c,"m3c: contraer_matriz(m3e)")

		print(f"{FR_GREEN}\n====== MATRIZ FINAL COMPLETA ======\n{NO_COLOR}")
		matrizFinal = np.hstack( (np.vstack( (m0c, m1c) ), np.vstack( (m2c, m3c) )) )
		mostrar_matriz(matrizFinal,"Matriz Final: np.hstack( (np.vstack( (m0c, m1c) ), np.vstack( (m2c, m3c) )) )")

		print(f"\n{FR_YELL}======== that's all ========{NO_COLOR}\n")
		pause()

	except Exception as Argument:
		error_msg = "ERROR IN <" + my_script_name + ">. SEE server_messages.txt !"
		write_log_file("my_messages.txt",error_msg)
		write_traceback_info_1(Argument,traceback,my_script_name)
		pause()     
	
else:
    # something wrong
    print(frRED("---- upsssssssss something is wrong ----"))
