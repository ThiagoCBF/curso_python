"""
Repetições
while(enquanto)
executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um codigo nao tem fim
"""

condicao = True;

while condicao:
    nome = input('Qual éo seu nome: ')
    print(f'Seu nome é {nome}')

    if nome == 'sair':
        break