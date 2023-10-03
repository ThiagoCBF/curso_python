'''
Métodos úteis dos dicionários em Python
Len - quantas chaves
Keys - iterável com as chaves
values - iterável com os valores 
items - iterável com chaves e valores
setdefault - adiciona valor se a chave não existe
copy - retorna uma cópia rasa (shallow copy)
get - obtém uma chave
pop - apaga um item com a chave especificada (del)
popitem - apaga o último item adicionado
update - atualiza um dicionário com outro
'''

p1 = {
    'nome': 'Thiago',
    'sobrenome': 'Ferreira',
}

print(p1.get('nome'))
print(p1['nome'])

nome = p1.pop('nome')
print(nome)
print(p1)

sobrenome = p1.popitem()
print(sobrenome)
print(p1)

p1.update({
    'nome': 'novo valor',
    'idade': 30,
})

p1.update(nome='novo valor', idade=30)

lista = [['nome', 'novo valor'], ['idade, 30']]
p1.update(lista)
print(p1)