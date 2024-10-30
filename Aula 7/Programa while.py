print('+', 15 * '-', '+')
print('|', '  Bem vindo!!! ', '|')
print('|', 'Advinhe a senha', '|')
print('+', 15 * '-', '+')

numero = int(input('Digite a senha correta: '))
while numero != 777:
    print('Ha ha ha! Você está preso no loop!')
    numero = int(input('Digite a senha correta: '))
print('Muito bem! Esta livre agora!')
