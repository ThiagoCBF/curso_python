'''
Closure e funções que retornam outras funções
'''

def criar_saudacao(saudacao):
    def saudar(nome):
        return f'{saudacao}, {nome}!'
    return saudar

b = criar_saudacao('Boa dia')
a = criar_saudacao('Boa tarde')
print(b('Thiago'))
print(a('Thiago'))
