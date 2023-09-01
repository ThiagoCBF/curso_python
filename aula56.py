lista = []
item_novo = ''
item_apagado = ''

import os

while True:
    
    menu = input('Selecione uma opção \n [i]nserir [a]pagar [l]istar: ')
    if menu == 'i':
        item_novo = input('Escreva o novo item: ')
        lista.append(item_novo)
        os.system('cls')
        print(f'{item_novo} foi adicionada a lista')
        indices = (len(lista))
        continue
    
    if menu == 'a':
        if lista == []:
            os.system('cls')
            print('Lista vazia , impossivel apagar algo')
            continue
        else: 
            item_apagado = int(input('Escreva o indice a ser apagado da lista: '))
            del lista[item_apagado]
            indices = (len(lista))
            continue
    if menu == 'l':
        if lista == []:
            os.system('cls')
            print('Lista vazia , impossivel listar algo')
            continue
        else:
            os.system('cls')
            for i, valor in enumerate(lista):
                print(i, valor)
            continue
    else:
        print('Selecione uma das opções validas')
