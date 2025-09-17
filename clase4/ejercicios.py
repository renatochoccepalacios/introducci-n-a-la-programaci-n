# 1. Escribir un programa que muestre los números del 0 al 50, pero de 5 en 5
""" contador = 0

while contador <= 50 :
    print(contador)
    contador += 5 """

#Escribir un programa que muestre los números del 2000 al 0, pero de 250 en 250 

""" contador = 0

while contador <= 2000:
    print(contador)
    contador = contador + 250 """



# Escribir un programa que pida al usuario una palabra, debe mostrarla 10 veces, junto al
# número correspondiente.
# Ejemplo:
# 1 hola
# 2 hola

""" elegirPalabra = input("Escriba una palabra para mostrala 10 veces")
contador = 0

while contador < 10:
    contador = contador + 1

    print(f"{contador} {elegirPalabra}") """


# 4. Escribir un programa que pregunte al usuario cuantos años cumplio o cumplira este año
# a. Debe calcular el año de nacimiento, teniendo en cuenta el año actual.
# b. Debe mostrar por pantalla el año de nacimiento y los años que ha cumplido cada año
# hasta la edad actual.
# Ejemplo: 5
#  2017 0 años
#  2018 1 años
#  2019 2 años
#  2020 3 años
#  2021 4 años
#  2022 5 años


""" preguntarEdad = int(input("cuantos años cumpliste o cumpliras este año? ")) # 20
calcularEdad = 2025 - preguntarEdad # eje: 2025 - 20 = 2005 seria
contador = calcularEdad # ahora contador va hacer igual a 2005
numero = 0 #inicializamos en 0

while contador <= 2025 : # y ahora mientras 2005 sea menor o igual a 2025 se va a ejecutar el codigo
    print(f"{contador} {numero} años")
    contador = contador + 1
    numero = numero + 1 
 """
    

# Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la
# cuenta atrás desde ese número hasta cero separados por comas. (Investigue cómo mostrar
# datos con print en la misma línea de texto), Si se anima trate de no imprimir la última coma
# después del 0.
# Ejemplo: 5

# Está bien
# 5,4,3,2,1,0,
# Está mejor...
# 5,4,3,2,1,0

""" pedirNumero = int(input("escriba un numero entero positivo"))

while pedirNumero >= 0:
    if pedirNumero == 0 :
        print(pedirNumero)
    else :
        print(pedirNumero, end=", ")

    pedirNumero = pedirNumero - 1 """




# 6. (Utilice while, if, continue y break) Escribir un programa que muestre números del 0 al 30
# uno debajo de otro.
# ● Cuando los números sean 3, 8, 17, 26 debe mostrar el mensaje “saltando instrucciones
# con (xxxxxxxxxxxxx el nombre de la instrucción que permite realizar saltos en un bucle)
# llegue al número 3 o 8 o 17 o 26”
# ● Cuando los números sean mayores a 25 debe preguntar si continúa o sale del conteo
# (por ejemplo, presione Presione: 'S' para salir, cualquier otra tecla para continuar)
# ○ Si presiona cualquier tecla el programa seguirá su curso
# ○ Si presiona S, terminará el programa, antes de terminar debe mostrar a qué
# número de conteo llegó. 

""" contador = 0

while contador <= 30:


        if (contador == 3 or contador == 8 or contador == 17 or contador == 26) :

            print('''saltando instrucciones
                con (xxxxxxxxxxxxx el nombre de la instrucción que permite realizar saltos en un bucle)
                llegue al número 3 o 8 o 17 o 26''')
            contador = contador + 1
            continue

        if contador > 25 : 
            preguntarSiContinuar = input("Continuas o sales del conteo? Presiona S para salir si es otra tecla es continuar")
            
            if preguntarSiContinuar == "S" or preguntarSiContinuar == "s" :
                print(f"llego hasta el numero {contador} del conteo")
                break
            else :
                print(contador)
                contador = contador + 1
                continue
            
        print(contador)
        contador = contador + 1 """



