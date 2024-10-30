P1= float(input('Digite a nota da P1: '))
P2= float(input('Digite a nota da P2: '))
notafinal = ((P1 + P2)/2)

if notafinal >= 6:
    print('Sua média é', notafinal, 'parabéns você está aprovado!') 
elif notafinal <= 3:
    print('Sua média é', notafinal, 'você está reprovado!')
else:
    print('Sua média é', notafinal, 'você está de recuperação!')
