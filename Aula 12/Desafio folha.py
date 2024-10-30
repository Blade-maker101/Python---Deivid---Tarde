vehicles_one = ['carro', 'bicicleta', 'motor']
print(vehicles_one)
vehicles_two = vehicles_one
del vehicles_one[0]
print(vehicles_two)

cores = ['vermelho', 'verde', 'laranja']
parte1 = cores[:]
print(parte1)
parte2 = cores [0:2]
print(parte2)

lista = ['A', 'B', 'C', 'D', 'E']
novalista=lista[2:-1]
print(novalista)

minhalista = [1,2,3,4,5]
sliceone = minhalista[2: ]
slicetwo = minhalista[ :2]
slicethree = minhalista [-2: ]
print(sliceone)
print(slicetwo)
print(slicethree)

minhalista = [1,2,3,4,5]
del minhalista[0:2]
print(minhalista)
del minhalista[:]
print(minhalista)

minhalista = ['A','B',1,2]
print('A' in minhalista)
print('C' not in minhalista)
print( 2 not in minhalista)

lista1=['A','B','C']
lista2=lista1
lista3=lista2
del lista1[0]
del lista2[0]
print(lista3)

lista1=['A','B','C']
lista2=lista1
lista3=lista2
del lista1[0]
del lista2
print(lista3)

lista1=['A','B','C']
lista2=lista1
lista3=lista2
del lista1[0]
del lista2[:]
print(lista3)

lista1=['A','B','C']
lista2=lista1[:]
lista3=lista2[:]
del lista1[0]
del lista2[0]
print(lista3)

minhalista = [1,2,'in', True, 'ABC']
print(1 in minhalista)
print('A' not in minhalista)
print(3 not in minhalista)
print(False in minhalista)
