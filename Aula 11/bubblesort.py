lista = [8,10,6,2,4]
troca = True

while troca:
    troca = False  
    for i in range(len(lista)-1):
        if lista[i] > lista[i+1]:
            troca = True
            lista[i], lista[i+1] = lista[i+1], lista[i]
        
print(lista)

lista2 = [8,10,6,2,4]
lista2.sort()
print(lista2)

lista3 = [8,10,6,2,4]
lista3.reverse()
print(lista3)

lista4 = [8,10,6,2,4]
x = sorted(lista4, reverse=True)
print(x)