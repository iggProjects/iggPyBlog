# teacher example

# IMPORT FUNCTIONS
from MyFunc_ForTeacher import pause

texto = "programazioa gustatzen zait"

# numero de caracteres
print(len(texto))
# la primera caracter en mayúsculo
print(texto.capitalize())
# mayúsculos - lo opuesto en lower()
print(texto.upper())
pause()

# strip espacios
s = "    Hola.       "
s = s.strip()   # tambien hay lstrip, rstrip
print("X" + s + "X")
pause()

t = "###hola###"
t = t.strip("#")
print("X" + t + "X")
pause()

u = "Hola a todos todos todos"
u = u.replace("todos", "TODOS")
print(u)
pause()

#split
nombre_completo = "jon#smith"
nombres = nombre_completo.split("#")
print(type(nombres))
nombre, apellido = nombre_completo.split("#")
print(type(nombre), type(apellido))
pause()

# multi-linea con \n
print("programazioan\ngustatzen\nzait")
# substring
print(texto[13:22])
# los primeros 10 caracteres
print(texto[:12])
# al reves
print(texto[::-1])
pause()

# imprimir todo 5 veces
print(texto*5)
pause()

# imprimir cada cáracter en una linea
#for s in texto:
#   print(s)

# quitar espacios
texto = "     programazioa gustatzen zait.   "
print("X" + texto + "X")
print("X" + texto.strip() + "X")
pause()

BUSCAR = "gustatZEN"
if BUSCAR in texto:
    print("Encontrado")
else:
    print("No encontrado")
pause()
    
tuple = ("Jon", "Maria", "Antonio")
a = "$".join(tuple)
print(a)
pause()

z  = "abc"
y = " ".join(z)
print(y)
pause()

# recibe un carácter y devuelve su representación en código unicode
print(ord("ñ"))
# recibe un número y devuelve su representación como carácter
print(chr(241))
pause()

##########################################
# RETO respuesta - encriptar y descifrar
texto = "Texto para encriptar"
lista = []

# usar lista.append() para agregar los números a la lista
for i in texto:
    lista.append(ord(i) + 10)

# mostrar la lista de la cadena cifrado

# ahora descifra la lista - los números unicode de cada carácter esta en la lista
for j in range(0, len(lista)):
   print(chr(lista[j]-10), end=" ")
pause()
    
# RETO respuesta - Amazon sistema de registro
# Palabras para excluir de la contraseña. Hay mejoras formas de hacer eso, con una lista, por ejemplo....
EXCLUDE1 = "password"
EXCLUDE2 = "contraseña"
EXCLUDE3 = "123456"

nombre = input("Cúal es tu nombre?")
apellido = input("Cúal es tu apellido?")
usuario = input("Introducir un nombre de usuario (mínimo 5 carácteres):")
password = input("Introducir la contraseña (mínimo 6 carácteres, sin palabras típicas):")

if len(usuario) < 5:
    print("Por favor, vuelve a introducir un usuario.")
elif len(password) < 6:
    print("Por favor, vuelve a introducir una contraseña.")
elif EXCLUDE1 in password.lower() or EXCLUDE2 in password.lower() or EXCLUDE3 in password:
    print(f"Por favor, vuelve a introducir una contraseña sin palabras claves como {password}.")
else:
    print(f"Bienvenidos a Amazon {nombre.capitalize()}, {apellido.capitalize()}.")
pause()    
    
  
# convertir 122,Python,es,64,un,777,lenguaje,222,de,55,66,programacion a Python es un lenguaje de programacion
text = "   122,Python,es,64,un,777,lenguaje,222,de,55,66,programacion    "
text = text.strip()

print("X" + text + "X")
lista = text.split(",")

print(type(lista))
print(lista)
print(type(lista[0]))
texto_lista = [i for i in lista if not i.isnumeric()]  # list comprehension
print(texto_lista)
pause()

# opcion 1
texto_final1 = ""
for i in texto_lista:
  texto_final1 = texto_final1 + " " + i
print(texto_final1.strip())
pause()

# opcion 2
texto_final2 = " ".join(str(i) for i in texto_lista)
print(texto_final2)
pause()

# Generar un informe con:
# - los nombres de los usuarios
# - los dominios únicos (sin repetir el dominio)
emails = ["jon.smith@microsoft.com", "maria.fernandez@microsoft.com", "david@microsoft.com", "isabel@microsoft.es","alfonso@gmail.com"]


dominios = []
for email in emails:
  nombre, dominio = email.split("@")
  print(nombre)
  if dominio not in dominios:
    dominios.append(dominio)

print(dominios)
pause()

# con los nombres, generar un texto en format CSV con nuevos correos e.g maria@nazaret.eus,jon@nazaret.eus,david@nazaret.eus
nombres = ("maria", "jon", "david")
DOMINIO = "@nazaret.eus"
correos = []
for nombre in nombres:
  correo = nombre + DOMINIO
  correos.append(correo)

texto = ",".join(correos)
print(texto)

pause()



#********************************************

# Generar un informe con:
# - los nombres de los usuarios
# - los dominios únicos (sin repetir el dominio)

print()

dominios = []
for email in emails:
  nombre, dominio = email.split("@")
  print(nombre)
  if dominio not in dominios:
    dominios.append(dominio)

print(f"\ndominios -> {dominios}\n")

# con los nombres, generar un texto en format CSV con nuevos correos e.g maria@nazaret.eus,jon@nazaret.eus,david@nazaret.eus

nombres = ("maria", "jon", "david")
DOMINIO = "@nazaret.eus"
correos = []
for nombre in nombres:
  correo = nombre + DOMINIO
  correos.append(correo)

texto = ",".join(correos)
print(f"texto \n")