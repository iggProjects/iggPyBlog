#
#  Execute Sets of 4 "Games of life", 1 for each quadrant, with multiprocessing.
#

# IMPORT SECTION

try:   # Import My Own Functions from include dir 
	import sys, traceback, time, multiprocessing
	#from multiprocessing.pool import ThreadPool as Pool
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

	#
	# Constantes
	#

	NX = 10
	NY = 24
	NITER= 50
	MSG_TEXT  = 'Games record-> '
	BASE_PRINT = 25
	#BASE_PRINT = int(NITER/10)
	#N_CPU = multiprocessing.cpu_count()

except Exception as ImportError:
    FR_RED   = "\033[91m" 
    NO_COLOR = "\033[00m"
    print("print empty line") 
    print(f"\033[91mIMPORT ERROR ==>\033[00m {ImportError} | {ImportError.__class__} | {ImportError.__doc__}")

#
# Funciones
#

# Execute 4 matrixes (games) simultaneously 
def exec_4_game(game):
	
	try:
		print(f"{FR_GREEN}COMMENT:Set {game} | cpu name: {multiprocessing.current_process().name} | mp-name: {multiprocessing.Process().name}")
		
		# Inicializo la matriz con ceros y luego se convierte en matrix de 0 y 1 al azar
		#matriz1 = crear_matriz()
		matriz1 = np.zeros((NX, NY))					 	
		matriz1 = np.random.randint(2, size=(NX, NY))
		#matriz2 = crear_matriz()
		matriz2 = np.zeros((NX, NY))					 	
		matriz2 = np.random.randint(2, size=(NX, NY))
		#matriz3 = crear_matriz()
		matriz3 = np.zeros((NX, NY))					 	
		matriz3 = np.random.randint(2, size=(NX, NY))		
		#matriz4 = crear_matriz()
		matriz4 = np.zeros((NX, NY))					 	
		matriz4 = np.random.randint(2, size=(NX, NY))

		n=1
		while n <= NITER:	  
		# while n<= nIter or [CONDICION DE MATRIZ IDENTICA ENTRE DOS ITER]:	  

			#matriz1 = exec_game_iter(matriz1,'matriz1')

			# Copio la matriz para poner en ella los cambios
			matrizTemp = np.copy(matriz1)

			# Recorro la matriz para aplicar reglas a la matrizTemp
			for x in range(0, NX):
				for y in range(0, NY):
					# Numero de Vecinos
					nVecinos = matriz1[	(x-1)%NX, (y-1)%NY ] 		\
									+ matriz1[	(x)%NX, 	(y-1)%NY ] 		\
									+ matriz1[	(x+1)%NX, (y-1)%NY ] 		\
									+ matriz1[	(x-1)%NX, (y)%NY ] 			\
									+ matriz1[	(x+1)%NX, (y)%NY ] 			\
									+ matriz1[	(x-1)%NX, (y+1)%NY ] 		\
									+ matriz1[	(x)%NX, 	(y+1)%NY ] 		\
									+ matriz1[	(x+1)%NX, (y+1)%NY ]

					# Regla 1: celda muerta (0) con 3 vecinas revive (1)
					if matriz1[x,y] == 0 and nVecinos == 3:
						matrizTemp[x,y] = 1
					
					# Regla 2: celda viva (1) con mas de 3 vecinas o menos de 2 muere (2)
					elif matriz1[x,y] == 1 and ( nVecinos < 2 or nVecinos > 3 ):
						matrizTemp[x,y] = 0
			
			# try to control event pf equal matrixes
			if np.array_equal(matriz1,matrizTemp):
				if "PoolWorker-1" in multiprocessing.current_process().name:			
					print(f"{FR_GREEN}COMMENT:cpu id: {multiprocessing.current_process().name} | {multiprocessing.Process().name} | obs:game-reach-equality_in_matriz1")
				matriz1 = 9 * np.ones([NX,NY])
			else:	
				# Copio matrizTemp en matriz para la proxima iteracion
				matriz1 = np.copy(matrizTemp)

			############################################
			#matriz2 = exec_game_iter(matriz2,'matriz2')
			############################################

			# Copio la matriz para poner en ella los cambios
			matrizTemp = np.copy(matriz2)

			# Recorro la matriz para aplicar reglas a la matrizTemp
			for x in range(0, NX):
				for y in range(0, NY):
					# Numero de Vecinos
					nVecinos = matriz2[	(x-1)%NX, (y-1)%NY ] 		\
									+ matriz2[	(x)%NX, 	(y-1)%NY ] 		\
									+ matriz2[	(x+1)%NX, (y-1)%NY ] 		\
									+ matriz2[	(x-1)%NX, (y)%NY ] 			\
									+ matriz2[	(x+1)%NX, (y)%NY ] 			\
									+ matriz2[	(x-1)%NX, (y+1)%NY ] 		\
									+ matriz2[	(x)%NX, 	(y+1)%NY ] 		\
									+ matriz2[	(x+1)%NX, (y+1)%NY ]

					# Regla 1: celda muerta (0) con 3 vecinas revive (1)
					if matriz2[x,y] == 0 and nVecinos == 3:
						matrizTemp[x,y] = 1
					
					# Regla 2: celda viva (1) con mas de 3 vecinas o menos de 2 muere (2)
					elif matriz2[x,y] == 1 and ( nVecinos < 2 or nVecinos > 3 ):
						matrizTemp[x,y] = 0
			
			# try to control event pf equal matrixes
			if np.array_equal(matriz2,matrizTemp):
				if "PoolWorker-1" in multiprocessing.current_process().name:			
					print(f"{FR_GREEN}COMMENT:cpu id: {multiprocessing.current_process().name} | {multiprocessing.Process().name} | obs:game-reach-equality_in_matriz2")
				matriz2 = 9 * np.ones([NX,NY])
			else:	
				# Copio matrizTemp en matriz para la proxima iteracion
				matriz2 = np.copy(matrizTemp)


			############################################
			#matriz3 = exec_game_iter(matriz3,'matriz3')
			############################################

			# Copio la matriz para poner en ella los cambios
			matrizTemp = np.copy(matriz3)

			# Recorro la matriz para aplicar reglas a la matrizTemp
			for x in range(0, NX):
				for y in range(0, NY):
					# Numero de Vecinos
					nVecinos = matriz3[	(x-1)%NX, (y-1)%NY ] 		\
									+ matriz3[	(x)%NX, 	(y-1)%NY ] 		\
									+ matriz3[	(x+1)%NX, (y-1)%NY ] 		\
									+ matriz3[	(x-1)%NX, (y)%NY ] 			\
									+ matriz3[	(x+1)%NX, (y)%NY ] 			\
									+ matriz3[	(x-1)%NX, (y+1)%NY ] 		\
									+ matriz3[	(x)%NX, 	(y+1)%NY ] 		\
									+ matriz3[	(x+1)%NX, (y+1)%NY ]

					# Regla 1: celda muerta (0) con 3 vecinas revive (1)
					if matriz3[x,y] == 0 and nVecinos == 3:
						matrizTemp[x,y] = 1
					
					# Regla 2: celda viva (1) con mas de 3 vecinas o menos de 2 muere (2)
					elif matriz3[x,y] == 1 and ( nVecinos < 2 or nVecinos > 3 ):
						matrizTemp[x,y] = 0
			
			# try to control event pf equal matrixes
			if np.array_equal(matriz3,matrizTemp):
				if "PoolWorker-1" in multiprocessing.current_process().name:			
					print(f"{FR_GREEN}COMMENT:cpu id: {multiprocessing.current_process().name} | {multiprocessing.Process().name} | obs:game-reach-equality_in_matriz3")
				matriz3 = 9 * np.ones([NX,NY])
			else:	
				# Copio matrizTemp en matriz para la proxima iteracion
				matriz3 = np.copy(matrizTemp)

			############################################
			#matriz4 = exec_game_iter(matriz4,'matriz4')
			############################################

			# Copio la matriz para poner en ella los cambios
			matrizTemp = np.copy(matriz4)

			# Recorro la matriz para aplicar reglas a la matrizTemp
			for x in range(0, NX):
				for y in range(0, NY):
					# Numero de Vecinos
					nVecinos = matriz4[	(x-1)%NX, (y-1)%NY ] 		\
									+ matriz4[	(x)%NX, 	(y-1)%NY ] 		\
									+ matriz4[	(x+1)%NX, (y-1)%NY ] 		\
									+ matriz4[	(x-1)%NX, (y)%NY ] 			\
									+ matriz4[	(x+1)%NX, (y)%NY ] 			\
									+ matriz4[	(x-1)%NX, (y+1)%NY ] 		\
									+ matriz4[	(x)%NX, 	(y+1)%NY ] 		\
									+ matriz4[	(x+1)%NX, (y+1)%NY ]

					# Regla 1: celda muerta (0) con 3 vecinas revive (1)
					if matriz4[x,y] == 0 and nVecinos == 3:
						matrizTemp[x,y] = 1
					
					# Regla 2: celda viva (1) con mas de 3 vecinas o menos de 2 muere (2)
					elif matriz4[x,y] == 1 and ( nVecinos < 2 or nVecinos > 3 ):
						matrizTemp[x,y] = 0
			
			# try to control event pf equal matrixes
			if np.array_equal(matriz4,matrizTemp):
				if "PoolWorker-1" in multiprocessing.current_process().name:			
					print(f"{FR_GREEN}COMMENT:cpu id: {multiprocessing.current_process().name} | {multiprocessing.Process().name} | obs:game-reach-equality_in_matriz1")
				matriz4 = 9 * np.ones([NX,NY])
			else:	
				# Copio matrizTemp en matriz para la proxima iteracion
				matriz4 = np.copy(matrizTemp)


			if ( ( "PoolWorker-1" in multiprocessing.current_process().name) and (n % BASE_PRINT == 0) ):
				print("print empty line")
				print(f"{FR_GREEN}COMMENT:cpu name: {multiprocessing.current_process().name} | {multiprocessing.Process().name} | iteration: {n}")

				#show_4_matrix(matriz1,matriz2,matriz3,matriz4)
				X, Y = NX, NY

				for x in range(0, 2*X+1):
					for y in range(0, 2*Y+1):
						
						# matriz1  (1er cuadrante)
						if x<X and y<Y:
							if matriz1[x,y] == 1:
								print(f"{int(matriz1[x,y])}", end ="")
							else:
								print(f"{int(matriz1[x,y])}", end ="")
						
						#separación entre matrices 1 y 2
						if y == Y and x != X:
							print(f"777", end ="")
						
						# matriz2	(2do cuadrante)	
						if ( x<X ) and ( y > Y ):
							if matriz2[x,(y-Y-1)] == 1:
								print(f"{int(matriz2[x,y-Y-1])}", end ="")
							else:
								print(f"{int(matriz2[x,y-Y-1])}", end ="")

						# línea entre matrices 1 y 2 con 3 y 4
						if x == X:
							print(f"7", end ="")
						
						# matriz3 (3er cuadrante)
						if ( x>X ) and ( y<Y ):
							if matriz3[x-X-1,y] == 1:					
								print(f"{int(matriz3[x-X-1,y])}", end ="")
							else:					
								print(f"{int(matriz3[x-X-1,y])}", end ="")	

						#matriz4 (4to cuadrante)
						if ( x>X ) and ( y>Y ):
							if matriz4[x-X-1,y-Y-1] == 1:
								print(f"{int(matriz4[x-X-1,y-Y-1])}", end ="")
							else:
								print(f"{int(matriz4[x-X-1,y-Y-1])}", end ="")
						
					print()

				#time.sleep(SLEEP)			
			n+=1

		print("print empty line")
		print(f"{FR_GREEN}COMMENT:{multiprocessing.current_process().name}: Set {game} finished | {NITER} iterat for each game | games: 4 | total-iterat {NITER*4}")
	
	except Exception as Argument:
		error_msg = "ERROR IN function <exec_4_game>. SEE server_messages.txt !"
		write_log_file("my_messages.txt",error_msg)
		write_traceback_info_1(Argument,traceback,"function exec_4_game")


