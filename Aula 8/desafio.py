num1 = int(input('Digite o número inicial: '))
num2 = int(input('Digite o número final: '))
soma = 0

for total in range(num1, num2 +1):
    soma += total

print('A soma dos números de ', num1, 'a', num2, 'é', soma)