# 7. Escribir un programa que muestre la sucesión de Fibonacci.
# En matemáticas, la sucesión de fibonacci es una sucesión infinita de números naturales,
# donde el siguiente número es calculado sumando los dos números anteriores.
# Empiece a partir del 1 y termine cuando sea mayor a 200 
    
""" a = 1
b = 1

while a <= 200 :
    print(a) # 1

    siguiente = a + b # 1+1 = 2
    a = b # 1 va a ser igual a b osea 1
    b = siguiente # b va a ser igual a 2 """
# 1
# 1
# 2





# 8. Escribir un programa que muestre un menú con las siguientes opciones:
# a. Suma.
# b. Multiplicación
# c. Largo de Palabras
# d. Salir
#  Funcionamiento:
# ● El usuario debe ver el menú de opciones todo el tiempo.
# ● Si elige la opción a
# debe solicitar 2 números, sumarlos y mostrarlos.
# Si elige la opción b
# debe solicitar 2 números, multiplicarlos y mostrarlos.
# ● Si elige la opción c,
# Debe solicitar dos palabras y mostrar la palabra más larga, avisar cuando
# sean iguales.en ambos casos debe mostrar el largo de cada una
# ● Si elige la opción d
# Debe salir y despedir al usuario. 

""" while True :
    elegirOpciones = input(''' elija una de estas opciones: 
                            a. Suma.
                            b. Multiplicación
                            c. Largo de Palabras
                            d. Salir ''')
    if elegirOpciones == "a":
        numero1 = int(input("ingrese el primer numero: "))
        numero2 = int(input("ingrese el segundo numero: "))
    
        suma = numero1 + numero2
        print(f"la suma de {numero1} mas {numero2} es {suma}")

    if elegirOpciones == "b":
        numero1 = int(input("ingrese el primer numero: "))
        numero2 = int(input("ingrese el segundo numero: "))
    
        multiplicacion = numero1 + numero2
        print(f"la multiplicacion de {numero1} y {numero2} es de {multiplicacion}")

    if elegirOpciones == "c":
        ingresarPalabraUno = input("Ingrese la primera palabra: ")
        ingresarPalabraDos = input("Ingrese la segunda palabra: ")

        if(len(ingresarPalabraUno) > len(ingresarPalabraDos)) :
            print(f"la palabra mas larga es {ingresarPalabraUno} por que tiene {len(ingresarPalabraUno)} caracteres")
        elif ingresarPalabraUno == ingresarPalabraDos :
            print(f'''Ambas palabras son iguales y tienen el mismo largo 
                  {ingresarPalabraUno} = {len(ingresarPalabraUno)}
                  {ingresarPalabraDos} = {len(ingresarPalabraDos)}
            
                ''')
        else :
            print(f"la palabra mas larga es {ingresarPalabraDos} por que tiene {len(ingresarPalabraDos)} caracteres")

        
    if elegirOpciones == "d":
        print("Saliste del programa")
        break """






# Escribir un programa que solicite una frase al usuario y luego una letra, usando while y lo
# aprendido sobre string en las clases anteriores, acceso a cada caracter de una cadena por
# medio del elemento palabra[0], (no use IN).
# Buscar si la letra que ingresó se encuentra en la frase solicitada.
# Cuente cuántas veces está esa letra dentro de la frase
# Si, esta mostrará un mensaje que diga “letra ... encontrada aparece ... veces.
# Si no está mostrara “Letra ... no encontrada en la frase”
# Luego de resolver debe preguntar al usuario si quiere salir debe ingresar una letra “S” o si
# presiona cualquier otra letra continuará. 


while True :
    frase = input("Ingrese una frase: ")
    letra = input("Ingrese una letra: ")

    indice = 0
    contador = 0

    while indice < len(frase):
        if(frase[indice] == letra) :
            contador = contador + 1
        indice = indice + 1

    if( contador > 0) :
        print(f'la letra "{letra}" encontrada de la frase "{frase}" aparece {contador} veces')
    else :
        print(f"la letra {letra} no se encontro")

    salir = input("ingrese la 'S' para salir o cualquier letra para continuar: ")

    if(salir == "S" or salir == "s") :
        print("Saliste del programa")
        break


