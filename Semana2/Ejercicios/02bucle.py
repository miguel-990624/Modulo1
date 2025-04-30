"Contar del 1 al 10"
num1 ,num2 = 0 , 0
while num1 < 10:
    num1 +=1
    print(num1)

"Contar del 10 al 1"
num1 = 10
while num1 > 0:
    print (num1)
    num1 -= 1

"Sumar los numeros del 1 al 10"
num1 ,num2 = 0 , 0
while num1 < 10:
    num1 += 1
    num2 += num1
    print(num2)

"Pedir un numero positivo"
num1 = -1
while num1 < 0:
    num1=int(input("ingrese un numero positivo: "))

"Menu interactivo"
while num1 != "3":
    num1 = (input("""Que desea hacer:
                        1. Saludar
                        2. Despedirse
                        3. Salir
                     """))
    match num1:
        case "1":
            print("Hola, Como estas")
        case "2":
            print("Adios, Feliz dia")
        case "3":
            break
        case _:
            print("no es una opcion valida")

"Adivina el numero"
num1 = 555
while num2 != num1:
    num2 = int(input("ingresa la contraseña: "))
    if num2 > num1:
        print("muy alto")
    elif num2 < num1:
        print("muy bajo")
    else:
        print("Correcto")

"Contar vocales en una palabra"
palabra = input("ingresa una palabra: ")
num1= 0
num2 = 0
while num1 != len(palabra):
    if palabra[num1].lower() == "a" or palabra[num1].lower() == "e" or palabra[num1].lower() =="i" or palabra[num1].lower() =="o" or palabra[num1].lower() == "u":
        num2 +=1
    num1 += 1
print(f"numero de vocales es: {num2}")

"Validar contraseña"
palabra = "python123"
intento = ""
while intento != palabra:
    intento = input("ingrese contraseña: ")
    if intento != palabra:
        print("incorrecto")
    else:
        print ("correcto")

"Sumar hasta detenerse"
num2 = 0
condi = True
print("ingres numeros hasta el 0 y te dare la suma de los valores ingresados" \
"")
while condi:
    num1 = int(input("ingresa un numero: "))
    num2 += num1
    if num1 == 0:
        condi = False
        break
print(f"el total de su suma es: {num2}")

"Numero de intentos"
num1 = 0
condi = True
while condi:
    num1 = int(input("ingrese un numero entre el 1 y el 10: "))
    if 0 > num1 or num1 > 10:
        print("ingrese un numero en el rango deseado")
    else:
        print("correcto")
        break