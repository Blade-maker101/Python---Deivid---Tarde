quartos = [[[False for r in range(20)] for f in range(15)] for t in range(3)] #21 quartos, 16 andares, 4 predios
quartos[1][9][13] = True # predio 2, andar 10, quarto 14
quartos[0][0][0] = True # predio 1, andar 1, quarto 1
quartos[2][14][19] = True # predio 3, andar 15, quarto 20
print(quartos)