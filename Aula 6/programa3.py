a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))
c = int(input('Digite o terceiro número: '))

maiornumero = a

if b > maiornumero:
    maiornumero = b

if c > maiornumero:
    maiornumero = c

print('O maior número digitado foi', maiornumero)