"""  
1.- This code is to pass the exercises to the teacher
2.- The SCRIPT is for:
    2.1.-
    2-2.-
    .
    .

"""
#
# IMPORT SECTION
#
from MyFunc import *
from MyColors import *
from math import ceil
from os import  system

# CONSTANTS
# Colors
NO_COLOR = "\033[00m"
FR_RED   = "\033[91m"
FR_GREEN = "\033[92m"
FR_YELL  = "\033[93m"
FR_BLUE  = "\033[94m"
FR_MAG   = "\033[95m"

#
# ---------- COURSE EXCERCISE ----------
#

if __name__ == "__main__":

    system('cls')
    print(f"{FR_GREEN}---------- main ----------{NO_COLOR}")
    pause()    

    # first case 
    # function -> replace()
    texto = "Pitón es un lenguaje de programación. Pitón está usado para la automación, análisis de datos e incluso la creación de páginas webs. Pitón fue creado por Bill Gates en 1960. Pitón es difícil de usar."

    texto=texto.replace('Pitón','Python')
    texto=texto.replace('Bill Gates en 1960','Guido Van Rossum en 1989')
    texto=texto.replace('es difícil','es fácil')

    print(texto)

    # second case
    # functions -> swapcase, replace, upper, in, count, find, strip
    texto = "    Lo más importante que nos ha mantenido en Python... bueno, hay 2 cosas importantes. Uno son las bibliotecas. La otra cosa que nos mantiene en Python, y esto es lo más importante, es facil de leer y entender. Cuando contratamos nuevos empleados. Solo digo, 'todo lo que escribas debe estar en python'. Sólo para que pueda leerlo. Y es increíble porque puedo ver desde el otro lado de la habitación, mirando su pantalla, si su código es bueno o malo. Porque un buen código de Python tiene una estructura muy obvia. Y eso hace que mi vida sea mucho más fácil        "

    #Contar las veces que la palabra Python aparece en el texto...y si a veces aparece en el texto con mayusculas y minusculas - Python, python
    print(frGREEN(f"\toccurrences of the word 'Python': {texto.count('Python')}"))

    #Encuentras la ubicación (numero de carácter) donde esta la primera ocurrencia de la palabra Python. ¿Y la segunda?
    print(frGREEN(f"\tFirst occurrence of python -> {texto.find('Python')}"))
    print(frGREEN(f"\tSecond occurrence of python -> {texto.find('Python',texto.find('Python')+1)}"))

    #La palabra 'código' esta en el texto? Usar if ... in ...:
    if texto.find('codigo') > -1:
        print(frGREEN(f"La palabra 'código' SI está en el texto,y empieaza en la posición {texto.find('código')} 👌"))
    else: 
        print(frRED(f"La palabra 'código' NO está en el texto "))

    #Reemplazar Python por PYTHON
    texto = texto.replace('Python','\033[92mPYTHON\033[00m')
    print(f"{FR_YELL}Substitute Python with PYTHON{NO_COLOR}")
    print(texto + '')

    #Quitar los espacios
    texto = texto.strip()
    print(f"{FR_YELL}Delete spaces{NO_COLOR}")
    print(texto + '')

    #Cambiar la letra de todo el texto a "lO MÁS IMPORTANTE QUE NOS HA MANTENIDO EN pYTHON... "
    texto = texto.swapcase()
    print(f"{FR_YELL}Change letters with swapcase method{NO_COLOR}")
    print(texto + '')

    

else:
    # something wrong
    print(f"{FR_RED}---- upsssssssss something is wrong ---{NO_COLOR}")
