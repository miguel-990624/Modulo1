contactos = {}
control = True
while control :
    opcion = int(input("""Que desea hacer?
                        1.  Agregar un nuevo contacto
                        2.  Mostrar todos los contactos
                        3.  Buscar un contacto
                       """))
    if opcion == 1:
        nombre = input("Ingresa el nombre de tu contacto: ")
        numero = int(input("Ingresa su numero de telefono: "))
        contactos[nombre] = numero
    elif opcion == 2:
        for clave, valor in contactos.items():
            print(f"{clave} => {valor}")
    elif opcion == 3:
        verificacion = input("Que contacto buscas en tu directorio: ")
        if verificacion in contactos:
            print(f"Tienes a {verificacion} agregad@ en tus contactos")
    else:
        print("Opcion no valida")