'''
split / join - List e string
split - divide uma string
join - une string

'''

frase = 'frase genérica, para teste'
lista_frases_cruas = frase.split(',')

lista_frases = []

for i, frase in enumerate(lista_frases_cruas):
    lista_frases.append(lista_frases_cruas[i].strip()) #lstrip , rstrip

print(lista_frases)

frases_unidas = '----'.join(lista_frases)
print(frases_unidas)