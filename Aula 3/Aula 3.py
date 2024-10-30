print(0.00000005)
print(50000000)
print(-0.000000018)

# operações matemáticas
print(2+2, '\n')  # + adição - são unários ou binários

print(2-2, '\n')  # - subtração

print(2 * 3)  # * multiplicação
print(2 * 3.)
print(2. * 3)
print(2. * 3., '\n')

print(6 / 3)  # / divisão
print(6 / 3.)
print(6. / 3)
print(6. / 3., '\n')

print(6 // 3)  # //divisão número inteiro (arredondamento)
print(6 // 3.)
print(6. // 3)
print(6. // 3., '\n')

print(6 // 4)  # arredonda para o menor número
print(6. // 4)
print(3.8 / 2)
print(3.8 // 2)
print(2.4 / 2)
print(2.4 // 2, '\n')

print(-6 / 4)
print(-6 // 4)  # arredonda para -2 pois arredonda para baixo
print(11 / 3)
print(11 // 3, '\n')

print(14 % 4)  # % resto (módulo) - 14/4 = 3, resta 2
print(12 % 4.5, '\n')

print(2 ** 3)  # ** exponenciação
print(2 ** 3.)
print(2. ** 3)
print(2. ** 3., '\n')

print(+2)  # unário
print(-4 + 4)  # binário
print(-4. + 8, '\n')  # binário

# hierarquia de prioridades:
# 1° **
# 2° + - (unário)
# 3° * / // %
# 4° + - (binário)
# 5° < <= > >=
# 6° == !=

print(2 + 3 * 5, '\n')

print(9 % 6 % 2, '\n')

# o python faz o 2**3 e depois ele faz o valor que sai disso (8) e depois eleva o 2^8
print(2 ** 2 ** 3, '\n')

print(-3 ** 2)  # parênteses
print((-3) ** 2)
# o número é uma entidade separada do "-" o que o faz voltar no fim do cálculo
print(-2 ** 3)
print((-2) ** 3)
print(-(3 ** 2), '\n')

print((5 * ((25 % 13) + 100) / (2 * 13)) // 2, '\n')

print((2 ** 4), (2 * 4.), (2 * 4))
print((-2 / 4), (2 / 4), (2 // 4), (-2 // 4))
print((2 % -4), (2 % 4), (2 ** 3 ** 2), '\n')

# variáveis:
# armazenam valores na memória
# o conteúdo pode ser modificado
# toda variável possuí um nome e um valor
# nome da variáveis

# nome das variáveis:
# pode ser composto de letras maiúsculas e minúsculas, números e caracteres
# deve começar com uma letra (sublinhado é considerado letra)
