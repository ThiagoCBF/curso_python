# Manipulando chaves e valores em dicionários

pessoa = {}

chave = 'nome_completo'

pessoa[chave] = 'Thiago Ferreira'
pessoa['sobrenome'] = 'Barbosa'


print(pessoa[chave])
pessoa[chave] = 'Couto'

del pessoa['sobrenome']

print(pessoa)
print(pessoa[chave])

if pessoa.get('sobrenome') is None:
    print('Não existe')
else:
    print(pessoa['sobrenome'])