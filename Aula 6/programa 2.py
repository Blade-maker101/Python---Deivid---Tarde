a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))
c = int(input('Digite o terceiro número: '))
if a == b and a == c:
    maiornumero = a, print('Os números são iguais')
elif a > b and a > c:
    maiornumero = a, print('O maior número é: ', a)
elif b > a and b > c:
    maiornumero = b, print('O maior número é: ', b)
else:
    maiornumero = c
    print('O maior número é: ', c)
    