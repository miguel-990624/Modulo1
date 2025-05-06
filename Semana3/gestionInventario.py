class Producto:
    def __init__(self, data):
        self.data = data

    def get(self, key):
        return self.data.get(key)
    
    def set (self, key, value):
        self.data[key] = value

togle = lambda x: not x

def add ():
    precio = input("ingrese el valor por unidad del producto: ")
    if precio.replace(".", "", 1).replace(" ","").isdigit():
        precio = float(precio.replace(" ",""))
        cantidad = input("ingrese la cantidad de productos que desea llevar: ")
        if cantidad.count(".") == 0 and cantidad.replace(" ","").isdigit():
            cantidad = int(cantidad.replace(" ",""))
            datosProducto = {"nombre":nombre, "precio":precio, "cantidad": cantidad}
            producto = Producto(datosProducto)
            carrito.append(producto)
        else:
            print("El dato ingresado no es un valor valido, intente de nuevo")
    else:
        print("El dato ingresado no es un valor valido, intente de nuevo")

"""
ingresar productos 2
"""
carrito = []
contador = 0
nombre = input("ingrese nombre del producto: ")
if len(carrito) == 0:
    add()
else:
    for i in carrito:
        if nombre.lower() == i.get("nombre").lower():
            print("Este producto ya se encuentra en su carrito")
            cantidad = input(f"ingrese la cantidad de productos adicionar, cuenta actual {i.get("cantidad")}: ")
            if cantidad.count(".") == 0 and cantidad.replace(" ","").isdigit():
                cantidad = int(cantidad.replace(" ",""))
                cantidad += i.get("cantidad")
                i.set("cantidad", cantidad)
                print(f"la cantidad fue correctamente actualizada, cantidad actual: {i.get("cantidad")}")
            else:
                print("El dato ingresado no es un valor valido, intente de nuevo")
            break
        elif (contador == len(carrito)):
            add()
        else:
            contador += 1

"""
Buscar por nombre
"""
busqueda = input("ingresa el nombre del producto que buscas: ")
if len(carrito) != 0:
    for i in carrito:
        if busqueda.lower() == i.get("nombre").lower():
            print("temporal")