##############################################################
#                         MAIN                               # 
##############################################################

# COLUMNS & LINES console screen
# NY, NX = os.get_terminal_size(0)		
# print(f"cols: {os.get_terminal_size(0)[0]} , rows:  {os.get_terminal_size(0)[1]} ")
# Ajusto por espacios e indicador de iteraciones
# NX, NY = NX-22, int(NY/2)-1				  

if __name__ == '__main__':

	try:

		my_script = __file__.split('\\')
		my_script_name = my_script[len(my_script)-1]
		write_log_file("my_messages.txt","IN '" + my_script_name + "'")

		# READ PARAMETERS 
		# number of SET's, each of one of four games (matrixs)
		nSets = 2
		#nSets = int(sys.argv[1])
		# number of CPU in multiprocessing call
		nCPU = 2
		#nCPU = int(sys.argv[2])

		# parameter for multiporcessing call
		list_games = [(x+1) for x in range(0,nSets)]

		# time
		inicio = time.time()

		# CALL MULTIPROCESSING
		try: 

			#print("print empty line")
			print(f"{FR_BLUE}= = = = = LG MP = = = = =")
			print(f"{FR_RED}= = = GAME PARAMETERS = = = ")
			print(f"{FR_GREEN}. . . . Number Sets for 4 simultaneous Life_Game_Matrix: {len(list_games)}")
			print(f"{FR_GREEN}. . . . Iterations for each game: {NITER}")
			print(f"{FR_GREEN}. . . . number of cpus participating: {nCPU}")
			print(f"{FR_GREEN}. . . . matrices {NX} x {NY}")
			print(f"{FR_GREEN}. . . . Printing only for first process")
			print(f"{FR_GREEN}. . . . List of Sets: {list_games}")


			#exec_games(list_games,nCPU)

			with multiprocessing.Pool(nCPU) as pool:
				pool.map(exec_4_game,list_games)


			# BALANCE
			print(f"print empty line")
			print(f"{FR_YELL}- - - - - BALANCE - - - - -")
			print(f"{FR_GREEN}. . . . Number of cpus participating: {nCPU}")
			print(f"{FR_GREEN}. . . . Sets executed: {list_games[nSets-1]}")
			print(f"{FR_GREEN}. . . . Games executed: {list_games[nSets-1]*4}")
			print(f"{FR_GREEN}. . . . Each game (matrix) includes {NITER} iterations of game of life")
			print(f"{FR_GREEN}\twith a matrix of {NX} x {NY} in each quadrant of the screen")
			print(f"{FR_GREEN}\tand only {int(NITER/BASE_PRINT)} print screens for each game (matrix) of the first process")
			
			elapsed_time = "{:.2f}".format(time.time()-inicio)
			print(f"print empty line")
			print(f"{FR_GREEN}. . . . Elapsed Time: {elapsed_time} seconds")
			print(f"print empty line")
			print(f"{FR_GREEN}- - - - - THAT's-ALL - - - - - THAT's-ALL - - - - - ")
			print(f"print empty line")

		except Exception as Argument:
			error_msg = "ERROR IN function <exec_games>. SEE server_messages.txt !"
			write_log_file("my_messages.txt",error_msg)
			write_traceback_info_1(Argument,traceback,"function exec_games")
			
	except Exception as Argument:
		error_msg = "ERROR IN <" + my_script_name + ">. SEE server_messages.txt !"
		write_log_file("my_messages.txt",error_msg)
		write_traceback_info_1(Argument,traceback,my_script_name)

else:
    # new thread
    print(frRED("---- LG MP new thread ----"))
