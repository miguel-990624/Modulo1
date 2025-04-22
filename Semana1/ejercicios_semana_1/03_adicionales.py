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