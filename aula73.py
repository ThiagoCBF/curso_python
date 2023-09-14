#Exercício 2x , 3X e 4x numeros

def duplicar(x2, x3, x4):
    x2 = x2 * 2
    x3 = x3 * 3
    x4 = x4 * 4
    return x2, x3, x4

numero = int(input('Escolha um numero: '))
print(duplicar(numero, numero, numero))
