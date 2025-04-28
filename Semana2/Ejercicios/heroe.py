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
                        2. Invacion alien
                        3. Gato en un arbol
                      """)
    if situacion == "1":
        if poderes2 == "4" or estado.lower() == "dinero":
            pagar = input("""Quieres pagarle a Mojojo para que libere al alcalde?
                          1. Si
                          2. No
                          """)
            if pagar == "1" or pagar.lower() == "si":
                print("Una vez mas lograste slavar saltadilla con tus grandes poderes")
            else:       
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
                        if poderes2 == "5" or poderes2.lower() == "psiquicos":
                            poderes3 = input("""Tus poderes son de larga distancia?
                                                1. Si
                                                2. No
                                            """)
                            if poderes3 == "1" or poderes2.lower() == "si":
                                print("Derrotaste a mojojo desde tu escondite, y el alcalde se salvo, pero nunca nadie supo quien salvo realmente la ciudad")
                            elif poderes3 == "2" or poderes2.lower() == "no":
                                print("Mojojo se comio al alcalde, pero no te preocupes el siguiente alcalde sera mas agradable")
                            else:
                                print("Tratar de usar tus poderes en tu condicion te dio una aneurisma y te moriste")
                    elif dolor == "3":
                        if poderes1 == "1" or poderes1.lower() == "si":
                            if 15 <= edad <= 50:
                                print(f"gracias a tus poderes {nombre} lograste llegar a la escena justo a tiempo y pelear con mojojo, Ahora quedaste con heridas profundas y la ciudad sin protector")
                            else:
                                print(f"A tu edad, mejor dejale esto a los profesionales")
                        else:
                            print("Sin poderes y herido, no eres rival para mojojo, no te recomiendo pelear, solo seria mas trabajo para las chicas superpoderosas")
                    else:
                        print("Estas muerto")
    elif situacion == "2":
                if estado == "1" or estado.lower() == "melo":
                    print("Estas habilitado para luchar contra los aliens ")
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
                        print("Error, conquistaron saltadilla")
                elif estado == "3" or estado.lower() == "inconciente":
                    print("Incapacitado, ganaron los aliens, los abdujeron a todos y se los comieron")
                elif estado == "4" or estado.lower() == "Herido":
                    dolor = input("""Que tan grave: (1-3)
                                    1. Dolor de cabeza
                                    2. Demasiado
                                    3. Poco
                                """)
                    if dolor == "1":
                        print("Tomate alguito y melo")
                    elif dolor == "2":
                        if poderes2 == "5" or poderes2.lower() == "psiquicos":
                            poderes3 = input("""Tus poderes son de larga distancia?
                                                1. Si
                                                2. No
                                            """)
                            if poderes3 == "1" or poderes2.lower() == "si":
                                print("Derrotaste a los aliens desde tu escondite, todos se salvaron, pero nunca nadie supo quien salvo realmente la ciudad")
                            elif poderes3 == "2" or poderes2.lower() == "no":
                                print("Los aliens destrozaron todo menos tu escondite, le tienen miedo a tus poderes psiquicos")
                            else:
                                print("Tratar de usar tus poderes en tu condicion te dio una aneurisma y te moriste")
                    elif dolor == "3":
                        if poderes1 == "1" or poderes1.lower() == "si":
                            if 15 <= edad <= 50:
                                print(f"gracias a tus poderes {nombre} lograste llegar a la escena justo a tiempo y pelear con lso aliens, Ahora quedaste con heridas profundas y la ciudad sin protector")
                            else:
                                print(f"A tu edad, mejor dejale esto a los profesionales")
                        else:
                            print("Sin poderes y herido, no eres rival para los aliens, no te recomiendo pelear, solo seria mas trabajo para las chicas superpoderosas")
                    else:
                        print("Estas muerto")
    elif situacion == "3":
        print("Los bomberos ya van en camino")

elif tipo == "2" or tipo.lower() == "antiheroe":
    situacion = input(f"""Que sucede en saltadilla? (1-4)
                        1. Va caer un misil en la ciudad?
                        2. Comprar una pizza
                        3. Rescate en el arbol
                        4. Gato en un arbol
                      """)
    if situacion == "1": 
        if estado == "1" or estado.lower() == "melo":
            print("Estas habilitado detener el mision pronto a caer ")
        elif estado == "2" or estado.lower() == "cansado":
            ("No estas en todas tus capacidades, deseas arriesgarte?")
            Arriesgarse = input(f"""No estas en todas tus capacidades, deseas arriesgarte?
                                1. Si
                                2. No""")
            if Arriesgarse == "si":
                print("Suerte en el combate :b")
            elif Arriesgarse == "No":
                print("Suerte en la casita entonces")
            else:
                print("Dije si o no")
        elif estado == "3" or estado.lower() == "inconciente":
            print("Despierta, Despierta")
        elif estado == "4" or estado.lower() == "herido":
            Quetanherido = input(f""" Que tan herido esta?
                        1. Mucho
                        2. Bastante
                        3. Poco
                      """)
            if Quetanherido == "1" or estado.lower == "mucho":
                print("No creo que una pizza sea lo mejor en tu condición")
            elif Quetanherido == "2" or estado.lower == "bastante":
                print("Va a ser dificil sanar a base de pizza")
            elif Quetanherido == "3" or estado.lower == "poco":
                print("Suerte con tu antojo jsafjas")
elif tipo == "3" or tipo.lower() == "Villano":
    situacion = input(f"""Que sucede en saltadilla? (1-4)
                        1. La ciudad se encuentra muy tranquila
                        2. Las personas estan felices en un parque
                        3. Un transporte de colegio va muy tranquilo
                        4. Un puente se encuentra estable
                      """)
    if situacion == "1":
        if estado == "1" or estado.lower() == "melo":
            print("Estas habilitado para quitar la tranquilidad de la ciudad ")
        elif estado == "2" or estado.lower() == "cansado":
            solo = input(f"""Estas solo o acompañado?
                            1. Solo
                            2. Acompañado  
                          """)
            if solo == "1" or solo.lower() == "solo":
                print("Igual puedes destrozar la ciudad")
            elif solo == "2" or solo.lower() == "acompañado":
                print("Mucho mejor, se puede quitar la tranquilidad y la paz de la ciudad")
            else:
                print("Explicate mejor ombee ")
        elif estado == "3" or estado.lower() == "inconciente":
            print("Incapacitado, gano el heroe")
        elif estado == "4" or estado.lower() == "Herido":
            dolor = input("""Que tan grave: (1-3)
                            1. Dolor de cabeza
                            2. Demasiado
                            3. Poco
                          """)
            if dolor == "1":
                print("Tomate alguito como un dolex y melo")
            elif dolor == "2":
                print("Primero curate, luego destrozamos la ciudad")
            elif dolor == "3":
                print("Buena suerte en la pelea, puedes quitar la paz en la ciudad")
            else:
                print("Estas muerto")
    elif situacion == "2":
        if estado == "2" or estado.lower() == "melo":
            print("Estas habilitado para quitar la felicidad del parque, con todaa ")
        elif estado == "2" or estado.lower() == "cansado":
            solo = input(f"""Estas solo o acompañado?
                            1. Solo
                            2. Acompañado  
                          """)
            if solo == "1" or solo.lower() == "solo":
                print("Igual dale, el mal que triunfe")
            elif solo == "2" or solo.lower() == "acompañado":
                print("Que chimbx, dale con toda")
            else:
                print("Explicate mejor ombee")
        elif estado == "3" or estado.lower() == "inconciente":
            print("Incapacitado, gano el heroe")
        elif estado == "4" or estado.lower() == "Herido":
            dolor = input("""Que tan grave: (1-3)
                            1. Dolor de cabeza
                            2. Demasiado
                            3. Poco
                          """)
            if dolor == "1":
                print("Tomate alguito como un dolex y melo")
            elif dolor == "2":
                print("Primero curate, luego quitamos la felicidad del parque")
            elif dolor == "3":
                print("Buena suerte en la pelea, puedes quitar la felicidad del parque")
            else:
                print("Estas muerto")
    elif situacion == "3":
        if estado == "2" or estado.lower() == "melo":
            print("Estas habilitado para quitar la tranquilidad del transporte del colegio ")
        elif estado == "2" or estado.lower() == "cansado":
            solo = input(f"""Estas solo o acompañado?
                            1. Solo
                            2. Acompañado  
                          """)
            if solo == "1" or solo.lower() == "solo":
                print("Igual dale, el mal que triunfe")
            elif solo == "2" or solo.lower() == "acompañado":
                print("Que chimbx, dale con toda")
            else:
                print("Explicate mejor ombee")
        elif estado == "3" or estado.lower() == "inconciente":
            print("Incapacitado, gano el heroe y la tranquilidad")
        elif estado == "4" or estado.lower() == "Herido":
            dolor = input("""Que tan grave: (1-3)
                            1. Dolor de cabeza
                            2. Demasiado
                            3. Poco
                          """)
            if dolor == "1":
                print("Tomate alguito como un dolex y melo")
            elif dolor == "2":
                print("Primero curate, luego quitamos la tranquilidad del transporte del colegio")
            elif dolor == "3":
                print("Buena suerte en la pelea, puedes quitar la quitar la tranquilidad del transporte del colegio")
            else:
                print("Estas muerto")
    elif situacion == "4":
        if estado == "2" or estado.lower() == "melo":
            print("Estas habilitado para quitar la estabilidad del puente ")
        elif estado == "2" or estado.lower() == "cansado":
            solo = input(f"""Estas solo o acompañado?
                            1. Solo
                            2. Acompañado  
                          """)
            if solo == "1" or solo.lower() == "solo":
                print("Igual dale, el mal que triunfe")
            elif solo == "2" or solo.lower() == "acompañado":
                print("Que chimbx, dale con toda")
            else:
                print("Explicate mejor ombee")
        elif estado == "3" or estado.lower() == "inconciente":
            print("Incapacitado, gano el heroe y la estabilidad del puente")
        elif estado == "4" or estado.lower() == "Herido":
            dolor = input("""Que tan grave: (1-3)
                            1. Dolor de cabeza
                            2. Demasiado
                            3. Poco
                          """)
            if dolor == "1":
                print("Tomate alguito como un dolex y melo")
            elif dolor == "2":
                print("Primero curate, luego quitamos la estabilidad del")
            elif dolor == "3":
                print("Buena suerte en la pelea, puedes quitar la estabilidad del puente")
            else:
                print("Estas muerto")        