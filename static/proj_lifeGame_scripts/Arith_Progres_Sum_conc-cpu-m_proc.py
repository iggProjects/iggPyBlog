#!/usr/bin/env python3

#
# Arithmetical Progression
#   An = A1 + (n-1) * d
#   Suma(n primeros términos) = (n * ( 2*A1 + (n-1)*d )) / 2  =  n * (A1 + An) / 2
#

import multiprocessing
import time
import sys
#
# Buscador -> https://duckduckgo.com
# bUSQUEDA:  python multiprocessing cpu id
# Resultado: https://stackoverflow.com/questions/10190981/get-a-unique-id-for-worker-in-python-multiprocessing-pool#10192611
# Atencion: multiprocessing.current_process()
#
# place thousands separator
def place_comma(numb):
    return ("{:,}".format(numb))

count = 0
count_print = 0
		
# Suma de una progresión artimética de radio d y primer elemento a
def suma_AP(d):
# def suma_AP(d,n):
	global count_print, count
	resultado = sum(razon_inic + i*d for i in range(0,n_ter))
	# if para imprimir pocos registros 
	if ( (count+1) % (base) == 0):
		count_print += 1
		# pid=str(multiprocessing.Process.pid)
		# name=str(multiprocessing.Process.name)
		print(f"prints cada {base} sucesiones | print No: {place_comma(count_print)} ({count+1}) | razon: {place_comma(d)} | suma:{place_comma(resultado)}")

		#	print(f"prints cada {base} sucesiones | print No: {place_comma(count)} ({count+1}) | razon: {place_comma(d)} | suma:{place_comma(resultado)} {pid} <--> {name}")
	count += 1
	# return resultado

# Ejecuta la suma para una lista de razones y primeros elementos 
def suma(lista,n_ter,n_cpus):
	with multiprocessing.Pool(n_cpus) as pool:
		pool.map(suma_AP,lista)
		# pool.map(suma_AP,lista,n_ter)

#
# PROGRAMA
#

if __name__ == '__main__':

	# Parametros

	# param 1: razón inicial
	razon_inic = int(sys.argv[1])
	# param 2: número de términos a sumar
	n_ter = int(sys.argv[2]) 
	# param 3: número de sucesiones a calcular
	n_sucesiones = int(sys.argv[3])
	# param 4: número de CPU's a usar
	n_cpus = int(sys.argv[4])

	# Lista de n razones para las n sucesiones
	lista_razones = [razon_inic + 2*x for x in range(0, n_sucesiones)]

	# Intervalo para Prints  
	base = int(n_sucesiones / 10)

	inicio = time.time()

	# CALL multiprocessing function
	suma(lista_razones,n_ter,n_cpus)

	duracion = time.time() - inicio

	# cálculo razón de la sucesión final (para mostrarla)
	razon_fin = lista_razones[n_sucesiones-1]

	# cálculo aprox de operaciones aritméticas
	oper_arit = 2*n_sucesiones*n_ter

	# print(f"lista de razones: {lista_razones} ")
	print(f"-----------BALANCE--------------")
	print(f"Nro prints teóricos: {place_comma(int(n_sucesiones/base))} | nro prints: {count_print}")
	print(f"razon 1ra Suc: {razon_inic} | razon ult Suc: {place_comma(razon_fin)} | nro términos a sumar: {n_ter} | nro sucesiones: {place_comma(n_sucesiones)}")
	print(f"numb PCU: {n_cpus} | estimado operac aritmeticas: {place_comma(oper_arit)}")

	duracion = time.time() - inicio
	print(f"Duracion {duracion} segundos")
