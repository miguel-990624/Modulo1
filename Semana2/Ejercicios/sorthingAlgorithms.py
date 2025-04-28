"""
Bubble Sort:

Va a revisar elemento por elemento de la lista que le entregue, entonces va a tomar el primer elemento y lo va a comparar con el siguiente,
cada vez haciendo la validacion con menos numeros, por que ya no necesito ir hasta el final si se que tengo un elemento mayor al final bien
organizado, si por obra y gracia del espiritu santo, el arreglo ya esta ordenado, entonces no va a hacer ningun cambio y se va a salir del ciclo.
"""
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr


"""
Selection Sort:

Este algoritmo inicia en la primera posicion y va a buscar el valor menor o mayor de la lista, dependiendo de lo que se desee, y lo va a llevar a
la primera posicion, disponible, luego repite el proceso buscando el siguiente valor desde la siguiente posicion del arreglo
"""

def selection_sort(arr):
    n = len(arr)
    for i in range (n):
        mindex = i
        for j in range (i + 1, n):
            if arr[j] < arr[mindex]:
                mindex = j
        arr[i], arr[mindex] = arr[mindex], arr[i]
    return arr

"""
Insertion Sort:

Este algoritmo toma una lista e inicia a comparar el elemento  x con el x-1 => [x-1, x], si x es menor que x-1, entonces va a cambiar posicion, para 
que ahora el arreglo se vea asi [x, x-1], leugo lo hace con el siguiente elemento iniciando en donde esta ahora x -1, de modo que se veria asi el arreglo
[x, x -1 , x+1], inciamos desde x-1, miramos si x+1 es menor que x-1, si lo es, entonces cambiamos posicion, luego cuando estamos en [x, x+1, x-1],
miramos si x+1 es menor que x, si lo es, entonces cambiamos posicion, para quedar con el arreglo ordenado [x+1, x, x-1], y asi sucesivamente 
hasta que el arreglo quede ordenado.
"""

def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

