#Hola Mundo: Escribir un programa que muestre por pantalla "¡Hola Mundo!".
# print("¡Hola Mundo!")


#Bienvenida personalizada: Escribir un programa que pida al usuario su nombre y muestre un saludo personalizado. 

# nombre = input("ingrese un nombre ")
# print(f"Hola como estas? {nombre}")



# Operaciones básicas: Crear un programa que realice y muestre la suma, resta,
# multiplicación y división de dos números.

# num1 = int(input("ingrese un numero "))
# num2 = int(input("ingrese un el segundo numero "))

# suma = num1 + num2
# resta = num1 - num2
# multiplicacion = num1 * num2


# print(f"la suma entre {num1} y {num2} es de {suma}")
# print(f"la resta entre {num1} y {num2} es de {resta}")
# print(f"la multiplicación entre {num1} y {num2} es de {multiplicacion}")



# Formato de dirección: Crear un programa que pida al usuario su dirección y la muestre en
# un formato específico

# direccion = input("ingrese su direccion ")
# numero = int(input("ingrese el numero de su localidad "))

# print("su dirección es {} y su numero es {}".format(direccion, numero))




#Variables y constantes 

# Valores iniciales: Escribir un programa que asigne y muestre el valor de tres variables diferentes. 

# nota1 = int(input("ingrese el primer valor "))
# nota2 = int(input("ingrese el segundo valor "))
# nota3 = int(input("ingrese el segundo valor "))
# promedio = int(input("ingresar la cantidad de notas que queres promediar "))

# asignarPromedio = (nota1 + nota2 + nota3) / promedio

# print(f"el promedio de {promedio} notas es de {asignarPromedio}")




# Interpolación de cadenas: Escribir un programa que combine varias variables en una sola
# cadena. 

# nombre = input("ingrese su nombre ")
# apellido = input("ingrese su apellido ")
# edad = int(input("ingrese su edad "))

# asignarCadena = f"Tu nombre es {nombre} y tu apellido es {apellido} y tenes {edad} años "
# print(asignarCadena)



#Cambio de valores: Escribir un programa que intercambie los valores de dos variables y los muestre. 

# nombre = input("Ingrese su nombre para cambiarlo ")
# print("su nombre es ", nombre)

# cambiarNombre = input("ingrese el nuevo nombre ")
# nombre = cambiarNombre
# print("Se ha cambiado de nombre correctamente a ", nombre)



# Área de un rectángulo: Escribir un programa que calcule el área de un rectángulo dados su base y altura.

# base = int(input("ingresar la base "))
# altura = int(input("ingresar la altura "))

# calcularArea = f"el area de un rectangulo es {base * altura}"
# print(calcularArea)



#Circunferencia: Escribir un programa que calcule la circunferencia de un círculo dado su radio. 
# import math

# circunferencia = int(input("escribe la longitud de la circunferencia "))
# radio = int(input("escribe el radio "))

# calcularCircufenrencia = f"la circuferencia es ", circunferencia * radio * math.pi

# print(calcularCircufenrencia)



#Conversión de temperatura: Escribir un programa que convierta una temperatura de Celsius a Fahrenheit

# gradosCelsius = int(input("escriba la temperatura en grados Celsius "))

# convertirGrados = (gradosCelsius * 9 / 5) + 32

# print(f"la converción de grados Celsius {gradosCelsius} a grados Fahrenheit es {convertirGrados}")



#Longitud de una cadena: Escribir un programa que pida al usuario una cadena de texto y muestre su longitud. 

# cadenaDeTexto = input("ingrese una cadena de texto ")

# longitudCadena = len(cadenaDeTexto)
# print("la longitud de la cadena de texto es de ", longitudCadena)



#Conversión de tipos: Escribir un programa que convierta un número entero a flotante y a cadena, y los muestre.

# numeroEntero = int(input("ingrese un numero entero "))

# convertirNumeroFlotante = float(numeroEntero)
# convertirNumeroCadena = str(numeroEntero)

# print("Numero convertido a flotante ",convertirNumeroFlotante)
# print("Numero convertido a Cadena ",convertirNumeroCadena)



#Suma de variables de distintos tipos: Escribir un programa que muestre el resultado de dos sumas con variables de distintos tipos.

