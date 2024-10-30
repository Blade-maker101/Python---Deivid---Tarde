def mensagem (dados, num):
    print('Seu', dados, 'é', num)
mensagem('Telefone', '99999999')
mensagem('RG', '4312351132')
mensagem('CPF', '131989840218')

def nomes(nome1,nome2):
    print('Olá', nome1)
    print('Olá', nome2)
nomes('Carlos', 'Ana')

def nomecompleto(nome,sobrenome):
    print('Olá, meu nome é', nome, sobrenome)
nomecompleto(nome = 'Luke', sobrenome = 'Skywalker')
nomecompleto(sobrenome = 'Skywalker',nome = 'Luke')


def endereco(rua, cidade, cep):
    print('Seu endereço é rua', rua, 'na cidade de', cidade, 'CEP', cep)

r = input('Rua: ')
c = input('Cidade: ')
cp = input('CEP: ')

endereco(r,c,cp)
