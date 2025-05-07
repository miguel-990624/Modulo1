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

def update ():
    print("Este producto ya se encuentra en su carrito")
    cantidad = input(f"ingrese la cantidad de productos adicionar, cuenta actual {i.get("cantidad")}: ")
    if cantidad.count(".") == 0 and cantidad.replace(" ","").isdigit():
        cantidad = int(cantidad.replace(" ",""))
        cantidad += i.get("cantidad")
        i.set("cantidad", cantidad)
        print(f"la cantidad fue correctamente actualizada, cantidad actual: {i.get("cantidad")}")
    else:
        print("El dato ingresado no es un valor valido, intente de nuevo")

"""
ingresar productos 2
"""
carrito = []
while True:
    opcion = input("""
        --- Menu de opciones---
            1.  Agregar al carrito
            2.  Buscar en el carrito
            3.  Agregar mas productos
            4.  Eliminar productos
            5.  Valor total del carrito
            6.  Salir
          """)
    if opcion == "1":
        nombre = input("ingrese nombre del producto: ")
        if len(carrito) == 0:
            add()
        else:
            contador = 0
            for i in carrito:
                if nombre.lower() == i.get("nombre").lower() and (contador == len(carrito)):
                    update()
                    break
                elif (contador == len(carrito)-1):
                    add()
                else:
                    contador += 1
    elif opcion == "2":
        busqueda = input("ingresa el nombre del producto que buscas: ")
        if len(carrito) == 0:
            print("No hay elementos en su carrito")
        else:
            for i in carrito:
                total =0
                if busqueda.lower() == i.get("nombre").lower():
                    total = i.get("cantidad") * i.get("precio")
                    print(f"""
                        El producto {i.get("nombre")} se encuentra en tu inventario
                        hay {i.get("cantidad")}, con un precio unitario de {i.get("precio")} 
                        para un total de: {total}
                        """)
                else:
                    print(f"No se encontro el producto: {busqueda}. Intente agregarlo o escribirlo correctamente.")
    elif opcion == "3":
        nombre = input("ingrese nombre del producto: ")
        if len(carrito) == 0:
            print("No hay elementos en su carrito")
        else:
            for i in carrito:
                if nombre.lower() == i.get("nombre").lower():
                    update()
                    break
                else:
                    print("No hay productos con ese nombre")
    elif opcion == "4":
        nombre = input("ingrese nombre del producto: ")
        contador = 0
        if len(carrito) == 0:
            print("No hay elementos en su carrito")
        else:
            for i in carrito:
                if nombre.lower() == i.get("nombre").lower():
                    carrito.pop(contador)
                    break
                else:
                    contador += 1
                    if contador == len(carrito):
                        print(f"No se encontro el producto: {nombre}. Intente escribirlo correctamente.")
    elif opcion == "5":
        total = 0
        if len(carrito) == 0:
            print("No hay elementos en su carrito")
        else:
            for i in carrito:
                total += (lambda cantidad, precio: cantidad * precio)(i.get("cantidad"), i.get("precio"))
            print(f"El total del carrito es: {total}")
    elif opcion == "6":
        break
    else:
        print("Opcion no valida, ingrese un numero del menu de opciones")