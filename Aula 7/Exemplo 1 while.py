maiornum = -99999999999

num = int(input('Digite um número ou -1 para sair: '))

while num != -1:
    if num > maiornum:
        maiornum = num
    num = int(input('Digite um número ou -1 para sair: '))

print('O maior número digitado foi', maiornum)