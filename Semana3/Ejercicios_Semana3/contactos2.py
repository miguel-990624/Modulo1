"""
Ejercicio 1: Registro de Estudiantes
Objetivo:
Crear un diccionario para almacenar información sobre estudiantes y realizar algunas operaciones básicas como agregar, modificar y mostrar datos.

Instrucciones:
Crea un diccionario llamado estudiantes, donde las claves sean los nombres de los estudiantes y los valores sean otro diccionario con las claves edad y calificacion.

El programa debe permitir al usuario realizar las siguientes operaciones:

Agregar un nuevo estudiante (nombre, edad, calificación).
Modificar la calificación de un estudiante.
Mostrar la información de todos los estudiantes.
Eliminar un estudiante por su nombre.
"""
"""
class Estudiante:
    def __init__(self, data):
        self.data = data

    def get(self, key):
        return self.data.get(key)
    
    def set(self, key, value):
        self.data[key] = value
"""
"""
Agregar un usuario
"""

class Estudiante:
    def __init__(self, name, data):
        self.name = name
        self.data = data

    def get(self, key):
        return self.data.get(key)

    def set(self, key, value):

        self.data[key] = value

    def __str__(self):
        # Return a string representation for easier debugging and printing
        return f"{self.name}: {self.data}"

togle = lambda x: not x

clase = []

()
# control = True

# while control:
#     print("""
# --- Salon de Clases ---
          
#           """)
# # Accessing data:
for estudiante in clase:
    print(estudiante)