# variableEntera = int(input("ingrese un numero entero "))
# variableText = input("ingrese una cadena ")

# sumarVariables = str(variableEntera)+ " " + variableText

# print("la suma de las variables es ", sumarVariables)



#Comparación de números: Escribir un programa que compare dos números y muestre si el primero es mayor, menor o igual al segundo. 

# num1 = int(input("ingrese un numero "))
# num2 = int(input("ingrese otro numero "))

# if num1 > num2:
#     print(f"el numero {num1} es mayor a {num2}")
# elif num1 <= num2:
#     print(f"el numero {num1} es menor e igual que {num2}")


#Verificación de edad: Escribir un programa que verifique si una persona es mayor de edad (18 años o más). 

# edadPersona = int(input("escribe su edad "))

# if edadPersona >= 18:
#     print(f"Usted tiene {edadPersona} años, es mayor de edad")
# else:
#     print(f"Usted tiene {edadPersona} años, no es mayor de edad")


#Número par o impar: Escribir un programa que determine si un número es par o impar. 

# num = int(input("ingrese un numero "))

# if num % 2 == 0:
#     print(f"el numero {num} es par ")
# else:
#     print(f"el numero {num} es impar")


#Suma de dos números: Escribir un programa que pida al usuario dos números y muestre su suma. 

# num1 = int(input("ingrese un numero "))
# num2 = int(input("ingrese otro numero "))

# suma = f"la suma entre {num1} y {num2} es {num1 + num2}" 

# print(suma)



#Multiplicación de números: Escribir un programa que pida al usuario tres números y muestre su producto. 

# num1 = int(input("ingrese el primer numero "))
# num2 = int(input("ingrese el segundo numero "))
# num3 = int(input("ingrese el tercer numero "))

# producto = f"el producto de {num1}, {num2} y {num3} es de {(num1 * num2) * num3}"

# print(producto)



#Concatenación de cadenas: Escribir un programa que pida al usuario dos cadenas de texto y las muestre concatenadas. 

# text1 = input("escriba un texto ")
# text2 = input("escriba otro texto ")

# concatenar = f"{text1} {text2}"

# print(concatenar)


#Pago por horas trabajadas: Escribir un programa que pregunte al usuario por el número de horas trabajadas y el costo por hora, y muestre la paga correspondiente. 

# horasTrabajadas = int(input("ingrese las horas trabajadas "))
# costoPorHora = int(input("ingrese el costo por hora "))

# paga = f"la paga correspondiente es de {horasTrabajadas * costoPorHora}"

# print(paga)





#Mostrar variables en una línea: Escribir un programa que contenga 4 variables de distintos tipos y las muestre en una línea.

# variable1 = input("escriba una variable de cualquier tipo ")
# variable2 = input("escriba la segunda variable de cualquier tipo ")
# variable3 = input("escriba la tercera variable de cualquier tipo ")
# variable4 = input("escriba la cuarta variable de variable de cualquier tipo ")

# mostrar = f"{variable1} {variable2} {variable3} {variable4}"

# print(mostrar)


# Suma de enteros positivos: Escribir un programa que lea un entero positivo y muestre la
# suma de todos los enteros desde 1 hasta n. NO deben utilizar estructuras NO vistas en la
# clase 2. 

# num = int(input("escriba un numero "))


#Mayúsculas y minúsculas: Escribir un programa que pida al usuario una cadena y la muestre en mayúsculas y minúsculas

# texto = input("ingrese un texto para mostrarlo en mayusculas y minusculas ")

# convertirTextoMayusculas = f"Texto en Mayusculas: {texto.upper()}" 
# convertirTextoMinusculas = f"Texto en Minusculas: {texto.swapcase()}" 

# print(convertirTextoMayusculas)
# print(convertirTextoMinusculas)


#Reemplazo de caracteres: Escribir un programa que pida al usuario una cadena y reemplace todas las 'a' por 'e'. 
# texto = input("ingrese un texto ")

# reemplazar = texto.replace('a', 'e')

# print("Texto reemplazado la a por la e ", reemplazar)


#Subcadena: Escribir un programa que pida al usuario una cadena y muestre los primeros 5 caracteres.

texto = input("ingrese un texto ")

mostarCincoCaracteres = texto[0:5]

print("Mostrando los primeros 5 caracteres", mostarCincoCaracteres)
