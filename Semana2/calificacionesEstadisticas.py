def promediar (val1, val2):
    val2=0
    for x in val1:
        val2 = val2 + x
    return val2 /len(val1)



calificaciones = []
mayores = []
promedio = 0
cuenta = 0
act = True
while act:
    control = (input("""¿Que desea hacer? 
                        1. ingresar calificaciones 
                        2. conocer estado del curso 
                        3. calcular promedio
                        4. buscar calificaciones mayores a un valor
                        5. verificacion y conteo
                        6. salir
                        """))
    
    match control:
        case "1":
            temp = (input("Ingrese sus calificaciones, si son varias separarlas por comas: "))
            if temp.count(","): 
                for x in temp.split(","):
                    if x.replace(".", "", 1).replace(" ","").isdigit():
                        val = float(x.replace(" ",""))
                        if val >= 0 and val <= 100:
                            calificaciones.append(val)
                        else:
                            print(f"El valor {x} no es valido, es un numero fuera de rango")
                    else:
                        print(f"El valor {x} no es valido o, no es un numero")
            else:
                if temp.replace(".", "", 1).replace(" ","").isdigit():
                    calificaciones.append(float(temp))
                else:
                    print(f"El valor {temp} no es valido")

        case "2":
            if len(calificaciones) == 0:
                print("No hay calificaciones")
            else:
                promedio = promediar(calificaciones, promedio)
                if promedio == 100:
                    print("notas perfectas")
                elif promedio >= 70:
                    print("Aprobado")
                elif promedio >= 60:
                    print("Regular")
                else:
                    print("Reprobado")
                
        case "3":
            if len(calificaciones) == 0:
                print("No hay calificaciones")
            else:
                promedio = promediar(calificaciones,promedio)
                print(f"El promedio de las calificaciones hasta ahora es: {promedio}, en un total de {len(calificaciones)} calificaciones")
        case "4":
            if len(calificaciones) == 0:
                print("No hay calificaciones")
            else:
                valor = input("Ingrese el valor a comparar: ")
                if valor.replace(".", "", 1).replace(" ","").isdigit():
                    mayores.clear()
                    cuenta = 0
                    valor = float(valor)
                    while cuenta < len(calificaciones): 
                        if calificaciones[cuenta] > valor:
                            mayores.append(calificaciones[cuenta])
                        cuenta += 1
                    print(f"Las calificaciones mayores a {valor} son: {mayores}")
                else:
                    print(f"El valor {valor} no es valido")
        case "5":
            if len(calificaciones) == 0:
                print("No hay calificaciones")
            else:
                valor = input("Ingrese el valor a buscar: ")
                if valor.replace(".", "", 1).replace(" ","").isdigit():
                    cuenta = 0
                    valor = float(valor)
                    for x in calificaciones:
                        if x == valor:
                            cuenta += 1
                    print(f"La calificacion igual a {valor} se repite en tus notas {cuenta} veces")
                else:
                    print(f"El valor {valor} no es valido")
        case "6":
            act = False
        case _:
            print("Opcion no valida")