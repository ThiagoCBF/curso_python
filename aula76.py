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

pessoa = {
    'nome': 'Thiago',
    'sobrenome': 'Ferreira' 
}
print(len(pessoa))
print(list(pessoa.keys()))
print(list(pessoa.values()))
print(list(pessoa.items()))

pessoa.setdefault('idade', 0)
print(pessoa['idade'])