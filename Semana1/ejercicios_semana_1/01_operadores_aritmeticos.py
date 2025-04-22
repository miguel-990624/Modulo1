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