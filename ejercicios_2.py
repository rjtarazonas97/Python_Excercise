from os import system as consola_limpia
# Para Windows
consola_limpia('cls')

# Nivel 1 – Fácil 🟢

# Contar números
# Imprime los números del 1 al 10 usando for.

""" for i in range(1,11):
    print(i) """

# Tabla de multiplicar
# Pide un número y muestra su tabla de multiplicar del 1 al 10.

""" num = int(input("Introduce un número para ver su tabla de multiplicar: "))

for i in range(1, 13):
    print(f"{num} x {i} = {num * i}") """
    

# Suma de una lista
# Dada una lista de números, calcula su suma usando for.

""" numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
suma = 0
for numero in numeros:
    suma += numero
    print(f"la suma es: {suma}") """


# Contar letras
# Pide una palabra y muestra cuántas letras tiene recorriéndola con for.

""" palabras = input("Introduce una palabra: ")

palabra = 0
for letras in palabras:
    palabra += 1
    
print(f"La palabra {palabras} tiene {palabra} letras") """

# Contar de 2 en 2
# Imprime los números pares del 2 al 20 usando range() con paso 2.

""" for i in range(2, 21, 2):
    print(i)
 """
# Nivel 2 – Intermedio 🟡

# Lista invertida
# Dada una lista, imprime sus elementos en orden inverso usando for.

""" lista = [1,2,3,4,5,6,7,8,9,10]

for i in range (len(lista)-1,-1,-1):
    print(lista[i])
 """
# Números primos hasta N
# Pide un número y muestra todos los números primos menores o iguales a él.

""" num = int(input("Ingresa un numero: "))
primos = []

for i in range (2, num + 1):
    es_primo = True
    for j in range(2, int(i**0.5) + 1):
        if i % j == 0:
            es_primo = False
            break
        if es_primo:
            primos.append(i)
            
print(f"Los números primos menores o iguales a {num} son: {primos}") """


# Filtrar números pares
# Dada una lista de números, guarda en otra lista solo los pares usando for.

""" list_num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = []

for numero in list_num:
    if numero % 2 == 0:
        pares.append(numero)

print(f"Los números pares de la lista son: {pares}") """

# Patrón de asteriscos
# Dibuja el siguiente patrón con for:

# *
# **
# ***
# ****
# *****

""" for i in range(1,6):
    print('*' * i)
 """

# Factorial de un número
# Calcula el factorial de un número usando for.

""" num = int(input("Introduce un número para calcular su factorial: "))
factorial = 1

for i in range(1, num +1):
    factorial *= i
    print(f"El factorial de {i} es: {factorial}")
    
print(f"El factorial de {num} es: {factorial}") """

# Nivel 3 – Difícil 🔴

# Tabla de multiplicar completa
# Imprime las tablas del 1 al 10, cada una con sus resultados.

""" for i in range(1,11):
    print(f"Tabla del {i}:")
    for j in range(1,13):
        print(f"{i} x {j} = {i*j}") """

# Números palíndromos 
# Muestra todos los números palíndromos del 1 al 500.

""" for i in range(1, 501):
    if str(i) == str(i)[::-1]:
        print(i, end=' ') """

# Matriz identidad
# Crea una matriz identidad de tamaño N×N e imprímela usando for.

""" n1 = int(input("Introduce el tamaño de la matriz identidad: "))
matriz = []

for i in range(n1):
    fila = []
    for j in range(n1):
        if i == j:
            fila.append(1)
        else:
            fila.append(0)
    matriz.append(fila)

for fila in matriz:
    print(fila) """

# Fibonacci con for
# Genera los primeros N números de la secuencia de Fibonacci usando for.

""" for n in range(1, 11):
    a, b = 0, 1
    print(f"Fibonacci {n}: {a}")
    for _ in range(1, n):
        a, b = b, a + b
        print(f"Fibonacci {n}: {a}") """

# Triángulo de Pascal
# Imprime los primeros N niveles del triángulo de Pascal usando for.

""" n = int(input("Introduce el número de niveles del triángulo de Pascal: "))
triangulo = []

for i in range(n):
    fila = [1] * (i + 1)
    for j in range(1, i):
        fila[j] = triangulo[i - 1][j - 1] + triangulo[i - 1][j]
    triangulo.append(fila)

for fila in triangulo:
    print(fila)
 """