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

"""
Merge Sort:
"""

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    """Aqui se vuelve a llamar la funcion merge_sort, para dividir el arreglo en dos mitades otra vez, hasta que queden en un solo elemento"""
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])
    
    """Aqui se ejecuta la funcion merge, que es la encargada de unir los dos arreglos, lo que pasa es que cada que arriba se llama la funcion merge_sort
    se va a ir dividiendo el arreglo en dos mitades, y cuando ya no haya mas mitades, se va a empezar a unir los arreglos
    de a pares, hasta que se vuelva a unir todo el arreglo
    Como en magic, cada uno de los merge_sort entran al stack pero abajo hay otro triger de merge, cuando ya no se pueden subdividir mas,
    se inician a resolver todos los merge que quedaron en el stack, si se dividio 3 veces, se van a resolver 3 triggers de merge, hasta
    limpiar el stack y que quede el arreglo ordenado"""
    return merge(left_half, right_half)

def merge(left, right):
    result = []
    i = j = 0
    # Merge the two sorted lists
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    # Add remaining elements
    result.extend(left[i:])
    result.extend(right[j:])
    return result

""""""
