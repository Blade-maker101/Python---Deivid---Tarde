media = float(0)
totaldeprovas = int(input('Digite quantas provas: '))

for i in range(totaldeprovas):
    print('Digite a nota da prova', i + 1, ':', end='')
    nota = float(input())
    media += nota

total = media / (i + 1)
print('Sua média é', round(total))
