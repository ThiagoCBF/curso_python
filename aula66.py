'''
Valores padrão para parâmetros
Caso o valor nao seja enviado para o parâmetro, o valor padrão será usado
'''

def soma(x, y, z=None):
    if z is not None:
        print(f'{x=} + {y=} + {z=}', x + y + z)
    else:
        print(f'{x=} + {y=}', x + y)

soma(1, 2)
soma(3, 5)
soma(7, 12)
soma(2, 2, 0)