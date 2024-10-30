# Operadores bit a bit
# & = and
# | = or
# ~ = not
# ^ = or exclusivo

x = 0
y = 22
print(x and y)

x = 15
y = 22
print(x and y)

x = 0b001111
y = 0b010110
print(x and y)

x = 0b001111
y = 0b010110
print(x & y)
# bit a bit = compara x e y e cria um novo binário a partir dele
# no caso: 000110