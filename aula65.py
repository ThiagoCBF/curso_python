'''
Argumentos nomeados e não nomeados em funções Python 
Argummento nomeado tem nome com sinal de igual
Agurmento não nomeado recebe apenas o argumentoo(valor)
'''

def soma(x, y, z):
    print(f'{x=} + y={y} + {z=}' , x + y + z )

# Argumento Não Nomeado
soma(1, 2, 3)

# Argumento Nomeado
soma(y=2, z=3, x=1)


print(1, 2, 3, sep='-')