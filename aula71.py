'''
Higher order functions
funções de primeira classe
'''

def saudacao(msg, nome):
    return f'{msg}, {nome}!'

def executa(funcao, *args):
    return funcao(*args)

a = executa(saudacao, 'Boa tarde', 'Thiago',)
print(a)
