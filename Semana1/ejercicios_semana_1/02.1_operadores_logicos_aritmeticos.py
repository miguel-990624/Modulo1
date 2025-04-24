"""
1.Acceso exclusivo al evento
"""
edad = int(input("ingresa tu edad: "))
invitacion = int(input("Numero de invitacion: "))
if edad >= 21 and invitacion == 777:
    print("Bienvenido al evento")
else:       
    print("No puedes ingresar al evento")

"""
2. Descuento por edad o monto
"""
edad = int(input("ingresa tu edad: "))
monto = int(input("ingresa el monto de la compra: "))
if edad < 60 or monto > 100:
    print("Tienes un descuento del 10%")
else:
    print("No tienes descuento")

"""
3. Verificación para participar en un concurso internacional
"""
edad = int(input("ingresa tu edad: "))
nacionalidad = input("ingresa tu nacionalidad: ")
documento = int(input("ingresa tu documento de identidad: "))

if 30 >= edad >= 18 and nacionalidad.lower() != "antartida" and documento != 0:
    print("Puedes participar en el concurso internacional")
else:
    print("No puedes participar en el concurso internacional")

"""
4. Evaluación académica de estudiante
"""
nota1 = int(input("ingresa la nota 1: "))
nota2 = int(input("ingresa la nota 2: "))

if nota1 >= 6 and nota2 >= 6:
    print("Aprobado")
else:
    print("Reprobado")

"""
5. Conexión segura en la red
"""
protocolo = input("ingresa el protocolo, http o https: ")
puerto = int(input("ingresa el puerto, 443 o 80: "))
if (protocolo == "https" and puerto == 443):
    print("Conexión segura")
else:
    print("Conexión insegura")


"""
6. Requisitos para obtener una beca
"""
promedio = float(input("ingresa tu promedio: "))
materias = int(input("ingresa el numero de materias: "))
ingresos = int(input("ingresa tus ingresos: "))
if promedio >= 8 and materias < 3 and ingresos <= 1500:
    print("Eres elegible para la beca")
else:   
    print("No eres elegible para la beca")

"""
7. Acceso a atracción en parque temático
"""
estatura = float(input("ingresa tu estatura en cm: "))
edad = int(input("ingresa tu edad: "))

if estatura >= 140 and 60 >= edad >= 10:
    print("Puedes acceder a la atracción")
else:
    print("No puedes acceder a la atracción")

"""
8. Validación de contraseña segura
"""

contrasena = input("ingresa tu contraseña: ")
if len(contrasena) >= 8:
    for x in range(len(contrasena)):
        if x < len(contrasena) - 2:
            num1 = contrasena[x]
            num2 = contrasena[x+1]
            num3 = contrasena[x+2]

        try:
            num1 = int(num1)
            num2 = int(num2)
            num3 = int(num3)
        except:
            num1 = 0
            num2 = 0
            num3 = 0
        
        if num1 + 2 == num3 and num2 + 1 == num3:
            print("Contraseña insegura")
            break

        if x == len(contrasena) - 1:
            print("Contraseña segura")
else:
    print("Contraseña insegura")

"""
9. Evaluación para tarjeta de crédito
"""
ingresos = int(input("ingresa tus ingresos: "))
deuda = input("Tienes una deuda, si o no?")

if ingresos >= 2500 :
    print("Eres elegible para la tarjeta de crédito")
elif ingresos >= 1500 and deuda == "no":
    print("Eres elegible para la tarjeta de crédito")
else:
    print("No eres elegible para la tarjeta de crédito")

"""
10. Horario permitido para clases
"""
hora = int(input("ingresa la hora, en formato militar del 0 a las 23 horas : "))
if 18>= hora >= 8 and hora != 13:
    print("Horario permitido para clases")
else:
    print("Horario no permitido para clases")

