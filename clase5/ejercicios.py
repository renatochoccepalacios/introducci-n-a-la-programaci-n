# Escribir un programa que muestre la palabra UNPAZ, letra por letra, y al finalizar la palabra
# “Universidad”, use “else”. 

""" palabra = "UNPAZ"

for x in palabra :
    print(x)
else :
    print("Universidad") """

# Escribir un programa que solicite una palabra y la muestre letra por letra separada por un
# guión, en una misma línea de texto (renglón), use “end”.
# por ejemplo:
# azul
# a-z-u-l

""" palabra = input("Ingrese una palabra: ")

for x in range(len(palabra)):

    if x == len(palabra) - 1 :
        print(palabra[x])
    else :
        print(palabra[x], end="-") """

# range(inicio, final, saltos)


# Escribir un programa que solicite una palabra y muestre el índice a partir del 1 de cada letra
# y la letra (puede utilizar acumulador o la función más avanzada vista en clases)
# por ejemplo:
# Hola
# 1 H
# 2 o
# 3 l
# 4 a 

""" palabra = input("Ingrese una palabra: ")
contador = 1
 
# #con contador
# for i in palabra :
#     print(f"{i} {contador}")
#     contador = contador + 1

# sin contador
for indice in range(len(palabra)) :
    print(f"{indice + 1} {palabra[indice]}") """


# Escribir un programa que solicite un número entero positivo, que muestre los múltiplos de 5
# que existen entre el número ingresado y su multiplicación por 30.
# por ejemplo: entre 3 y (3*30) 

""" numero = int(input("ingrese un numero: "))

for indice in range(numero, numero * 30 + 1):
    if indice % 5 == 0:
        print(indice) """


# Escribir un programa que solicite un número y repita un asterisco tantas veces como el
# número que ha ingresado, esto formará un triángulo
# por ejemplo: 3
# *
# **
# ***

""" numero = int(input("ingrese un numero: "))

for indice in range(1, numero + 1):
    print("*" * indice) """


# Vuelva a ejecutar el mismo programa, pero ahora con el triángulo dado vuelta
# por ejemplo: 3
# ***
# **
# * 

""" numero = int(input("ingrese un numero: "))

for indice in range(numero, 0, -1): # empieza en numero, termina en 1, va de -1 en -1
    print("*" * indice) """


# Escribir un programa que solicite tres números uno a la vez, verifique y muestre cada vez si
# este es un número negativo o es un número de 1, 2, 3 cifras o más. 

""" numero1 = int(input("ingrese el primer numero: "))


if numero1 < 0 :
    print(f"el numero {numero1} es negativo")
    print(f"tiene {len(numero1)} cifras")
else :
    print(f"el numero {numero1} es positivo")
    print(f"tiene {len(numero1)} cifras") """



# Escribir un programa que muestre los elementos de la siguiente lista
# ['Jose','Pedro','Armando','Analía','Florencia']

""" array = ['Jose','Pedro','Armando','Analía','Florencia']

for indice in range(len(array)) :
    print(f"{indice + 1} {array[indice]}") """


# Escribir un programa que enumere los nombres de la lista anterior del ejercicio 38. utilice la
# función vista en clase. 

""" array = ['Jose','Pedro','Armando','Analía','Florencia']

for indice, contenido in enumerate(array) : 
    print(f"{indice} {contenido}") """



# Escribir un programa que muestre el nombre más largo de la lista del ejercicio 38. utilice len()

""" array = ['Jose','Pedro','Armando','Analía','Florencia']

nombreLargo = ""
longitudMax = 0

for nombre in array :
    if len(nombre) > longitudMax :
        longitudMax = len(nombre)
        nombreLargo = nombre

print(f"el nombre mas largo es {nombreLargo} con {longitudMax} letras") """


# Escribir un programa que solicite un número y calcule la tabla de multiplicar de ese número
# hasta el 10. 

pedirNumero = int(input("ingrese un numero: "))

for indice in range(1, 10 + 1, 1) :
    print(f"{pedirNumero} x {indice} = {indice * pedirNumero}")