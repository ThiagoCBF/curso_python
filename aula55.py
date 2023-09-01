'''
enumerate - enumera iteráveis (índice)
'''
lista = ['Thiago', 'Ferreira', 'Couto']
lista.append('Barbosa')



for indice, nome in enumerate(lista):
    print(indice, nome)

for item in enumerate(lista):
    indice, nome = item
    print(indice, nome)

for tupla_enumerda in enumerate(lista):
    print('For da tupla:')
    for valor in tupla_enumerda:
        print(f'\t{valor}')