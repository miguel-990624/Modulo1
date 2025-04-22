"""
El ejercicio esta en mi repositorio: https://github.com/miguel-990624/Modulo1
"""
print("Calculadora de compra")
nombre = input("ingrese el nombre del producto deseado: ")
unitario = input("ingrese el valor unitario del producto deseado: ")
cantidad = input("ingrese la cantidad de productos deseados, en numeros enteros: ")
descuento = input("ingrese el valor de su descuento entre el 0 y 100, si aplica: ")

"""
Cree una funcion que me calcula el valor de un descuento para llamarla dentro del codigo
si el cliente ingresa bien los datos
"""
def calcular () :
    total = unitario * cantidad
    totalDescontado = ((100 - descuento)/100) * total
    print(f"Para el producto {nombre}, el precio total es de: ${total:.2f}, con el valor del descuento ${totalDescontado:.2f}")
    
"""
En stack overflow encontre que lo mas normal es EAFP(easier ask forgiveness than permission), que seria usar el metodo try, except, pero tambien
ponian que existe el metodo replace, que me va a buscar el punto decimal, lo va a quitar, y solo lo va a hacer 1 vez
de modo que cuando el cliente ingrese un numero asi tenga un decimal, lo va a reconocer como numero
por que tambien estoy usando el metodo isdigit para verificar que sea un valor numerico.
"""
if(unitario.replace(".", "", 1).isdigit()):
    """
    Voy a sobreescribir el valor que ingreso el cliente y con el mismo valor convertido al tipo de variable que necesito
    """
    unitario = float(unitario)
    """
    Aqui voy no solo a ver que si sea un numero, sino que el valor de unitario sea mayor que 0 por que no existen productos con precios
    negativos
    """
    if(cantidad.replace(".", "", 1).isdigit() and unitario > 0):
        cantidad = float(cantidad)
        """
        Esta condicional tiene una condicion extra y es que para verificar que un numero sea entero, su modulo de 1 debe ser 0,
        entonces como no es posible comprar productos por partes, verificare que el valor ingresado sea un entero
        """
        if(descuento.replace(".", "", 1).isdigit() and cantidad > 0 and cantidad%1 == 0):
            descuento = float(descuento)
            if(100 >= descuento >= 0 ):
                """
                Cuando todas las condiciones se cumplan, llamo mi funcion que me va a hacer el calculo
                """
                calcular()
            else:
                print("valor de descuento fuera del rango")
        elif(cantidad < 0 or cantidad%1 != 0):
            print("Cantidad de productos ordenados debe ser mayor a 0 y un numero entero, no se admiten decimales")
        else:
            print("Valor de descuento no valido, no es un numero")
    elif(unitario < 0):
        print("Valor de precio unitario menor a 0")
    else:
        print("Cantidad de productos no valida, no es un numero")
else:
    print("Valor de precio unitario no valido, no es un numero")
"""
Documentacion:
https://stackoverflow.com/questions/4138202/using-isdigit-for-floats
https://www.w3schools.com/python/ref_string_replace.asp
https://www.freecodecamp.org/news/python-convert-string-to-int-how-to-cast-a-string-in-python/
"""