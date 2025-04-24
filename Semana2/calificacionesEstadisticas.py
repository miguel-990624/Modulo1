suma = 0
def promedio(var):
    for x in var:
        suma += x
    return suma / len(var)

calificaciones = []
act = True
while act:
    control = int(input("""¿Que desea hacer? 
                        1. ingresar calificaciones 
                        2. conocer estado del curso 
                        3. calcular promedio
                        4. buscar calificaciones mayores a un valor
                        5. verificacion y conteo
                        6. salir
                        """))
    match control:
        case 1:
            temp = (input("Ingrese sus calificaciones, si son varias separarlas por comas: "))
            if temp.count(","): 
                for x in temp.split(","):
                    if x.replace(".", "", 1).replace(" ","").isdigit():
                        calificaciones.append(float(x))
                    else:
                        print(f"El valor {x} no es valido")
            else:
                if temp.replace(".", "", 1).replace(" ","").isdigit():
                    calificaciones.append(float(temp))
                else:
                    print(f"El valor {temp} no es valido")

        case 2:
            if len(calificaciones) == 0:
                print("No hay calificaciones")
            else:
                
        case 3:
            if len(calificaciones) == 0:
                print("No hay calificaciones")
            else:
                print("El promedio es: ", promedio)
        case 4:
            if len(calificaciones) == 0:
                print("No hay calificaciones")
            else:
                valor = int(input("Ingrese el valor a comparar: "))
                for i in calificaciones:
                    if i > valor:
                        print(i)
        case 5:
            if len(calificaciones) == 0:
                print("No hay calificaciones")
            else:
                print("El conteo de calificaciones es: ", len(calificaciones))
        case 6:
            act = False
        case _:
            print("Opcion no valida")