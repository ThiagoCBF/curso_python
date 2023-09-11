'''
arg - Argumentos não nomeados
* - *args (enpacotamento e desempacotamento)
'''

x, y, *resto = 1, 2, 3, 4
print(x, y, resto)



def soma(*args):
    total = 0
    for numero in args:
        total += numero
    return total

soma_1_2_3 = soma(1, 2, 3)
soma_3_5_6 = soma(4, 5, 6)

numeros = 1, 2, 3, 4, 5, 6, 7, 8, 78
outra_soma = soma(*numeros)
print(outra_soma)
print(sum(numeros))