# CLASE 5 FOR

palabra = "unpaz"

"""for x in palabra :
    print(x)"""
    


"""lista = [17, 4, -1 , 8 ]"""

"""for x in range(len(lista)) :
    print(x)"""
    
"""for x in range(len(lista)) :
    print(x)
    #print(lista[x])"""
    

"""for x in palabra:
    print(palabra)"""


""" for x in palabra :
    print(x, end = "") """

# range(inicio, final, saltos)
    
    

"""valores1 = range(10) # hasta 10
valores2= range(1, 11) # de 1 a 11
valores3 = range(1, 11, 2) # de 1 a 11 con saltos de 2


print(valores1)
print(valores2)
print(valores3)"""



""" for i in range(0,5,2) :
    print(i, end = "; ") """
    
"""for i in range(1,10,3) :
    print(i)"""
 
 
 
 
 
 
""" valores1 = range(10) # hasta 10
valores2= range(1, 11) # de 1 a 11
valores3 = range(1, 11, 2) # de 1 a 11 con saltos de 2


print(list(valores1))
print(list(valores2))
print(list(valores3)) """
 
 
 
# variable = [45, "texto abc ##? 123", 45.25]


""" for i in variable :
    print(variable) """

""" for i in range(len(variable)) :
    print(f"Indice: {i} || Contenido: {variable[i]}") """

# print(len(variable))



secuencia = ["pop", "rock", "jazz"]

""" for i in range(len(secuencia)):
    print(f"En el indice: {i} || Accedemos a: {secuencia[i]}") """

# con un contador

cont = 0
for i in secuencia :
    print(f"En el indice {cont} accedemos al elemento {i}")
    cont = cont + 1


# aca tenemos indice y contenido con enumerate
""" for indice, elemento in enumerate(secuencia) :
    print(f"En el indice {indice} accedemos al elemento {elemento}") """




""" for i in range(4):
    print(i)

    if i == 2 :
        break
else :
    print("Secuencia finalizada")
    print("Ultimo elemento: ", i) """


""" numero1 = int(input("ingrese el primer numero: "))
numero2 = int(input("ingrese el segundo numero: "))

suma = numero1 + numero2
print(f"la suma es {suma}")

producto = numero1 * numero2
print(f"el producto es {producto}")
 """


""" edad = int(input("ingrese su edad: "))

if edad < 18 :
    print("eres menor de edad")
elif edad > 18 and edad < 65 :
    print("eres adulto")
else :
    print("eres adulto mayor") """


""" edad = int(input("ingrese su edad: "))

if edad < 18 :
    print("usted es menor de edad")
elif edad < 65 :
    print("usted adulto")
else :
    print("usted adulto mayor") """



""" maximo = 0
while True :
    numeroPositivo = int(input("ingrese un numero "))

    if numeroPositivo < 0:
        break
    elif numeroPositivo > maximo:
        maximo = numeroPositivo
    print(f"el numero maximo es {maximo}") """


""" nombres = []



for indice in range(5) :
    nombre = input("ingrese un nombre: ")

    nombres.append(nombre)

for indice, contenido in enumerate(nombres) :
    print(f"Indice: {indice} || Nombre: {contenido}") """