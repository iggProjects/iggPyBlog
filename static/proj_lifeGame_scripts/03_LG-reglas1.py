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


# CONSTANTS

ITERAC = 50
nX = 10
nY = 16
yExt = 2*nY + 1
# nX, nY = os.get_terminal_size(0)
# nX, nY = int(nX/2)-5, (nY-5)

#
# Funciones
#

def mostrar_matriz(matriz):
	# os.system('clear')
	X, Y = matriz.shape
	for x in range(0, X):
		for y in range(0, Y):
			if matriz[x,y] == 1:
				print(f"{int(matriz[x,y])}", end =" ")
			elif matriz[x,y] == 0:
				print(f"{int(matriz[x,y])}", end =" ")
			elif matriz[x,y] == 9:
				print(f"{int(matriz[x,y])}", end =" ")
			else:
				print(f"{int(matriz[x,y])}", end =" ")
				 	 	
		print()
	print("print empty line")

#
# MAIN
#

if __name__ == "__main__":

	try:

		my_script = __file__.split('\\')
		my_script_name = my_script[len(my_script)-1]
		#print(f".....my_script_name: {my_script_name}")
		write_log_file("my_messages.txt","IN '" + my_script_name + "'")

		matriz  = np.random.randint(2, size=(nX, nY))
		matriz_ext = np.zeros((nX,yExt))

		for x in range(0,nX):
			for y in range(0,nY):
				matriz_ext[x,y] = matriz[x,y]

				nVecinos = matriz[ x-1, y-1 ]    \
								+ matriz[ x, y-1 ]    \
								+ matriz[ (x+1)%(nX), y-1 ]    \
								+ matriz[ x-1, y ]      \
								+ 0 * matriz[ x, y ]      \
								+ matriz[ (x+1)%nX, y ]      \
								+ matriz[ x-1, (y+1)%nY ]    \
								+ matriz[ x,   (y+1)%nY ]    \
								+ matriz[ (x+1)%nX, (y+1)%nY ]
				
				matriz_ext[x,y+nY+1] = nVecinos

		for x in range (0,nX):
			matriz_ext[x,nY] = 9

		n=1
		while n <= ITERAC:
			matrizTemp = np.copy(matriz_ext)
			# mostrar_matriz(matrizTemp)
			# print()

			for x in range(0, nX):
				for y in range(0, nY):

					if matriz_ext[x,y] == 0 and matriz_ext[x,y+nY+1] == 3:
						matrizTemp[x,y] = 1

					elif matriz_ext[x,y] == 1 and ( matriz_ext[x,y+nY+1]  < 2 or matriz_ext[x,y+nY+1] > 3 ):
						matrizTemp[x,y] = 0
						
			for x in range(0, nX):
				for y in range(0, nY):

					nVecinos = matrizTemp[ (x-1)%nX, (y-1)%nY ]    \
									+ matrizTemp[ x, (y-1)%nY ]    \
									+ matrizTemp[ (x+1)%(nX), (y-1)%nY ]    \
									+ matrizTemp[ (x-1)%nX, y ]      \
									+ 0 * matrizTemp[ x, y ]      \
									+ matrizTemp[ (x+1)%nX, y ]      \
									+ matrizTemp[ (x-1)%nX, (y+1)%nY ]    \
									+ matrizTemp[ x,   (y+1)%nY ]    \
									+ matrizTemp[ (x+1)%nX, (y+1)%nY ]
				
					matrizTemp[x,y+nY+1] = nVecinos

			matriz_ext = np.copy(matrizTemp)
			#print(f"-----MatrizGameLife----------MatrizNumVecinos----")
			if n==1:
				print(f"MATRIZ-INICIAL-{nX}x{nY}-Acompañada-Matriz-Nro-Vecinos")	
				mostrar_matriz( matriz_ext )		
				#print(f"-----MatrizGameLife----------MatrizNumVecinos-----")	
			elif n % 2 == 0:
				print(f"Iterac--{n}--matriz-{nX}x{nY}")	
				#print(f"----MatrizGameLife----------MatrizNumVecinos-----")		
				mostrar_matriz( matriz_ext )

			n += 1

		print(f"\n{FR_YELL}======== that's all ========{NO_COLOR}\n")		

	except Exception as Argument:
		error_msg = "ERROR IN <" + my_script_name + ">. SEE server_messages.txt !"
		write_log_file("my_messages.txt",error_msg)
		write_traceback_info_1(Argument,traceback,my_script_name)
		
	
else:
    # something wrong
    print(frRED("---- upsssssssss something is wrong ----"))
