"""
1. ¿Qué es un array o lista en Python?

Un array o una lista en Python es una manera de guardar varios datos dentro de una sola variable, de modo que se puede iterar sobre datos
para buscar y guardar informancion de manera mas eficiente.

    ¿Cómo se declara una lista vacía?

    para declarar una lista vacia hay que escrbir el nombre de la variabale, luego = para asignar el valor y se cierra con [] que indica que es
    un array, se veria de esta manera: lista = []


    ¿Cómo se crea una lista con valores iniciales?
    Para crear una lista con valores predeterminados, se haria lo mismo que para declarar un arreglo vacio, pero en lugar de dejarlo cerrado con
    los corchetes, dentro de estos se ponen valores separados por comas, especificando el tipo de dato que se va a guardar, por ejemplo:
"""

lista = [1, 2, 3, 4, 5]
lista2 = ["a", "b", "c", "d", "e"]

"""
2. ¿Cómo accedemos a los elementos de una lista?
Para acceder al elemento x de una lista, vamos a escribir el nombre del arreglo "lista" y como es una lista podemos acceder al indice del elemento
que necesitamos con los corchetes para indicar que es un arreglo y busco una posicion especifica. Por ejemplo tengo lista = [1, 2, 3, 4, 5], los indices
de este arreglo inician en 0, visto de otra manera, lista[0] = 1, lista[1] = 2, lista[2] = 3, lista[3] = 4, lista[4] = 5, cada elemento guarda un indice
que me permite acceder e iterar

    ¿Qué significa usar un índice negativo?
    Al usar el indice de manera negativa, inicio el conteo desde atras hasta adelante, como en el ejemplo anterior que tenia lista = [1, 2, 3, 4, 5],
    lista[-1] = 5, lista[-2] = 4, lista[-3] = 3, lista[-4] = 2, lista[-5] = 1, de esta manera puedo acceder a los elementos desde el final hacia el inicio
    ¿Qué pasa si intento acceder a un índice que no existe?
    Si intento acceder a un indice que no existe, entonces el programa lanza un error de tipo IndexError, indicando que el indice no existe
"""
print(lista[0])
print(lista[-1])

"""    
3. ¿Qué es el "slicing" o rebanado de listas?
El slicing o rebanado de listas es una manera de acceder a un rango de elementos dentro de una lista, por ejemplo, si tengo la lista = [1, 2, 3, 4, 5]
y quiero acceder a los elementos en la posicion x hasta z, voy a partir los indices de esta manera lista[x:z] x es desde el indice que inicio, los separo con ":" 
z es el indice al que quiero llegar, pero es de considerar que z no se va a incluir, entonces quiero el numero 2 al 4, pues mi indice rebanado seria
lista[1:4] = [2, 3, 4], si dejo uno de los indices vacio, voy a ir desde el elemento inicial hasta el z-1 o desde el x hasta el final, por ejemplo
lista[1:] = [2, 3, 4, 5], si quiero desde el inicio hasta el 4-1, entonces seria lista[:4] = [1, 2, 3, 4]
    ¿Cómo se obtiene una sublista usando slicing?
    Para obtener una sublista usando slicing, se hace de la manera que ya explique, con los dos indices separados por ":" y el resultado es una lista
    sublista = lista[x:z], donde x es el indice inicial y z es el indice final, pero no se incluye
"""
sublista = lista[1:4]
print(lista[1:4])
print(lista[1:])
print(sublista)

"""
4. ¿Cómo modificamos los elementos de una lista?
Para modificiar los elementos de una lista se debe acceder al elemento de la posicion que quiero modificar, y asignarle un nuevo valor, por ejemplo
para cambiar mi lista en el indice 2, primero accedo lista[2] y luego sobreescribo el valor, lista [2] = 10, ahora mi lista es [1, 2, 10, 4, 5]
    ¿Qué pasa si intento modificar un índice que no existe?
    Si intento modificar un indice que no existe, entonces el programa lanza un error de tipo IndexError, indicando que el indice no existe

"""
lista[2] = 10
print(lista)

