acerto = 0

perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '5'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/5?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '2',
    },
]

perguntas = list(perguntas)


#Pergunta 1

p1 = perguntas[0]
print('Pergunta:', p1['Pergunta'])

opcoes_p1 = p1['Opções']

for i, valor in enumerate(opcoes_p1):
    print(f'{i})', valor)

resposta_p1 = input('Escolha uma opção: ')
if resposta_p1 == '2':
    print('Certa Resposta')
    acerto = acerto + 1
else:
    print('Resposta incorreta')


#Pergunta 2

p2 = perguntas[1]
print('Pergunta:', p2['Pergunta'])

opcoes_p2 = p2['Opções']

for i, valor in enumerate(opcoes_p2):
     print(f'{i})', valor)

resposta_p2 = input('Escolha uma opção: ')
if resposta_p2 == '0':
    print('Certa Resposta')
    acerto = acerto + 1
else:
    print('Resposta incorreta')



#Pergunta 3

p3 = perguntas[2]
print('Pergunta:', p3['Pergunta'])

opcoes_p3 = p3['Opções']

for i, valor in enumerate(opcoes_p3):
     print(f'{i})', valor)

resposta_p3 = input('Escolha uma opção: ')
if resposta_p3 == '2':
    print('Certa Resposta')
    acerto = acerto + 1
else:
    print('Resposta incorreta')

print(f'Voce acertou {acerto} de 3')




