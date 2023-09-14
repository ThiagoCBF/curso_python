'''
Dicionários em Python (tipo dict)
Dicionário = 'chave' + 'valor'
chave = índices (tipo imutáveis= str, int, float, bool, tuple )
valor = qualquer tipo
{} ou dict / criar dicionário 
'''

pessoa = dict(nome='Thiago Ferreira', sobrenome='Barbosa')

a = {
    'nome': 'Cristiano',
    'sobrenome': 'Ferreira',
    'idade': 19,
    'altura': 1.8,
    'endereços': [
        {'rua': 'xx', 'número': 14},
        {'rua': 'yy', 'número': 121}
    ]

}
print(a['nome'])
print(a['sobrenome'])

print()

for chave in a:
    print(chave,':', a[chave])