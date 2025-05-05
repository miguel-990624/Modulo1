"""
Vamos a crear un contructor para poder instanciar mascotas durante el desarrollo del ejercicio, Este ejercicio pedia hacer 3 listas con Nombre, edad y si esta enfermo o no,
al ser un ejercicio facilmente resuelto con OOP, se decidio crear un arreglo de diccionarios u objetos, estos van a tener la funcion interna de set y get para editar 
los valores o llamarlos mas facilmente.
"""

class Mascota:
    """
    Primero pasamos los datos aqui al constructor para instaciar una nueva mascota
    """
    def __init__(self, data):
        self.data = data

    """
    Creamos una funcion get, que nos va a servir para pedir el valor de la propiedad que queremos, por decir algo si el objeto tiene nombre podemos pedir el nombre de
    ese obejto en particular
    """
    def get (self, key):
        return self.data.get(key)
    
    """
    Creamos una funcion set, que ahora nos va a decir que para la llave que necesitemos podemos cambiar el valor, por ejemplo si queremos cambiar el nombre, podemos ir
    directamente a la propiedad nombre y sobreescribirlo
    """
    def set (self, key, value):
        self.data[key] = value
def salir (x):
    return not x


def menu(opcion, control, arr):
    if opcion == 1:
        print("Ingrese los datos de su mascota: ")
        nombre = input("Nombre: ")
        edad = int(input("Edad: "))
        salud = input("Esta enfermo? Si o No: ")

        """
        Se le asignan los valores a propiedades dentro del objeto y se instancia datosMascota, luego se pasan datosMascota, como argumento del constructor para agregar
        al arreglo este nuevo objeto, para ir creciendo la lista de objetos.
        """
        datosMascota = {"nombre": nombre, "edad":edad, "salud":salud}
        mascota = Mascota(datosMascota)
        arr.append(mascota)
        print("Agregado correctamente")
    elif opcion == 2:
        if (len(arr) > 0):
            busqueda = input("Ingrese el nombre de la mascota que quiera remover del sistema: ")
            contador = 0
            for i in arr:
                
                """
                Como tenemos una funcion interna .get() podemos ir directamente a la propiedad "nombre" y nos va a retornar el valor que tiene ahi guardado dentro de 
                la propiedad. Ahora si encontramos que el valor ingresado coincide con el valor del arreglo en la posicion que esta, dentro de la propiedad nombre
                entonces saqueme del for y borreme ese valor.
                """
                if busqueda.lower() == i.get("nombre").lower():
                    break
                else:
                    contador += 1
            if(contador == len(arr)):
                print("no se encontro una mascota con ese nombre")
            else:
                arr.pop(contador)
                print(f"{busqueda} ha sido exitosamente removido")
        else:
            print("No hay datos en el sistema actualmente")
    elif opcion == 3:
        if (len(arr) > 0):
            contador = 1
            print("Lista de mascotas: ")
            for i in arr:
                print(f"{contador}. {i.get("nombre")}, tiene {i.get("edad")} y presenta enfermedad: {i.get("salud")}")
                contador += 1
        else:
            print("No hay datos en el sistema actualmente")
    elif opcion == 4:
        print("Cerrando operaciones")
    else:
        print("Opcion no valida")

listaMascotas = []
control = True
while control == True:
    opcion = int(input("""
                    Gestor de mascotas
                       Ingrese una opcion:
                        1. Añadir mascota al sistema
                        2. Remover mascota del sistema
                        3. Ver registro
                        4. Salir
                       """))
    menu(opcion, control, listaMascotas)
    
    if opcion == 4:
        control = salir(control)