"""
1. Calculadora de promedio con validación
"""
calificiones = []
total = 0

for x in range(3):
    cal = int(input(f"ingresa tu calificacion {x+1}: "))
    calificiones.append(cal)

for x in range(len(calificiones)):
    if(10 >= calificiones[x] >= 0):
        total = total + calificiones[x]
        print(total)
    else:
        print(f"la calificacion {x+1}, no es posible como nota, ingrese parametros entre el 0 y 10")
        break
    if(x == 2):
        print(f"su promedio de calificaciones es: {total/3}")
        if(total/3 >= 6):
            print("usted aprovo el curso")
        else:
            print("usted no aprovo el curso")

"""
2. Años para jubilarse
"""
def jubilar(var1, var2):
    if(var1 < var2):
        print(f"Aun no te jubilas, te faltan {var2 - var1} años para la jubilacion")
    else:
        print("felicitaciones por tu jubilacion, ya te puedes jubilar")

genero = input("Ingrese su genero, si es hombre H si es mujer M: ")
edad=int(input("ingrese su edad: "))

if(genero == "H"):
    jubilar(edad,65)
elif(genero == "M"):
    jubilar(edad,60)
else:
    print("genero no valido")


"""
3. Calculadora de salario neto
"""
salario=int(input("ingresa tu salario: "))
descuento= int(input("ingresa tu descuento mensual: "))
print(f"tu salario tras reducciones es de {salario -(salario*descuento)/100}")

"""
4. ¿Compatibles?
"""
nombres = []
edades = []
print("veamos que tan compatibles son")
for x in range(2):
    nombre = input(f"ingresa el nombre {x+1}: ")
    edad = int(input(f"ahora, {nombre} ingresa tu edad: "))
    nombres.append(nombre)
    edades.append(edad)

if(nombres[0] != nombres[1]):
    if(edades[0]>=18 and edades[1]>= 18):
        if(10 > edades[0] - edades[1] > -10):
            print("son compatibles")
        else:
            print("no son compatibles")
    else:
        print("no son compatibles")
else:
    print("no son compatibles")

"""
5. Calculadora de múltiplos
"""
num1 = int(input("ingrese un numero que quiera conocer si tiene multiplo: "))
num2 = int(input("ingrese el numero que cree que es multiplo de su anterio opcion: "))
if(num1 % num2 == 0):
    print(f"{num1} es multiplo de {num2}")
else:
    print("no son multiplos")

"""
6. Número mágico
"""
num1 = int(input("ingrese un numero: "))
if(num1 % 3 == 0 and num2 % 5 == 0):
    print("FizzBuzz")
elif(num1 % 3 == 0):
    print("Fizz")
elif(num1 % 3 == 0):
    print("Buzz")
else:
    print("Numero magico")


"""
7. Conversor de unidades avanzado
"""
num1=float(input("ingrese un numero de kilometros"))
print(f"{num1}km = {num1*1000}metros, {num1*100000}cm, {num1*1000000}mm")
