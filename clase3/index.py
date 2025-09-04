# texto = "unpaz"

# print(texto[-1],texto[-2],texto[-3], texto[-4], texto[-5])


# texto = "unpaz"

# print(texto[2:5])


# uni = "UNPAZ, Universidad Nacional de José C. Paz"

# print(uni[7::2])

# comillas
# print("hola como \"estas\" ")
# print("hola como \'estas\' ")

# #salto de linea
# print("hola como \nestas\n ")

# # tabular
# print("hola como \testas\t ")


# Primera letra en mayuscula

# nombre = "renato"
# print(nombre.capitalize())

# # Todo mayuscula

# nombre2 = "agustina"

# print(nombre2.upper())


# # todo minuscula

# nombre3 = "THIAGO"

# print(nombre3.lower())


# limpiar espacios en blanco

# frase = "hola   a"

# print(frase.strip())


# operadores logicos

# x = True
# y = False


# print(f"{x} and {y} es", x and y)
# print(f"{x} or {y} es", x or y)
# print("not x es", not x)


# in


# if

# a = 10
# b = 15

# if a > b:
#     c = a - b
#     print(c)
# else:
#     c = a + b
#     print(c)


#

# valor = int(input("ingresar un numero: "))

# if valor > 10 :
#     print(f"el valor {valor} ingresado es mayor que 10 ")
# else :
#     if valor == 10 :
#         print(f"el valor {valor} ingresado es igual que 10 ")
#     else:
#         print(f"el valor {valor} es menor a 10")
# print("fin del programa")


# edad = int(input("ingrese su edad: "))
# cantidadDeEntradas = int(input("Ingrese la cantidad de entradas: "))

# if edad <= 12 or edad >= 80:
#     print("usted entra gratis ")
# else:
#     if edad >= 13 and edad < 18:
#         print(f"debe pagar {12000 * cantidadDeEntradas}")
#     else:
#         if edad >= 18 and edad < 60:
#             print(f"debe pagar {18000 * cantidadDeEntradas}")
#         else:
#             if edad >= 60 and edad < 80:
#                 print(f"debe pagar {20000 * cantidadDeEntradas}")

# con elif

# if edad <= 12 or edad >= 80:
#     print("usted entra gratis ")
# elif edad >= 13 and edad < 18:
#     print(f"debe pagar {12000 * cantidadDeEntradas}")
# elif edad >= 18 and edad < 60:
#     print(f"debe pagar {18000 * cantidadDeEntradas}")
# else:
#     if edad >= 60 and edad < 80:
#         print(f"debe pagar {20000 * cantidadDeEntradas}")


# valor = "Universidad Nacional de José C. Paz"
# palabra = input("ingrese una palabra: ")

# if palabra.upper() in valor.upper():
#     print("Si esta")
# else :
#     print("No esta")


valor1 = int(input("ingrese el primer valor distinto de 0: "))
valor2 = int(input("ingrese el segundo valor distinto de 0: "))

if valor1 != 0 and valor2 != 0:
    print(f"la division de {valor1} y {valor2} es {valor1 / valor2}")
else:
    print("Se debe ingresar un numero distinto de 0 !")