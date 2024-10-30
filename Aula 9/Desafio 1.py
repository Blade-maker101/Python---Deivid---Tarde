x = int(input('Digite um número: '))
num = 0
if x == 0:
    print('O número não pode ser zero')
else:
    while x != 1:
        num += 1
        if x % 2 == 0:
            x = x / 2
            print(x)
        else:
            x = x * 3 + 1
            print(x)
    print('Etapas: ', num)
