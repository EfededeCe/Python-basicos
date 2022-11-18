"""Unidad 1""" # unidad 2 linea 192
# 1) Escribe un programa muestre por pantalla “Hello World”.

# print("Hello World")

# 2) Escribe un programa que escriba en la pantalla el resultado de sumar 3 + 5.

# print(3 + 5)

# 3) Escribe un programa que pida el nombre del usuario y escriba un texto
#    que diga “Hola nombreUsuario”

# nombre_usuario = input("Ingrese su nombre: ")
# print("Hola", nombre_usuario)

# 4) Escribe un programa que pida un número, pida otro número y escriba
#    el resultado de sumar estos dos números.

# num1 = int(input("Ingrese num1=> "))
# num2 = int(input("Ingrese num2=> "))

# print(num1 + num2)

#5) Escribe un programa que pida dos números y escriba en la pantalla cual es el mayor.

# n1 = int(input("Ingrese num1=> "))
# n2 = int(input("Ingrese num2=> "))
# if n1>=n2:
#     print("El mayor es", n1)
# else:
#     print("El mayor es", n2)

#6) Escribe un programa que pida 3 números y escriba en la pantalla el mayor de los tres.

# n3 = int(input("Ingrese num1=> "))
# n4 = int(input("Ingrese num2=> "))
# n5 = int(input("Ingrese num3=> "))
# if n3>=n4 and n3>=n5:
#     print("El mayor es", n3)
# elif n4>=n3 and n4>=n5:
#     print("El mayor es", n4)
# else:
#     print("El mayor es", n5)

# 7) Escribe un programa que pida un número y diga si es divisible por 2

# n6 =int(input("Dame un nro=> "))
# if n6%2 == 0:
#     print("Es divisible por 2")
# else:
#     print("No es divisible por 2")

# 8) Escribe un programa que pida un número y nos diga si es
#    divisible por 2, 3, 5 o 7 (sólo hay que comprobar si lo es por uno de los cuatro)

# n7 =int(input("Dame un nro=> "))
# if n7%2 == 0 or n7%3 == 0 or n7%5 == 0 or n7%7 == 0:
#     print("Es divisible por alguno")
# else:
#     print("No es divisible por ninguno")



# 9) Añadir al ejercicio anterior que nos diga por cuál de los cuatro es divisible (hay
#    que decir todos por los que es divisible)

# n8 =int(input("Dame un nro=> "))
# if n8%2 == 0 or n8%3 == 0 or n8%5 == 0 or n8%7 == 0:
#     if n8%2 == 0:
#         print("Es divisible por 2")
#     if n8%3 == 0:
#         print("Es divisible por 3")
#     if n8%5 == 0:
#         print("Es divisible por 5")
#     if n8%7 == 0:
#         print("Es divisible por 7")
# else:
#     print("No es divisible por ninguno")

# 10) Escribir un programa que escriba en pantalla los divisores de un número dado

# n9 = int(input("Mete un nro=> "))

# for i in range(1,n9):
#     if n9%i == 0:
#         print(n9, "es divisible por", i)

# 11) Escribir un programa que nos diga si un número dado es primo (no es divisible
#     por ninguno otro número que no sea él mismo o la unidad)

# n10 =int(input("Nro=> "))
# cont = 0

# for i in range(1, n10+1):
#     if i != 0 and n10 != 2 and n10/i == n10 or n10/i == 1:
#         cont+=1
# if cont == 2:
#     print("El nro es primo")
# else:
#     print("El nro NO es primo")



# 12) Pide una nota (número). Muestra la calificación según la nota:
#      0-3: Muy deficiente
#      3-5: Insuficiente
#      5-6: Suficiente
#      6-7: Bien
#      7-9: Notable
#      9-10: Sobresaliente

# n11 = int(input("nro=> "))
# if n11<=10 and n11>0:
#     if n11<=3:
#         print("Muy deficiente")
#     elif n11>3 and n11<5:
#         print("Insuficiente")
#     elif n11>=5 and n11<7:
#         print("Suficiente")
#     elif n11>=7 and n11<9:
#         print("Notable")
#     else:
#         print("Sobresaliente")
# else:
#     print("El numero no es válido")




# 13) Realiza un programa que escriba una pirámide del 1 al 30 de la siguiente
#     forma:
#     1
#     22
#     333
#     4444
#     55555
#     666666
#     ........

