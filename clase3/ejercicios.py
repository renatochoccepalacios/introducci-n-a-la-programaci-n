# Escribir un programa que solicite al usuario su nombre completo y luego muestre la
# cantidad de vocales que contiene

""" nombre = input("escriba su nombre completo: ")
nombre = nombre.lower()
contador = 0

if "a" in nombre:
    contador += 1
if "e" in nombre:
    contador += 1
if "i" in nombre:
    contador += 1
if "o" in nombre:
    contador += 1
if "u" in nombre:
    contador += 1

print(f"el texto tiene {contador} vocales") """





# Escribir un programa que solicite al usuario ingresar su peso en kilogramos con
# decimales, y muestre por pantalla el peso expresado en kilogramos (incluyendo la
# palabra "kilogramos") y el peso expresado en gramos (incluyendo la palabra
# "gramos"). Ejemplo: ingresa: 70.5 Resultado: "Usted pesa 70.5 kilogramos o 70500
# gramos". 

""" ingresarPeso = float(input("ingrese un peso en decimal "))
multiplicador = 1000

print(f"Usted pesa {ingresarPeso} Kilogramos")
print(f"Usted pesa {int(ingresarPeso * multiplicador)} gramos") """


# Escribir un programa que solicite al usuario ingresar una palabra y luego muestre esa
# palabra al revés. Además, debe indicar si la palabra es un palíndromo. 

""" palabra = input("ingrese una palabra ")

print(palabra[::-1]) """


# Escribir un programa que solicite una frase al usuario y muestre solo los primeros 20
# caracteres de la frase. 

""" frase = input("ingrese una frase: ")
print(frase[0:20:1]) """

# Escribir un programa que solicite la hora actual en formato "hh:mm" y muestre por
# pantalla la hora, los minutos y los segundos por separado. Ejemplo: El usuario ingresa
# “14:35:20”, el programa debe mostrar: “Hora: 14 - Minutos: 35 - Segundos: 20”. 

""" horaActual = input("ingresa la hora actual: ")
horaActual = horaActual.split(":")

hora = horaActual[0]
minutos = horaActual[1]
segundos = horaActual[2]

# print(f"la hora es {hora[0:2]} Minutos: {hora[3:5]} Segundos: {hora[6:8]}")
print(f"la hora es {hora} Minutos: {minutos} Segundos: {segundos}") """


# Escribir un programa que permita el ingreso por teclado de una frase y la muestre por
# pantalla primero en minúsculas, luego en mayúsculas y por último con la primera
# letra de cada palabra en mayúscula

""" frase = input("ingrese una frase: ")

print(f"frase en minusculas: ", frase.lower())
print(f"frase en mayusculas: ", frase.upper())
print(f"Primera letra en Mayuscula: ",frase.capitalize()) """



# Escribir un programa que solicite al usuario ingresar un carácter y determine si es una
# vocal. 

""" caracter = input("escriba una vocal: ")

caracter = caracter.lower()


if "a" == caracter:
    print("es una vocal a")
elif "e" == caracter:
    print("es una vocal e")
elif "i" == caracter:
    print("es una vocal i")
elif "o" == caracter:
    print("es una vocal o")
elif "u" == caracter:
    print("es una vocal u")
else:
    print("no es una vocal") """

# Escribir un programa que permita el ingreso de un número, y si el número es mayor
# a 10, debe mostrar su cuadrado. 

""" numero = int(input("ingrese un numero: "))

if numero > 10:
    print(f"el cuadrado de {numero} es {numero **2}")
else :
    print(f"el numero no es mayor a 10") """

# Escribir un programa que permita ingresar una edad, y muestre un mensaje según el
# rango de edad. Condiciones:
# o Si la edad está entre 0 y 12: "Niño".
# o Si la edad está entre 13 y 17: "Adolescente".
# o Si la edad es 18 o más: "Adulto". 

""" edad = int(input("ingrese su edad: "))

if edad >= 0 and edad <= 12 :
    print("Sos un Niño")
elif edad >= 13 and edad <= 17:
    print("Sos un Adolescente")
elif edad >= 18 :
    print("Sos un Adulto") """


# Escribir un programa que solicite al usuario ingresar un número y determine si es
# positivo, negativo o cero.

""" numero = int(input("ingrese un numero: "))

if numero > 0 :
    print("es un numero positivo")
elif numero < 0 :
    print("es un numero negativo")
elif numero == 0 :
    print("el numero es igual a cero") """


#  Escribir un programa que permita al usuario ingresar un número del 1 al 7 y muestre
# el día de la semana correspondiente (1 para lunes, 2 para martes, etc.). 

""" numero = int(input("ingrese un numero: "))

if numero <= 7 :
    if numero == 1 :
        print("es lunes")
    elif numero == 2 :
        print("es martes")
    elif numero == 3 :
        print("es miercoles")
    elif numero == 4 :
        print("es jueves")
    elif numero == 5 :
        print("es viernes")
    elif numero == 6 :
        print("es sabado")
    elif numero == 7 :
        print("es domingo")
else :
    print("el numero ingresado debe ser del 1 al 7") """


# Escribir un programa que solicite al usuario ingresar la calificación de una tarea (entre
# 0 y 100) y determine el rango de la calificación. Condiciones:
# o Si la calificación está entre 0 y 59: "Insuficiente".
# o Si la calificación está entre 60 y 79: "Aceptable".
# o Si la calificación está entre 80 y 89: "Buena".
# o Si la calificación está entre 90 y 100: "Excelente"

""" calificacionTarea = int(input("ingrese la calificacion de una tarea entre 0 y 100: "))

if calificacionTarea >= 0 and calificacionTarea <= 100 :
    if calificacionTarea >= 0 and calificacionTarea <= 59:
        print("Insuficiente")
    elif calificacionTarea >= 60 and calificacionTarea <= 79:
        print("Aceptable")
    elif calificacionTarea >= 80 and calificacionTarea <= 89:
        print("Buena")
    elif calificacionTarea >= 90 and calificacionTarea <= 100:
        print("Excelente")
else :
    print("el numero ingresado debe ser entre 0 y 100") """


# Escribir un programa que solicite al usuario ingresar la temperatura actual en grados
# Celsius y determine si es un día frío (menos de 15°C), templado (entre 15°C y 25°C)
# o caluroso (más de 25°C). 

""" gradosCelsius = int(input("ingrese una temperatura: "))

if gradosCelsius < 15 :
    print("es un dia frio")
elif gradosCelsius >= 15 and gradosCelsius <= 25:
    print("Es un dia templado")
elif gradosCelsius > 25 :
    print("es un dia caluroso") """


# Escribir un programa que solicite al usuario ingresar una letra y determine si es una
# consonante. 

""" letra = input("ingrese una letra: ")

if "a" == letra:
    print("No es una consonante, es una vocal a")
elif "e" == letra:
    print("No es una consonante, es una vocal e")
elif "i" == letra:
    print("No es una consonante, es una vocal i")
elif "o" == letra:
    print("No es una consonante, es una vocal o")
elif "u" == letra:
    print("No es una consonante, es una vocal u")
else:
    print("es una consonante") """


# Escribir un programa que permita ingresar un número y determine si es divisible por
# 3 y por 5. 

""" numero = int(input("ingrese un numero: "))

if numero % 3 == 0:
    print("El numero de divisible por 3")
elif numero % 5 == 0 :
    print("El numero es divisible por 5")
else :
    print("el numero no es divisible por ninguno") """