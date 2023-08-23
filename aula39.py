# Iterando strings com while

nome = 'Thiago Ferreira'
novo_nome = ''

indice = 0
while indice < len(nome):
    letra = nome[indice]
    novo_nome += f'*{letra}'
    indice += 1

print(novo_nome)