"""
5. ¿Cómo agregamos nuevos elementos a una lista?
Hay varios metodos para agregar nuevos elementos a una lista, el primero es append, que agrega un nuevo elemento al final de la lista, de modo que 
si tengo mi lista lista=[1, 2, 10, 4, 5] y hago lista.append(10), mi lista ahora es [1, 2, 3, 4, 5, 10], por que append agrega el elemento al final
y extiende la lista en uno. El segundo es insert, que agrega un nuevo elemento en la posicion que yo quiera, sin embargo no sobreescribe el codigo
sino que lo mueve a la derecha desde donde inserto el elemento, por ejemplo mi lista lista = [1, 2, 10, 4, 5, 10] y le inserto un 10 en la posicion 2
lista.insert(2, 10), mi lista ahora es [1, 2, 10, 10, 4, 5, 10], si me salgo de los limites de la lista, con un indice mayor, se va a agregar al final.
el elemento que estaba en la posicion 2 se movio a la posicion 3 y el que estaba en la
El tercero es extend, que agrega varios elementos a la lista por ejemplo, tengo mi lista lista [1, 2, 10, 10, 4, 5, 10] y le hago lista.extend([10, 20, 30])
mi lista ahora es [1, 2, 10, 10, 4, 5, 10, 10, 20, 30], extend agrega los elementos al final de la lista y la extiende en el tamaño de los elementos que le pase

"""

lista.append(10)
print(lista)
lista.insert(2, 10)
print(lista)
lista.extend([10, 20, 30])
print(lista)

"""
6. ¿Cómo eliminamos elementos de una lista?
Hay varias maneras de eliminar elementos de una lista, la primera es pop, que elimina el elemento en la posicion que yo quiera, por ejemplo
mi lista lista = [1, 2, 10, 10, 4, 5, 10, 10, 20, 30] y hago lista.pop(2), mi lista ahora es [1, 2, 10, 4, 5, 10, 10, 20, 30], el elemento que estaba en la 
posicion 2 se elimino, tambien si no le paso parametro elimina el ultimo elemento de la lista. El siguiente metodo para remover elementos de una lista es 
el metodo remove, que me remueve el primer match que le hagacon el valor que yo necesite lista = [1, 2, 10, 4, 5, 10, 10, 20, 30], si aplico remove seria 
lista.remove(10), y quedaria con un arreglo asi lista = [1, 2, 4, 5, 10, 10, 20, 30]. Ahora el metodo del, que me elimina un valor en un indice,
por ejemplo en mi arreglo lista =[1, 2, 4, 5, 10, 10, 20, 30] si uso el metodo del tendria algo asi del lista[5] => [1, 2, 4, 5, 10, 20, 30] o si 
se pasa vacio borra el arreglo del lista. El metodo clear borra completamente el contenido del arreglo y me entrega un arreglo vacio, clear lista => [].
El ultimo metodo seria que eliminacion usando slicing para sobreescribir el arreglo, me permitiria borrar de el indice x hasta el indice z-1, por ejemplo 
con el arreglo lista = [1, 2, 4, 5, 10, 20, 30], puedo hacer lista[5:]=[] y borra todos los elementos despues del indice 5, dejandome una arreglo asi
lista = [1, 2, 4, 5, 10].

"""
lista.pop(2)
print(lista)
lista.remove(10)
print(lista)
del lista[5]
print(lista)
lista[5:]=[]
print(lista)

"""
7. ¿Cómo buscamos elementos dentro de una lista?
Para verificar si hay un elemento dentro de una lista usariamos el metodo in, que regresa un valor booleano como metodo de confirmacion, retomando el 
arreglo, usariamos lista = [1, 2, 4, 5, 10], para verificar si el numero 10 esta presente podemos usar el metodo in en un print que nos verifica si esta o no
print(10 in lista), nos deberia retornar un valor verdadero. Otro metodo para saber donde se encuentra un elemento en el arreglo es el metodo index, que nos
dira el primer indice donde se encuentre ese elemento, print(lista.index(10)) que nos deberia decir que se encuentra en la posicion 4 de nuestro arreglo.
El metodo count, nos dice cuantas veces esta un elemento en el arreglo, por ejemplo en el arreglo lista=[1, 2, 4, 5, 10] si queremos ver cuantas veces se
repite el numero 10 hariamos un print(lista.count(10)) y debe retornar 1 
 
"""
print(10 in lista)
print(lista.index(10))
print(lista.count(10))

