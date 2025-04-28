"""
nombre

edad

Tipo de personaje: heroe, antiheroe, villano

estado: full, herido, fatigado

poderes: tiene o no?? y cuales ?? tiene debilidades ??

solo: si o no?? el compañero tiene poderes ??

situaciones: salvar a alguien, un villano amenaza la ciudad, trabajo social, todas las anteriores

en que estado va a quedar la ciudad 
"""
poder = 100
nombre = input ("Dame el nombre del poderoso: ")
edad = int(input(f"Que edad tiene {nombre}: "))
tipo = input(f"""Que tipo de personaje es {nombre}: 
                1. Heroe
                2. Antiheroe
                3. Villano
             """)
estado = input(f"""En que estado esta {nombre}:
                1. Melo
                2. Cansado
                3. Inconciente
                4. Herido
               """)
poderes1=input(f"""{nombre} tiene poderes? 
                1. Si
                2. No
               """)
if poderes1 == "1" or poderes1.lower() == "si":
    poderes2 = input("""Que poderes?
                        1. Volar
                        2. Super Fuerza
                        3. Super velocidad
                        4. Dinero
                        5. Psiquicos
                     """)
else:
    print("Esperemos que no los necesite")

if tipo == "1" or tipo.lower() == "heroe":
    situacion = input(f"""Que sucede en saltadilla? (1-4)
                        1. Mojojo secuestro al alcalde
                        2. Invasion Alien
                        3. Asalto a un banco
                        4. Gato en un arbol
                      """)
    if situacion == "1":
        if estado == "1" or estado.lower() == "melo":
            print("Estas habilitado para luchar contra el villano ")
        elif estado == "2" or estado.lower() == "cansado":
            solo = input(f"""Estas solo o acompañado?
                            1. Solo
                            2. Acompañado  
                          """)
            if solo == "1" or solo.lower() == "solo":
                print("Espera a las chicas superpoderosas")
            elif solo == "2" or solo.lower() == "acompañado":
                print("suerte en tu pelea, la union hace la fuerza")
            else:
                print("Error, se murio el alcalde")
        elif estado == "3" or estado.lower() == "inconciente":
            print("Incapacitado, gano mojojo")
        elif estado == "4" or estado.lower() == "Herido":
            dolor = input("""Que tan grave: (1-3)
                            1. Dolor de cabeza
                            2. Demasiado
                            3. Poco
                          """)
            if dolor == "1":
                print("Tomate alguito y melo")
            elif dolor == "2":
                print("Primero curate, luego hacemos reelecciones de alcalde")
            elif dolor == "3":
                print("Buena suerte en la pelea")
            else:
                print("Estas muerto")
    elif situacion == "2":
        if estado == "2" or estado.lower() == "melo":
            print("Estas habilitado para luchar contra el villano ")
        elif estado == "2" or estado.lower() == "cansado":
            solo = input(f"""Estas solo o acompañado?
                            1. Solo
                            2. Acompañado  
                          """)
            if solo == "1" or solo.lower() == "solo":
                print("Espera a las chicas superpoderosas")
            elif solo == "2" or solo.lower() == "acompañado":
                print("suerte en tu pelea, la union hace la fuerza")
            else:
                print("Error, se murio el alcalde")
        elif estado == "3" or estado.lower() == "inconciente":
            print("Incapacitado, gano mojojo")
        elif estado == "4" or estado.lower() == "Herido":
            dolor = input("""Que tan grave: (1-3)
                            1. Dolor de cabeza
                            2. Demasiado
                            3. Poco
                          """)
            if dolor == "1":
                print("Tomate alguito y melo")
            elif dolor == "2":
                print("Primero curate, luego hacemos reelecciones de alcalde")
            elif dolor == "3":
                print("Buena suerte en la pelea")
            else:
                print("Estas muerto")
            