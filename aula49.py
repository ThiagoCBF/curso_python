'''
Lista em Python

append - Adiciona um item ao final da lista
insert - Adiciona um item no índice escolhido
pop - Remove o ultimo item da lista ou do índice escolido
del ' Apaga um índice
clear - limpa a lista
extend - estende a lista

Create Read Update Delete
CRUD
'''

lista = [10, 20, 30, 40]
lista[2] = 300

del lista[2]
print(lista)
print(lista[2])

lista.append(50)
lista.pop()
lista.append(60)
print(lista)

lista.clear()
lista.insert(0, 'Thiago')
print(lista)


lista_a = [1, 2, 3]
lista_b = [4, 5, 6]
lista_c = lista_a + lista_b
lista_a.extend(lista_b)
print(lista_c)
print(lista_a)