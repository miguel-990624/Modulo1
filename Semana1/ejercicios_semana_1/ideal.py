# personalidad, humor, gustos, Mascotas, bailar, 
puntos = 0
personalidad = input("""Dime, como calificas tu personalidad:
                        1. Alegre
                        2. Temperamental
                        3. Tranquila
                        4. Otra
                     """).lower()
if personalidad == "1" or personalidad == "alegre":
    puntos += 20
    pregunta = int(input("Que tan frecuentemente te ries, en una escala del 1 al 10: "))
    if pregunta >= 8:
        puntos += 10
    elif pregunta >= 5:
        puntos += 15
    else:
        puntos += 0
    pregunta = input("Te gustan los juegos de palabras Si o No: ").lower()
    if pregunta == "si":
        puntos += 10
    elif pregunta == "no":
        puntos -= 5
    else:
        print("Respuesta no valida")
elif personalidad == "2" or personalidad == "temperamental":
    puntos += 10
    pregunta = int(input("Que tan frecuentemente te enojas, en una escala del 1 al 10: "))
    if pregunta >= 8:
        puntos -= 10
    elif pregunta >= 5:
        puntos += 5
    else:
        puntos += 10
    pregunta = input("Celos? Si o No: ").lower()
    if pregunta == "si":
        puntos -= 5
    elif pregunta == "no":
        puntos += 10
    else:
        print("Respuesta no valida")
elif personalidad == "3" or personalidad == "tranquila":
    puntos += 15
else:
    puntos += 0

parche = input("""Que prefieres 
                    1. Salir
                    2. Quedarte en casa: 
               """).lower()
if parche == "salir" or parche == "1":
    puntos += 10
    pregunta = input("Te gusta bailar? Si o No: ").lower()
    if pregunta == "si":
        puntos += 15
    elif pregunta == "no":
        puntos -= 5
    else:
        print("Respuesta no valida")
    pregunta = input("""Que prefieres (1 o 2): 
                        1. salir a comer
                        2. salir con amigos: 
                     """)
    if pregunta == "1":
        puntos += 10
    elif pregunta == "2":
        puntos += 15
    else:
        print("Respuesta no valida")
elif parche == "Quedarte en casa" or parche == "2":
    puntos += 5
    pregunta = input("Ver peliculas o series? Si o No: ").lower()
    if pregunta == "si":
        puntos += 10
    elif pregunta == "no":
        puntos -= 5
    else:
        print("Respuesta no valida")
    pregunta = input("""Que prefieres: 
                     1. Cocinamos
                     2. pedimos domicilio: 
                     """).lower()
    if pregunta == "1":
        puntos += 15
    elif pregunta == "2":
        puntos += 5
    else:
        print("Respuesta no valida")

animales = input("Te gustan los animales? Si o No: ").lower()
if animales == "si":
    puntos += 10
    pregunta = input("Tienes mascotas? Si o No: ").lower()
    if pregunta == "si":
        puntos += 5
        pregunta = input("""Cuanto quieres a tu mascota (1-4): 
                            1. Es lo que mas quiero
                            2. Es mi mejor amigo
                            3. Es mi compañero
                            4. No tengo mascota
                         """)
        if pregunta == "1":
            puntos -= 10
        elif pregunta == "2":
            puntos += 5
        elif pregunta == "3":
            puntos += 5
        elif pregunta == "4":
            puntos += 0
        else:
            print("Respuesta no valida")
    elif pregunta == "no":
        puntos += 0
    else:
        print("Respuesta no valida")
elif animales == "no":
    puntos -= 5
else:
    print("Respuesta no valida")

generos = input("""Que prefieres en tu entretenimiento?
                    1.Terror
                    2.Comedia
                    3.Romance
                    4.Documentales
                    5.Fantasia 
                """).lower()
if generos == "terror" or generos == "1":
    puntos += 10
    pregunta = input("""Que prefieres?
                        1. thriller
                        2. suspenso
                        3. psicologico 
                     """).lower()
    if pregunta == "thriller" or pregunta == "1":
        puntos += 5
    elif pregunta == "suspenso" or pregunta == "2":
        puntos += 10
    elif pregunta == "psicologico" or pregunta == "3":
        puntos += 15
    else:   
        print("Respuesta no valida")
    pregunta = input("""Te asustas facilmente?
                        1. Si
                        2. No 
                     """).lower()
    if pregunta == "si" or pregunta == "1":
        puntos += 10
    elif pregunta == "no" or pregunta == "2":
        puntos += 5
    else:       
        print("Respuesta no valida")
