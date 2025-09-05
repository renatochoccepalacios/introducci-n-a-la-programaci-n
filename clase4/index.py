#pseudocodigo

""" suma = 0
contador = 0

while contador < 5 : # mientras que sea verdadera
    valor = int(input("ingrese valor"))
    suma = suma + valor
    contador = contador + 1
print(suma) """

# estructura que me permite repetir unas o varias


""" secreto = "333"
intentos = 0

while intentos < 3:
    contrasena = input("ingrese la contraseña: ")

    if secreto == contrasena:
        print("podes ingresar")
        break
    else :
        print("contraseña incorrecta vuelva a ingresar")
    intentos = intentos + 1

if intentos == 3 :
    print("su tarjeta quedo bloqueada")
else :
    print("bienvenido") """




""" numero = int(input("ingrese un numero: "))
suma = 0
while numero != 0:"""




""" while True :
    num = int(input("ingrese numero: "))
    if (num != 0 ):
        print(f"numero {num}")
    else :
        break
print("fin del programa") """



""" while True :
    num = int(input("ingrese numero: "))
    print(f"numero {num}")
    if (num == 0 ):
        break
print("fin del programa") """


""" suma = 0
contador = 0
while True :
    
    num = int(input("ingrese numero: "))
    

    if (num != 0 ):
        print(f"numero {num}")
        suma = suma + num
        contador = contador + 1
    else:
        break

print(f"la cantidad de numeros es {contador}")
print(f"la suma total de numeros es {suma}")
print("fin del programa") """


# while true --> seria un while infinito
# continue --> volver a empezar
""" while True:
    numero = int(input("Ingrese numero: "))

    if(numero < 0) :
        continue
    print(f"Numero: {numero}")

print("fin del programa") """

""" while True :
    numero = input("Ingrese numero: ")
    if(numero == "A") :
        break
    if int(numero) < 0:
        continue

    print(f"numero: {int(numero)}")
    print(f"Fin del programa") """




while True :
    opcion = int(input('''-----Menu-----
    1. suma
    2. resta
    3. multiplicacion,
    4. division,
    5. salir
    
    Ingrese su opción: '''))

    if(opcion == 5) :
        print("fin del programa")
        break

    numero1 = int(input("ingrese un numero: "))
    numero2 = int(input("ingrese otro numero: "))
    if(opcion == 1) :
        suma = numero1 + numero2
        print(f"la suma de {numero1} mas {numero2} + {suma}")

    if(opcion == 2) :
        resta = numero1 - numero2
        print(f"la suma de {numero1} mas {numero2} - {resta}")

    if(opcion == 3) :
        multiplicacion = numero1 * numero2
        print(f"la suma de {numero1} mas {numero2} x {multiplicacion}")

    if(opcion == 4) :
        division = numero1 / numero2
        print(f"la suma de {numero1} mas {numero2} / {division}")



