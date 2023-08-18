#Operadores In e Not In
#Strings são iteráveis
#  0 1 2 3 4 5 
#  T H I A G O
#  -6-5-4-3-2-1
#nome = 'Thiago'
#print(nome[-4])

#print('z' not in nome) # Nao esta em 
#print('a' in nome) # Esta no nome
#print('ago' in nome)

nome = input('Digite seu nome: ')
encontrar = input('Digite o que quer encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')