# for i in range(1, 31):
#     for b in range(i):
#         print(i, end="")
#     print(end="\n")


# 14) Haz un programa que escriba una pirámide inversa de los números del 1 al
#     número que indique el usuario de la siguiente forma
#     (suponiendo que indica 6):
#     666666
#     55555
#     4444
#     333
#     22
#     1

# for i in range(31, 0, -1):
#     for b in range(i):
#         print(i, end="")
#     print(end="\n")


# 15) Crear un programa que escriba los números del 1 al 500,
# y que indique cuales son múltiplos de 4 y de 9 y que cada 5
# líneas muestre una línea horizontal.
# Por ejemplo:
# 1
# 2
# 3
# 4 (Múltiplo de 4)
# 5
# ------------------------------------------------------------
# 6
# 7
# 8 (Múltiplo de 4)
# 9 (Múltiplo de 9)
# 10

# for i in range(1, 501):
#     if i%4 == 0 and i%9 == 0:
#         print(i,"Múltiplo de 4 y de 9")
#     elif i%4 == 0:
#         print(i, "Múltiplo de 4")
#     elif i%9 == 0:
#         print(i, "Múltiplo de 9")
#     else:
#         print(i)
#     if i%5 == 0:
#         for i in range(80):
#             print("-", end="")
#         print("-")



"""Unidad 2"""
print("Hola")


# 1) Desarrollar una función que reciba tres números positivos y devuelva el mayor
# de los tres, sólo si éste es único (mayor estricto). En caso de no existir el mayor
# estricto devolver -1. No utilizar operadores lógicos (and, or, not). Desarrollar
# también un programa para ingresar los tres valores, invocar a la función y
# mostrar el máximo hallado, o un mensaje informativo si éste no existe.

def mayor(a=345, b=12, c=345):
    may = [a, b, c]
    may.sort()
    if may[1] == may[2]:
        may = -1
    else:
        may = may[2]
    return may

print(mayor())


# 2) Desarrollar una función que reciba tres números enteros positivos y verifique si
# corresponden a una fecha válida (día, mes, año). Devolver True o False según
# la fecha sea correcta o no. Realizar también un programa para verificar el
# comportamiento de la función.

def fecha(dd=33,mm=15,aa=154234):
    fech = ["","",""]
    if dd > 0 and dd < 32:
        fech[0] = dd
    if mm > 0 and mm < 13:
        fech[1] = mm
    if len(str(aa)) == 4:
        fech[2] = aa
    if fech[0] and fech[1] and fech[2]:
        fech = True
    else:
        fech = False
    return fech

print(fecha())

# 3) Un comercio de electrodomésticos necesita para su línea de cajas un programa
# que le indique al cajero el cambio que debe entregarle al cliente. Para eso se
# ingresan dos números enteros, correspondientes al total de la compra y al
# dinero recibido. Informar cuántos billetes de cada denominación deben ser
# entregados al cliente como vuelto, de tal forma que se minimice la cantidad de
# billetes. Considerar que existen billetes de $500, $100, $50, $20, $10, $5 y $1.
# Emitir un mensaje de error si el dinero recibido fuera insuficiente. Ejemplo: si la
# compra es de $317 y se abona con $500, el vuelto debe contener 1 billete de
# $100, 1 billete de $50, 1 billete de $20, 1 billete de $10 y 3 billetes de $1.

def vuelto(precio=1784,entrega=2000):
    diferencia = entrega - precio
    billetes = {
        500: 0,
        100: 0,
        50: 0,
        20: 0,
        10: 0,
        5: 0,
        1: 0
    }
    if diferencia > 0:
        while diferencia >= 100:
            billetes[100] += 1
            diferencia -= 100
        while diferencia >= 50:
            billetes[50] += 1
            diferencia -= 50
        while diferencia >= 20:
            billetes[20] += 1
            diferencia -= 20
        while diferencia >= 10:
            billetes[10] += 1
            diferencia -= 10
        while diferencia >= 5:
            billetes[5] += 1
            diferencia -= 5
        while diferencia >= 1:
            billetes[1] += 1
            diferencia -= 1
    else:
        billetes = "Monto abonado insuficiente"
    return billetes

print(vuelto())

# 4) Escribir dos funciones separadas para imprimir por pantalla los siguientes
# patrones de asteriscos, donde la cantidad de filas se recibe como parámetro:


