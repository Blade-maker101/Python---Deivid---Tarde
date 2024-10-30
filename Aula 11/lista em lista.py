lista1=[1]
lista2=lista1
lista1[0]=2
print(lista2)

lista1=[1]
lista2=lista1[:]
lista1[0] = 2
print(lista2)

lista3=[10,8,6,2,4]
novalista=lista3[1:3]
print(novalista)

lista3=[10,8,6,2,4]
novalista=lista3[1:-1]
print(novalista)

lista3=[10,8,6,2,4]
novalista=lista3[-1:1]
print(novalista)

lista3=[10,8,6,2,4]
novalista=lista3[:3]
print(novalista)

lista3=[10,8,6,2,4]
novalista=lista3[3:]
print(novalista)

lista3=[10,8,6,2,4]
novalista=lista3[:]
print(novalista)

lista3=[10,8,6,2,4]
novalista=lista3[1:3]
print(novalista)

lista3=[10,8,6,2,4]
del lista3[1:3]
print(lista3)

lista3=[10,8,6,2,4]
del lista3[:]
print(lista3)

lista3 = [0,3,12,8,2]
print(5 in lista3)
print(5 not in lista3)
print(12 in lista3)

lista3 = [7,3,11,5,1,9,7,15,13]
maior = lista3[0]
for i in range(1,len(lista3)):
    if lista3[i] > maior:
        maior = lista3[i]
print(maior)

lista3 = [1,2,3,4,5,6,7,8,9,10]
encontrar = 5
finalizado = False
for i in lista3:
    finalizado = lista3[i] == encontrar
    if finalizado:
        break

if finalizado:
    print('Elemento encontrado no índice: ', i)
else:
    print('Elemento não encontrado')

resultado = [5,11,9,42,3,49]
aposta = [3,7,11,42,34,49]
acertos = 0

for i in aposta:
    if i in resultado:
        acertos += 1
print('você acertou:', acertos, 'números')

lista = []
var = 2

for i in range(8):
    lista.append(var)
print(lista)

var = 2
lista = [var for i in range(8)]
print(lista)

quadrados = [x**2 for x in range(10)]
print(quadrados)

potenciacao = [2**i for i in range(8)]
print(potenciacao)

lista = [1,2,3,4,5,6,7,8,9]
impar = [x for x in lista if x%2 !=0]
print(impar)