def adicao(a,b,c):
    print(a,'+',b,'+',c,'=',a+b+c)
adicao(1,2,3)
adicao(c=1,a=2,b=3)
adicao(3,c=1,b=2)

def nomecompleto(nome,sobrenome = 'Silva'):
    print('Olá, meu nome é', nome, sobrenome)
nomecompleto('Jair','Souza')
nomecompleto('Sandra')
nomecompleto(nome = 'Roger')

def nomecompleto2(nome = 'Maria',sobrenome = 'Silva'):
    print('Olá, meu nome é', nome, sobrenome)
nomecompleto2()
nomecompleto2('Joelma')
nomecompleto2(nome = 'Igor')
nomecompleto2(sobrenome = 'Martins')
nomecompleto2('Sandro', 'Teodoro')
