var = float(input('Digite um número: ')) # o primeiro if ou elif que for ativo vai parar o run e ativar o seu print
if var <= 10:
    print('Seu número é menor ou igual a 10')
elif var <= 20:
    print('Seu número é maior que 10 e menor ou igual a 20')
elif var <= 40:
    print('Seu número é maior que 20 e menor ou igual a 40')
elif var <= 60:
    print('Seu número é maior que 40 e menor ou igual a 60')
elif var <= 80:
    print('Seu número é maior que 60 e menor ou igual a 80')
else:
    print('Seu número é maior que 80')