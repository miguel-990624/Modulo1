arr = ["hola ", "mundo", "mañana"]
count = 0
for i in arr:
    count = count + 1
print (count)

#remover un elemento de una lista si usar metodos
lista = [1, 2 , 3 , 4 , 5 , 5 , 6 , 5 , 7 , 8 , 5, 9, 5] 
n1 = 0
for i in lista:
    n3 = 0
    n2 = n1 + 1
    for z in lista:
        n3 += 1
    for x in lista:
        if 0 < n2 < n3:
            if lista[n1] == lista[n2]:
                lista.pop(n2)
                n3 -= 1
            else:
                n2 += 1
    n1 += 1
print(lista)