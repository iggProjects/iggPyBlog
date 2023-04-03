#!/usr/bin/env python3

#
# 	Arithmetical Progression
#   An = A1 + (n-1) * d
#   Suma(n primeros términos) = (n * ( 2*A1 + (n-1)*d )) / 2  =  n * (A1 + An) / 2
#

#
# Buscador -> https://duckduckgo.com
# bUSQUEDA:  python multiprocessing cpu id
# Resultado: https://stackoverflow.com/questions/10190981/get-a-unique-id-for-worker-in-python-multiprocessing-pool#10192611
# Atencion: multiprocessing.current_process()
#

import multiprocessing
import time
import sys
from os import system

# CONSTANTS

# Colors
NO_COLOR = "\033[00m"
FR_RED   = "\033[91m"
FR_GREEN = "\033[92m"
FR_YELL  = "\033[93m"
FR_BLUE  = "\033[94m"
FR_MAG   = "\033[95m"

# param 1_ elemento inicial de la sucesión
ELEM_INIC = 1
# param 2: razón inicial
RAZON_INIC = 1
# param 3: número de términos a sumar
N_TER = 10000 
# param 4: número de sucesiones a calcular
N_SUCESIONES = 100
# param 5: número de CPU's a usar
N_CPUS = 4
# Número para fijar frecuencia de prints
BASE = int(N_SUCESIONES / 10)

# place thousands separator
def place_comma(numb):
    return ("{:,}".format(numb))

count = 0
		
# Suma de una progresión artimética de radio d y primer elemento a
def suma_AP(d):
# def suma_AP(d,n):
	global count_print, count
	resultado = sum(ELEM_INIC + i*d for i in range(0,N_TER))
	# if para imprimir pocos registros 
	if ( (count) % (BASE) == 0):
		#count_print += 1
		pid=str(multiprocessing.Process.pid)
		name=str(multiprocessing.Process.name)
		print(f"\nPrint {count} | razón {d} -> Proceso: {pid} | nombre: {name}\n\t{FR_GREEN}====== SUMA DE LA PROGRESIÓN: {place_comma(resultado)} ======{NO_COLOR}")
	count += 1

# Ejecuta la suma para una lista de razones, todas con el mismo elemento inicial 
def suma(lista,N_CPUS):	
	print(f"multiprocessing pool: {multiprocessing.Pool(N_CPUS)} | var type: {type(multiprocessing.Pool(N_CPUS))}")
	with multiprocessing.Pool(N_CPUS) as pool:
		print(f"\t{FR_RED}===== pool : {pool}{NO_COLOR} =====")
		pool.map(suma_AP,lista)
		# pool.map(suma_AP,lista,N_TER)

#
# PROGRAMA
#

if __name__ == '__main__':
	# hora inicio
	inicio = time.time()
	system('cls')

	# Lista de n razones para las n sucesiones
	lista_razones = [(RAZON_INIC + 2*x) for x in range(0, N_SUCESIONES)]

	# CALL multiprocessing function
	suma(lista_razones,N_CPUS)

	# cálculo aprox de operaciones aritméticas
	oper_arit = 2 * N_SUCESIONES * N_TER

	duracion = time.time() - inicio
	dur_5_dec = "{:.5f}".format(duracion)

	print(f"\n{FR_RED}-----------BALANCE--------------{NO_COLOR}\n")		

	print(f"\n{place_comma(N_SUCESIONES)} Sucesiones | Elem Inicial {ELEM_INIC} | No Términos {place_comma(N_TER)}\n")
	print(f"{FR_GREEN}======= Lista razones para las sucesiones ======={NO_COLOR}\n{lista_razones}")
	print(f"\nNo CPU's: {N_CPUS} | Estimado operac aritmeticas: {place_comma(oper_arit)} | Nro prints teóricos: {place_comma(int(N_SUCESIONES/BASE))}")
	print(f"\n{FR_GREEN}Duracion proceso sin incluir tiempo impresión BALANCE: {dur_5_dec} segundos{NO_COLOR}\n")

	print(f"{FR_YELL}======== that's all ========{NO_COLOR}\n")