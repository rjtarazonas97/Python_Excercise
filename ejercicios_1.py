from os import system as consola_limpia

# Para Windows
consola_limpia('cls')
# Para Linux / Mac
# consola_limpia('clear')

# Nivel Fácil 🟢
# Número positivo o negativo
# Pide un número y muestra si es positivo, negativo o cero.

""" num = float(input("Introduce un número: "))

if num > 0:
    print("El número es positivo.")
elif num < 0:
    print("El número es negativo.")
else:
    print("El número es cero.") """


# Mayor de edad
# Pide la edad y muestra si la persona es mayor o menor de edad.

""" edad = int(input("Introduce tu edad: "))

if edad >=18:
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.") """

# Par o impar
# Pide un número y muestra si es par o impar.

""" num = int(input("Introduce un número: "))
if num % 2 ==0:
    print("El numero es par.")
else:
    print("El numero es impar") """

# Nota aprobada o reprobada
# Pide una nota (0–10) y muestra si aprobaste (≥6) o no.

""" nota = float(input("Introduce tu nota: "))

if nota < 0 or nota > 10:
    print("Nota inválida. Debe estar entre 0 y 10.")
elif nota >= 6:
    print("¡Aprobaste!")
else:
    print("No aprobaste.") """
# Día de la semana
# Pide un número del 1 al 7 y muestra el día correspondiente o “Número inválido”.

""" dia = int(input("Introduce un numero del 1 al 7:"))

if dia < 1 or dia > 7:
    print("Numero invalido.")
elif dia == 1:
    print("Lunes")
elif dia == 2:
    print("Martes")
elif dia == 3:
    print("Miercoles")
elif dia == 4:
    print("Jueves")
elif dia == 5:
    print("Viernes")
elif dia == 6:
    print("Sabado")
else:
    print("Domingo") """

# Nivel Intermedio 🟡
# Clasificación de temperatura
# Pide la temperatura y clasifícala como “frío” (<10), “templado” (10–25) o “calor” (>25).

""" temperatura = float(input("Introduce la temperatura: "))

if temperatura < 10:
    print("Frio")
elif temperatura >= 10 and temperatura <=25:
    print("Templado")
else:
    print("Calor")
 """

# Conversión de calificación numérica a letra
# Pide una nota (0–100) y conviértela a A, B, C, D o F según el rango.

""" nota = float(input("Introduce tu nota: "))

if nota < 0 or nota >100:
    print("Nota inválida. Debe estar entre 0 y 100.")
elif nota >=90:
    print("A")
elif nota >=80:
    print("B")
elif nota >=70:
    print("C")
elif nota >=60:
    print("D")
else:
    print("F") """

# Calculadora simple
# Pide dos números y una operación (+, -, *, /) y muestra el resultado.

""" num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))

digito = input("Introduce la operacion (+, -, *, /):")

if digito == "+":
    print(f"El resultado de {num1} + {num2} es: {num1 + num2}")
elif digito == "-":
    print(f"El resultado de {num1} - {num2} es: {num1 - num2}")
elif digito == "*":
    print(f"El resultado de {num1} * {num2} es: {num1 * num2}")
else:
    if num2 == 0:
        print("Error: División por cero no permitida.")
    else:
        print(f"El resultado de {num1} / {num2} es: {num1 / num2}") """

# Verificación de contraseña
# Compara la contraseña ingresada con una guardada y muestra si es correcta o incorrecta.

""" GUARDADA = "1234"
ingresada = input("Introduce la contraseña: ")

if ingresada == GUARDADA:
    print("LA CONTRASEÑA ES CORRECTA")
else:
    print("LA CONTRASEÑA ES INCORRECTA") """


# Mes con estación del año
# Pide el número de mes y muestra la estación (primavera, verano, otoño, invierno).

""" input_mes = int(input("Introduce el número del mes (1-12): "))

if input_mes < 1 or input_mes > 12:
    print("Número de mes inválido. Debe estar entre 1 y 12.")
elif input_mes in [12,1,2,3]:
    print("Verano")
elif input_mes in [4,5,6]:
    print("Otoño")
elif input_mes in [7,8,9]:
    print("Invierno")
else:
    print("Primavera") """



# Nivel Avanzado 🔴
# Sistema de descuentos
# Pide el precio y la categoría de cliente (normal, socio, VIP) y aplica distintos porcentajes de descuento.

# Clasificador de triángulos
# Pide tres lados y determina si el triángulo es equilátero, isósceles o escaleno.

# Simulador de cajero automático
# Pide el tipo de operación (retirar, depositar, consultar saldo) y actúa según el caso.

# Calculadora de IMC con interpretación
# Pide peso y altura, calcula el IMC y muestra si es bajo peso, normal, sobrepeso u obesidad.

# Sistema de calificación con observaciones
# Pide una nota (0–100) y muestra tanto la letra (A, B, C…) como un comentario (“Excelente”, “Bueno”, “Regular”, “Deficiente”).

