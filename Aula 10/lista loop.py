minhalista = []

for ia in range(5):
    minhalista.append(ia+1)

print(minhalista)

minhalista2 = []

for ib in range(5):
    minhalista2.insert(0, ib+1)

print(minhalista2)

minhalista3 = [10,1,8,3,5]

total = 0

for ic in range(len(minhalista3)):
    total += minhalista3[ic]

print(total)

minhalista4 = ['Branco', 'Roxo', 'Azul', 'Amarelo', 'Verde']

for cores in minhalista4:
    print(cores)

print(minhalista4)

minhalista5 = [10,1,8,3,5]

minhalista5[0],minhalista5[4] = minhalista5[4],minhalista5[0]
minhalista5[1],minhalista5[3] = minhalista5[3],minhalista5[1]

print(minhalista5)