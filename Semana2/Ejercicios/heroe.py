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
    if situacion == "2":
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