elif generos == "comedia" or generos == "2":
    puntos += 15
    pregunta = input("""Que prefieres?
                        1. comedia romantica
                        2. comedia negra
                        3. comedia tradicional 
                     """).lower()
    if pregunta == "comedia romantica" or pregunta == "1":
        puntos += 10
    elif pregunta == "comedia negra" or pregunta == "2":
        puntos += 10
    elif pregunta == "comedia de tradicional" or pregunta == "3":
        puntos += 15
    else:       
        print("Respuesta no valida")
    pregunta = input("Conoces a Monty Python? Si o No: ").lower()
    if pregunta == "si":
        puntos += 15
    elif pregunta == "no":
        puntos += 0
    else:       
        print("Respuesta no valida")
elif generos == "romance" or generos == "3":
    puntos += 5
    pregunta = input("Te gustan las tragedias? Si o No: ").lower()
    if pregunta == "si":
        puntos += 5
    elif pregunta == "no":
        puntos += 0
    else:       
        print("Respuesta no valida")
    pregunta = input("Haciendo arrunchis? Si o No: ").lower()
    if pregunta == "si":
        puntos += 20
    elif pregunta == "no":
        puntos -= 20
    else:       
        print("Respuesta no valida")
elif generos == "documentales" or generos == "4":
    puntos += 15
    pregunta = input("""Tipo de documental favorito:
                        1. Historico
                        2. Animales
                        3. Naturales
                        4. Espacio
                     """).lower()
    if pregunta == "historico" or pregunta == "1": 
        puntos += 5
    elif pregunta == "animales" or pregunta == "2":
        puntos += 10
    elif pregunta == "naturales" or pregunta == "3":
        puntos += 10
    elif pregunta == "espacio" or pregunta == "4":
        puntos += 15
    else:
        print("Respuesta no valida")
elif generos == "fantasia" or generos == "5":
    puntos += 10
    pregunta = input("""Que prefieres: 
                        1. Alta fantasia (Lotr)
                        2. Fantasia oscura
                        3. Ciencia ficcion
                     """).lower()
    if pregunta == "alta fantasia" or pregunta == "1":
        puntos += 15
    elif pregunta == "fantasia oscura" or pregunta == "2":
        puntos += 10
    elif pregunta == "ciencia ficcion" or pregunta == "3":
        puntos += 10
    else:
        print("Respuesta no valida")

else:
    print("Respuesta no valida")

orden = input("Te gusta el orden? Si o No: ").lower()
if orden == "si":
    puntos += 10
    pregunta = input("Te molesta el desorden? Si o No: ").lower()
    if pregunta == "si":
        puntos += 0
    elif pregunta == "no":
        puntos += 5
    else:
        print("Respuesta no valida")
elif orden == "no":
    puntos -= 10
else:
    print("Respuesta no valida")

boda = input("Te gustaria casarte? Si o No: ").lower()
if boda == "si":
    puntos += 10
elif boda == "no":  
    puntos -= 10
else:
    print("Respuesta no valida")
    
crias = input("Te gustaria tener hijos? Si o No: ").lower()
if crias == "si":
    puntos += 10
elif crias == "no":  
    puntos += 0
else:
    print("Respuesta no valida")

trabajo = input("Te gustaria trabajar? Si o No: ").lower()
if trabajo == "si":
    puntos += 10
    pregunta = input("Te gusta tu trabajo? Si o No: ").lower()
    if pregunta == "si":
        puntos += 10
    elif pregunta == "no":
        pregunta = input("Te gustaria cambiar de trabajo? Si o No: ").lower()
        if pregunta == "si":
            puntos += 5
        elif pregunta == "no":
            puntos -= 20
        else:
            print("Respuesta no valida")
    else:
        print("Respuesta no valida")
elif trabajo == "no":   
    puntos -= 10
else:   
    print("Respuesta no valida")

print(f"Tu puntaje es: {puntos}")
if puntos >= 170:
    print("Quisiera conocerte, salgamos")
elif puntos >= 110:
    print("podriamos conocernos, minimo seriamos buenos amigos")
elif puntos >= 50:
    print("podriamos ser amigos")
else:
    print("No creo que seriamos ni amigos")