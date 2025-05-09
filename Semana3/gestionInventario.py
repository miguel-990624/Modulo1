"""
Explanation: (in eng since you said to only code like that from now on)

So i created a constructor method Producto, this will allowme to instantiate and pass inner functions to the
product i create, to avoid having to update the info by overriding like this i[name][0], which does not seem
very organized to me, so i have set up the functions that let me get the data i need with either a get or 
override one of the values directly without having to update the whole array that i am passing as values. 
"""
class Producto:
    def __init__(self, name, data):
        self.name = name
        self.data = data

    def get(self, key):
        if key == "nombre":
            return self.name
        elif key == "cantidad":
            return self.data[0]
        elif key == "precio":
            return self.data[1]
    
    def set (self, key, value):
        if key == "cantidad":
            self.data = (value, self.data[1])
        elif key == "precio":
            self.data = (self.data[0], value) 
"""
I added the function add which is letting me create a new instance of Producto with the data that is being 
requested, name, price, quantity. I pass them as the arguments to the constructor and then it is appended 
to the cart array.
"""
def add ():
    precio = input("ingrese el valor por unidad del producto: ")
    if precio.replace(".", "", 1).replace(" ","").isdigit():
        precio = float(precio.replace(" ",""))
        cantidad = input("ingrese la cantidad de productos que desea llevar: ")
        if cantidad.count(".") == 0 and cantidad.replace(" ","").isdigit():
            cantidad = int(cantidad.replace(" ",""))
            producto = Producto(nombre,(cantidad,precio))
            carrito.append(producto)
        else:
            print("El dato ingresado no es un valor valido, intente de nuevo")
    else:
        print("El dato ingresado no es un valor valido, intente de nuevo")

"""
update function was created to modify the amount the product currently has, it verifies outside the function
that the value that is being updated exist actually, then it calls the function, which will add a positive 
value to the current amount, using the method passed by the constructor get, to add to what the user types
and then using the set method without updating price i override the quantity
"""

def update ():
    print("Este producto ya se encuentra en su carrito")
    cantidad = input(f"ingrese la cantidad de productos adicionar, cuenta actual {i.get("cantidad")}: ")
    if cantidad.count(".") == 0 and cantidad.replace(" ","").isdigit():
        cantidad = int(cantidad.replace(" ",""))
        cantidad += i.get("cantidad")
        i.set("cantidad",cantidad)
        print(f"la cantidad fue correctamente actualizada, cantidad actual: {i.get("cantidad")}")
    else:
        print("El dato ingresado no es un valor valido, intente de nuevo")

"""
While for menu handling, while tru it loops infinitely 
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
        nombre = input("Ingrese nombre del producto: ")
        """
        the first item is added if its empty, then if the cart is no longer empty, based on what the
        user types, if it's already a name on the cart array, the customer will be asked if they want to 
        update instead
        """
        if len(carrito) == 0:
            add()
            
        else:
            product_found = False
            for i in carrito:
                if nombre.lower() == i.get("nombre").lower():
                    ans = input("Producto ya en el carrito, quiere cambiar la cantidad? S / N \n")
                    if ans.lower() == "s":
                        update() 
                        product_found = True
                        break
                    elif ans.lower() == "n":
                        break
                    else:
                        print("Respuesta invalida")
                        break
            if not product_found:
                add()
    elif opcion == "2":
        """
        will verify from now on the cart is not empty before continuing, then we will be allowed to continue.
        this will look in the array for a name matching to get the info on the product we are looking for
        """
        if len(carrito) == 0:
            print("No hay elementos en su carrito")
        else:
            busqueda = input("ingresa el nombre del producto que buscas: ")
            for i in carrito:
                total =0
                if busqueda.lower() == i.get("nombre").lower():
                    total = i.get("precio") * i.get("cantidad")
                    print(f"""
                        El producto {busqueda} se encuentra en tu inventario
                        hay {i.get("cantidad")}, con un precio unitario de {i.get("precio")} 
                        para un total de: {total}
                        """)
                    break
                else:
                    print(f"No se encontro el producto: {busqueda}. Intente agregarlo o escribirlo correctamente.")
    elif opcion == "3":
        """
        directly update function
        """
        if len(carrito) == 0:
            print("No hay elementos en su carrito")
        else:
            nombre = input("ingrese nombre del producto: ")
            for i in carrito:
                if busqueda.lower() == i.get("nombre").lower():
                    update()
                    break
                else:
                    print("No hay productos con ese nombre")
    elif opcion == "4":
        """
        will look for a name matching in the array and then it will remove it from the cart if it matches a name that
        exists within the array
        """       
        if len(carrito) == 0:
            print("No hay elementos en su carrito")
        else:
            nombre = input("ingrese nombre del producto: ")
            contador = 0
            for i in carrito:
                if busqueda.lower() == i.get("nombre").lower():
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
            """
            This was a trickier solution, it was done when asking chat to do it on one line, the way it works is that 
            first we will call the sum function, it will add all values within an array and give a result, then we pass 
            as parameter the cart array, wich will be mapped over, the map function will go over a iterable value such as
            the cart and it will return another array in that case, for example if the object has over 10 elements, i could
            return an array with the values i require, in this case the values i need to be returned for the array that will be
            added using the sum function are the product of the quantity and price of each product i have in the cart.

            so if i have this [{"x":[2,10]},{"y":[5,5]}] 
            i will map over doing what is inside the lambda function
            we will be left with this sum([20,25])
            it will add what is inside the array that was returned and then we will be given the result
            total = 45
            """
            total= sum(map(lambda i: i.get("cantidad") * i.get("precio"), carrito))
            print(f"El total del carrito es: {total}")
    elif opcion == "6":
        """
        Break to exit
        """
        break
    else:
        """
        If user cannot type an option correctly
        """
        print("Opcion no valida, ingrese un numero del menu de opciones")