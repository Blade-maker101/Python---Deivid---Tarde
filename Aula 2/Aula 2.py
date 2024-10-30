print('Meu nome é', 'Python.', end='\n')
print('Monty Python', '\n')
# end = ao final do print colocar o que está escrito nos parenteses
# o end também substitui a quebra de linha se caso o end não seja \n (o \n deve ser escrito no último '' de texto)

print('Meu', 'nome', 'é', 'Monty', 'Python')
print('Meu', 'nome', 'é', 'Monty', 'Python \n', sep='-')
# sep = usa o que está escrito em sep para separar cada palavra do print

print('Meu', 'nome', 'é', sep='-', end='*')
print('Meu', 'nome', 'é \n', sep='*', end='\n',)

print('Programação', 'Essenciais', 'em', sep='***', end='...')
print('Python')

print('     *      '*2)
print('    * *     '*2)
print('   *   *    '*2)
print('  *     *   '*2)
print(' *       *  '*2)
print('****   **** '*2)
print('   *   *    '*2)
print('   *   *    '*2)
print('   *****    '*2)

print('     *      ', '    * *     ', '   *   *    ', '  *     *   ', ' *       *  ',
      '****   **** ', '   *   *    ', '   *   *    ', '   *****    \n', sep='\n')

print('Eu gosto de Pyhton')
print('Eu gosto de "Python"')
print("Eu gosto de 'Python'\n")

print("\"Eu sou\"")
print('""Aprendiz de""')
print('"""Python"""\n')

print(0b1110101)  # binário
print(0o123)  # octodecimal/octal
print(0x123, '\n')  # hexadecimal

print(True > False)  # true = 1 e false = 0
print(True < False, '\n')
print(3e5)  # aqui os números etão sendo elevados em notação cientifíca (no caso 3*10^5)
print(3e-04)
# Inteiros (int) = só aceitam números inteiros
# Flutuantes (float) = contém partes decimais ou fracionárias
