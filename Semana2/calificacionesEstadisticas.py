"""
Esta es una funcion de promediar, se va a usar al menos en dos opciones, entonces es mas eficiente
y menos espacio consumido en lineas, hacer una funcion que promedia, me retorna el valor acumulado de 
cada calificacion y lo divide sobre el numero total de calificaciones
"""
def promediar (val1, val2):
    val2=0
    for x in val1:
        val2 = val2 + x
    return val2 /len(val1)


"""
Voy a declarar las variables que voy a usar en la parte de arriba por orden en el codigo, se declararan
vacias o en cero, y el la variable de control si el ciclo esta activo o no, en verdadero para que el codigo
se pueda ejecutar. tengo en orden el arreglo donde guardare las calificaciones, el arreglo donde 
se van a guardar las calificaciones mayores al valor buscado, el promedio inicial que es cero, una variable
cuenta que va a contar la posicion del arreglo de calificaciones, por que las instrucciones dicen que debo 
hacer este proceso con un ciclo while y no con un for, entonces debo llevar un contador para poder detener 
el ciclo y el controlador de si el codigo se sigue ejecutando o no.
"""
calificaciones = []
mayores = []
promedio = 0
cuenta = 0
act = True

"""
Aqui inicia el ciclo, que me va a dar 6 opciones, como aparece en el menu, me parece que es mas eficiente en
este caso usar un while para el control, siento que tengo mas control sobre salir o que se ejecute, por que 
solo va a estar pendiente de una condicion, si se cumple bien y sino se sale.
"""
while act:
    """
    El menu se va a usar utilizando un match, que va a verficiar el valor que se le ingresa al
    controlador, y dependiendo de la opcion que se elija, se ejecutan las instrucciones que el
    usuario desee, entonces va a estar pendiente que el usuario ingrese un valor valido y va a
    hacer match con las opciones que estan escritas, sino el caso default se va a ejecutar, que es
    el que me dice que la opcion no es valida, y me vuelve a preguntar que desea hacer.
    """
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
            """
            Aqui se van a ingresar las calificaciones, como se pidio el sistema va a permitir que se ingresen
            varias calificaciones a la vez, todas mientras se separen por comas, para resolver esto preferi
            dejar que el usuario ingrese la informacion como un string por que es mas facil realizar las 
            validaciones que hice sobre un string.

            Primero se ingresa la informacion, luego si valida si la informacion tiene comas, si tiene comas
            entonces voy a iniciar un ciclo for, que sobre lo que tengo entendido que hace el metodo split, es que
            me separa el string en partes, en plan que si tengo "1 , 2" voy a tener "1" y "2". Sobre el string 
            dividido voy a relizar aun mas validaciones, para a segurarme que en primera instacia, sea un numero 
            que me estan ingresando, retirando los primeros . que encuentre en el string y los espacios para validar 
            que si sea posible convertirlo en un numero, luego lo convierto en un numero retirando todos los espacios
            que el usuario haya podido ingresar, despues de esto valido que el numero este en el rango que se 
            requiere, de ser asi, se le hace un append al arreglo de calificaciones, con este valor, de no ser asi,
            se lanza un mensaje de error, para que el usuario sepa cual no es un valor valido de los ingresados usando
            un f-string que me permite precisamente mostrar el valor que quiero.
            """
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
                """
                Si el usuaio no ingresa comas, voy a hacer el proceso anterior sin necesidad de un ciclo for, puesto que
                solo tengo un valor. Se realizan las mismas validaciones que en el proceso de si es convertible a un numero
                si esta dentro de paramentro y tambien se convierte en un numero eliminando los espacios que tenga.

                """
                if temp.replace(".", "", 1).replace(" ","").isdigit():
                    calificaciones.append(float(temp.replace(" ","")))
                else:
                    """
                    Aqui se da un mensaje de error, si el valor ingresado no es posible de realizar nada de lo anterior, entonces 
                    no es posible usarlo como calificacion.
                    """
                    print(f"El valor {temp} no es valido")

        case "2":
            """
            Si no hay valores aun ingresados, osea que el largo del arreglo de calificaciones es cero, entonces
            se lanza un mensaje de error, para que el usuario sepa que no hay calificaciones, no es posible verificar
            como esta el curso si no hay calificaciones. Este proceso se repite con cada uno de los siguientes procesos.
            """

            if len(calificaciones) == 0:
                print("No hay calificaciones")
            else:
                """
                Si hay calificaciones, entonces se usa la funcion promediar que se declaro al inicio, para que me sobreescriba 
                el valor promedio y dependiendo de este valor, se da un mensaje diferente para que el usuario conozca su estado
                en el curso.

                """
                promedio = promediar(calificaciones, promedio)
                if promedio == 100:
                    print(f"notas perfectas: {promedio}")
                elif promedio >= 70:
                    print(f"Aprobado: {promedio}")
                elif promedio >= 60:
                    print(f"Regular: {promedio}")
                else:
                    print(f"Reprobado: {promedio}")
                
        case "3":
            if len(calificaciones) == 0:
                print("No hay calificaciones")
            else:
                """
                Aqui se usa la funcion promediar que se declaro al inicio, para que me sobreescriba
                el valor promedio y se le da este valro al usuario, para que sepa en el total de calificaciones
                que lleva a la fecha, cuanto es el promedio de lo que saca.
                """

                promedio = promediar(calificaciones,promedio)
                print(f"El promedio de las calificaciones hasta ahora es: {promedio}, en un total de {len(calificaciones)} calificaciones")
        case "4":
            if len(calificaciones) == 0:
                print("No hay calificaciones")
            else:

                """
                Aqui se le pide al usuario que ingrese un valor, este valor se le hacen verificaciones apropiadas para poder realizar el proceso,
                se vacia el arreglo mayores, para sobreeescribirlo sin ningun conflicto, y por ultimo se regresa la cuenta a 0 que es la variable 
                de control sobre el ciclo while, para poder recorrer todas las calificaciones.

                El ciclo while esta encargado de hacer una verificacion de si el numero en la posicion x es mayo al ingresado, de ser asi, se
                hace un append al arreglo mayores con ese valor, y se mueve a la siguiente posicion, cuando no hay mas valores, se sale del 
                ciclo y se imprime en consola, el arreglo mayores y cuantas calificaciones hay mayores al valor ingresado.
                """
                valor = input("Ingrese el valor a comparar: ")
                if valor.replace(".", "", 1).replace(" ","").isdigit():
                    mayores.clear()
                    cuenta = 0
                    valor = float(valor.replace(" ",""))
                    while cuenta < len(calificaciones): 
                        if calificaciones[cuenta] > valor:
                            mayores.append(calificaciones[cuenta])
                        cuenta += 1
                    print(f"""Las calificaciones mayores a {valor} son: {mayores}.
                          En total son {len(mayores)} de {len(calificaciones)} calificaciones""")
                else:
                    print(f"El valor {valor} no es valido")
        case "5":
            if len(calificaciones) == 0:
                print("No hay calificaciones")
            else:
                valor = input("Ingrese el valor a buscar: ")
                if valor.replace(".", "", 1).replace(" ","").isdigit():
                    cuenta = 0
                    valor = float(valor.replace(" ",""))
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