def ast_cuad(filas):
    for i in range(filas):
        # print('* ' * (filas*2))
        print('* ' * filas)
    
ast_cuad(3)

def ast_triangulo(filas):
    for i in range(filas):
        for a in range(i+1):
            # print("*"*2, end="")
            print("* ", end="")
        print("")

ast_triangulo(5)

# 5) Crear una función lambda que devuelva el cuadrado de un valor recibido cómo
# parámetro. Desarrollar además un programa para verificar el comportamiento
# de la función.

al_cuadrado = lambda x: x ** 2
print(al_cuadrado(4))


# 6) Crear una función lambda para comprobar si un número es par o impar.
# Desarrollar además un programa para verificar el comportamiento de la
# función.

es_par = lambda x: x % 2 == 0

print(es_par(4))


# 7) Crear una lista con los cuadrados de los números entre 1 y N (ambos
# incluidos), donde N se ingresa desde el teclado. Luego se solicita imprimir los
# últimos 10 valores de la lista.

def cuads(n):
    cuadrados = []
    for i in range(1,n+1):
        cuad = i ** 2
        cuadrados.append(cuad)
    print(cuadrados[-10:])

cuads(40)


# 8) Eliminar de una lista de palabras aquellas que se encuentren también en una segunda lista.
# Imprimir la lista original, la lista de palabras a eliminar y la lista resultante.

lista1 = ["olla", "collar","clip", "autos", "Torneo", "Uololóh", "chango", "maceta"]
lista2 = ["Troya", "collar","clip", "Bicicleta", "Torno", "Murciélago", "chango", "tundra"]

def palabras(list1, list2):
    lista_elim = []
    list_origin = list(list1)
    for i in list_origin:
        if i in list2:
            lista_elim.append(i)
            list1.remove(i)
    return f'Lista original: {list_origin}\nLista eliminados: {lista_elim}\nLista resultante: {list1}'

print(palabras(lista1,lista2))

# 9) Escribir una función que reciba una lista como parámetro y devuelva True si la
# lista está ordenada en forma ascendente o False en caso contrario. Por
# ejemplo, ordenada([1, 2, 3]) retorna True y ordenada(['b', 'a']) retorna False.
# Desarrollar además un programa para verificar el comportamiento de la
# función.

li_desorden = [2, 3, 1, 5]
li_orden = [1, 2, 3, 5, 8, 123]

def ordenada(ord):
    ordena = sorted(ord)
    # ordena.sort()
    print(ordena)
    if ord == ordena:
        orden = True
    else:
        orden = False
    return orden

ordenada(li_desorden)

# 10) Desarrollar una función que determine si una cadena de caracteres es capicúa,
# sin utilizar cadenas auxiliares ni rebanadas. Escribir además un programa que
# permita verificar su funcionamiento.

capicua = "Neuquen"
no_capicua = "Córdoba"

def es_capicua(c):
    capi = ""
    for i in range(len(c)-1,-1,-1):
        capi+= c[i]
    return c.lower() == capi.lower()

print(es_capicua(no_capicua))



# 11) Leer una cadena de caracteres e imprimirla centrada en pantalla. Suponer que
# la misma tiene 80 columnas.



# 12) Escribir una función que reciba como parámetro una tupla conteniendo una
# fecha (día,mes,año) y devuelva una cadena de caracteres con la misma fecha
# expresada en formato extendido. Por ejemplo, para (12, 10,17) devuelve “12 de
# Octubre de 2017”. Escribir también un programa para verificar su
# comportamiento.



# 13) Ingresar una frase desde el teclado y usar un conjunto para eliminar las
# palabras repetidas, dejando un solo ejemplar de cada una. Finalmente mostrar
# las palabras ordenadas según su longitud.



# 14) Desarrollar una función eliminar_claves() que reciba como parámetros un
# diccionario y una lista de claves. La función debe eliminar del diccionario todas
# las claves contenidas en la lista, devolviendo el diccionario modificado y un
# valor de verdad que indique si la operación fue exitosa. Desarrollar también un
# programa para verificar su comportamiento.



# 15) Escribir una función para eliminar una subcadena de una cadena de
# caracteres, a partir de una posición y cantidad de caracteres dados,
# devolviendo la cadena resultante. Escribir también un programa para verificar
# el comportamiento de la misma. Escribir una función utilizando rebanadas
