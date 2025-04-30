"Invertir una lista:"
lista = [1, 2, 3, 4, 5]
lista2 =[]
count = 1
for x in lista:
    lista2.append(lista[-count])
    count+= 1
print(lista2)


"Eliminar los numero negativos"
lista = [3, -1, 5, -2, 7]
count = len(lista)
for x in range(len(lista)):
    if 0 <= x < count:
        if lista[x] < 0:
            lista.pop(x)
            count -=1
    else:
        break
print(lista)

"Encontrar la suma de los cuadrados"
lista = [1, 2, 3, 4]
acumulado = 0
for x in lista:
    acumulado = acumulado + (x**2)
print(acumulado)

"Duplicar los valores de una lista:"
lista2 =[]
for x in lista:
    lista2.append(x*2)
print(lista2)