"""
8. ¿Cómo ordenamos los elementos de una lista?

Para ordenar un arreglo, hay metodos que agilizan el proceso, el primero de ellos es sort que nos va a cambiar la lista que usemos para que se vea 
arreglada de menor a mayor valor, nuestro arreglo lista ya esta ordenado asi pero haciendolo quedariamos con lista.sort() => [1, 2, 4, 5, 10], para
ordenarlos de arriba a abajo seria ingresando el argumento reverse=True dentro del metodo .sort, asi lista.sort(reverse.True) => [10, 5, 4, 2, 1] con
esto cambiamos el arreglo original y ahora esta en orden descendente. El segundo metodo seria .sorted, que nos va a sobreescribir el arreglo en un
nuevo array con esto vamos a qudar con un segundo array sin modificar directamente el principal, lista3 = lista.sorted(), y al igual que con el
sort acepta el argumento reverse=True. Adicional a esto el argumento key permite poner parametros personalizados, para ordenar segun el criterio que
se necesite
"""
lista3 = [40, 10, 30, 20]
lista4 = lista3.sorted()
print(lista4)
lista4 = lista3.sorted(reverse=True)
print(lista4)


"""
9. ¿Cómo invertimos el orden de los elementos de una lista?
Para invertir un arreglo podemos usar el metodo reverse, que nos va a modificar la lista y nos va a retornar la misma lista pero en este caso invertido
lista.reverse() => [10, 5, 4, 2 , 1]. Otra manera posible de hacerlo seria sin modificar la lista actual usando slicing para en un nuevo arreglo
asignar los valores invertidos, lista2 = lista[::-1]. ::-1 significa desde el inicio hasta hasta el final recorramelos hacia atras, esto deberia entregar
un resultado asi lista2 = [1, 2, 4, 5, 10]
"""

lista3 = [10, 20, 30, 40]
lista4 = lista3[::-1]
print(lista4)
lista3.reverse()
print(lista3)

"""
10. ¿Cómo hacemos una copia de una lista?
Para hacer una copia de un arreglo, debemos guardar los valores del arreglo original en un nuevo arreglo, el primero metodo seria usar el metodo
copy lista2 = lista,copy() que nos va a entregar una lista 2 con todos los valores de la lista 1. El segundo metodo para copiar strings es recurriendo
nuevamente a hacer slicing, podemos asignar a un nuevo arreglo todos los elementos de lista desde inicio hasta el final, usando lista2 = lista[:].
El ultimo proceso que podriamos hacer es usar el constructor list() para declarar la nueva lista como una copia de la que nos interesa, haciendo entonces 
lista2 = list(lista)
"""

lista3 = [10, 20, 30]
lista4 = lista3.copy()
lista4 = lista3[:]
lista4 = list(lista3)

"""
11. ¿Cómo comprobamos si una lista está vacía?11. ¿Cómo comprobamos si una lista está vacía?

Para verificar si una lista esta vacia tenemos varias opciones, todas deben ser comparaciones, si tenemos el arreglo vacio podemos entonces hacer un if que lo
compare, if not(lista): deberia retornar verdad si la lista esta vacia por que la lista vacia equivale a booleano. if len(lista) == 0, nos permite ver
si el lenght de la lista es 0, lo que significa que no tiene elementos adentro, if lista == [], esto la compara con una lista vacia y si son iguales
retorna verdadero. Por ultimo el condicional if not any(lista): any nos retornaria falso por que no tiene valores, y con not retorna verdadero debido a 
que no tiene valores.
"""

mi_lista = []

if not mi_lista:
    print("La lista está vacía")
else:
    print("La lista no está vacía")

