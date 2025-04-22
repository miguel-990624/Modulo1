"""
1. Nombre y Edad
"""
nombre =input("Hola, ingresa tu nombre: ")
edad= input("Ahora quiero conocer tu edad: ")
print(f"hola {nombre}, tienes {edad} años")

"""
2. Suma de dos numeros enteros
"""
num1=int(input("ingresa un numero que quieras sumar: "))
num2=int(input("ingresa el segundo numero de tu operacion: "))
print(num1 + num2)

"""
3. Multiplicacion de decimales
"""
print("multipliquemos dos numeros decimales")
num1=float(input("ingresa el primer numero: "))
num2=float(input("ingresa el segundo numero: "))
print(num1*num2)

"""
4.Doble y triple
"""
num1=int(input("ingresa el valor de un numero que quieras conocer su doble y triple: "))
print(f"El doble del numero {num1} es: {num1 * 2}, y su triple es {num1 * 3}")

"""
5.Repetir palabra
"""
val=input("escribe una palabra que quieras ver como se repite: ")
num1 = int(input("ahora cuantas veces quieres que se repita: "))
for x in range(num1):
    print(val)

"""
6.Division
"""
num1=int(input("ingresa el valor del numerador: "))
num2=int(input("ingresa el valor del denominador: "))
total = num1/num2
print(f"El valor total de tu division es: {total:.2f}")

"""
7.
"""
nombre=input("ingresa tu nombre, para descomponerlo en letras: ")
for x in nombre:
    print(x)

"""
8. Division entera y modulo
"""
num1=int(input("ingresa el valor del numerador: "))
num2=int(input("ingresa el valor del denominador: "))
print(f"El valor total de tu division es: {num1//num2}, con un residuo de {num1%num2}")

"""
9.Todas la operaciones
"""
num1=int(input("ingresa el valor de la primera cifra para realizar todos los procesos matematicos con ella, este sera el numerador: "))
num2=int(input("ingresa el valor de la segunda cifra para realizar todos los procesos matematicos con ella, este sera el denominador: "))
print(f"El valor de la suma es de {num1+num2}, el de la resta es de {num1-num2}, multiplicacion es {num1*num2}, division es {num1/num2}")

"""
10. Potencias con f-strings
"""
num1=int(input("Escribe el numero del que quieres conocer la potencia: "))
print(f"la potencia 2 de {num1} es: {num1**2}, y su potencia 3 es: {num1**3}")

"""
11. Parte entera de un decimal
"""
num1=float(input("ingresa un numero decimal: "))
print(f"el numero sin decimales es {num1:.0f}")

"""
12. Mayor de edad (sin condicional)
"""
num1=int(input("ingresa tu edad: "))
print("Eres mayor de edad?")
print(num1 >= 18)

"""
13. ¿Son iguales?
"""
num1=int(input("ingresa un numero: "))
num2=int(input("ingresa un segundo numero: "))
if(num1 == num2):
    print("son iguales")
else:
    print("no son iguales")

"""
14. ¿Mayor que?
"""
num1 = int(input("ingresa un numero: "))
num2 = int(input("ingresa un segudno numero: "))
if (num1 > num2):
    print(f"{num1} es mayor que {num2}")
else:
    print(f"{num1} no es mayor que {num2}")

"""
15. ¿Menor o igual?
"""
num1 = int(input("ingresa un numero: "))
num2 = int(input("ingresa un segudno numero: "))
if (num1 <= num2):
    print(f"{num1} es menor o igual que {num2}")
else:
    print(f"{num1} no es menor o igual que {num2}")

"""
16. Ambos mayores que 10
"""
num1 = int(input("ingresa un numero: "))
num2 = int(input("ingresa un segudno numero: "))
if (num1 < 10 and num2 < 10):
    print("son mayores de 10")
else:
    print("no son mayores de 10")

"""
17. Al menos uno mayor que 10
"""
num1 = int(input("ingresa un numero: "))
num2 = int(input("ingresa un segudno numero: "))
if (num1 < 10 or num2 < 10):
    print("al menos 1 es mayor de 10")
else:
    print("no son mayores de 10")

"""
18. No son iguales
"""
num1 = int(input("ingresa un numero: "))
num2 = int(input("ingresa un segudno numero: "))
if (not num1 == num2):
    print(f"{num1} no es igual que {num2}")
else:
    print(f"{num1} es igual que {num2}")

"""
19. Promedio
"""
num1 = int(input("ingresa un numero: "))
num2 = int(input("ingresa un segudno numero: "))
num3 = int(input("ingresa un tercer numero: "))
print(f"el promedio de tus numeros es {(num1 +num2 + num3)/3}")

"""
20. Divisible por 5
"""
num1 = int(input("ingresa un numero: "))
if(num1%5 == 0):
    print("es divisible por 5")
else:
    print("no es divisible por 5")
