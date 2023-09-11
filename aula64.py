'''
Def em python
Def - Funções personalizadas para ajudar na replicação de comandos
Retorna None
'''

def imprimir(a, b, c):
    print(a, b, c)

imprimir(1, 2, 3)
imprimir(4, 5, 6)

def saudacao(nome='Sem nome'):
    print(f'Olá, {nome}!')

saudacao('Thiago')
saudacao('Cristiano')
saudacao()