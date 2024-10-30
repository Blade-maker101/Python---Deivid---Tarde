ano = int(input('Digite o ano: '))
tipo = ano % 4
if ano < 1582:
    print('Fora do calendário gregoriano')
elif tipo == 0:
    print('Ano bissexto')
else:
    print('Ano comum')
    