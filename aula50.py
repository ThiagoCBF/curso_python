'''
Cuidados com dados mutáveis
'''

lista_a = ['Thiago', 'Ana']
lista_b = lista_a.copy()

lista_a[0] = 'AAAAA'
print(lista_b)
print(lista_a)