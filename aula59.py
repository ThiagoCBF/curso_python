'''
Lista de listas e seus Índices
'''

salas = [
    ['Thiago', 'Couto', ], ['Ferreira', ], ['Barbosa', 'Silva',] 
]
'''
print(salas[0][0])
print(salas[0][1])
print(salas[2][0])
print(salas[1][0])
'''

for sala in salas:
    for aluno in sala:
        print(aluno)