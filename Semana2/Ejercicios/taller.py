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