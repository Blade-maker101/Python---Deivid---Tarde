temp = [[0.0 for i in range(24)] for j in range(31)]
for i in range(31):
    temp[i][12]=33.3
for linha in temp:
    print(linha)

total = 0.0
for dias in temp:
    total +=dias[12]
print(total)
media = total//31
print("Temperatura média mensal ao meio dia: ", media)

diasquentes = 0
for dias in temp:
    if dias [12] > 20.0:
        diasquentes +=1
print(diasquentes, "dias estavam quentes")