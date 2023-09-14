#Exercício multiplica numeros uns com outros


def multiplica(*args):
    total = 1
    for numero in args:
        total*= numero
    return total
    
multiplicacao = multiplica(1, 2, 3, 4, 5)
print(multiplicacao)

#Exercício Função define se é ímpar ou par

def impar(x):
    par = x % 2 ==0
    if par:
        return f'{x} é par'
    return f'{x} é ímpar'

print(impar(11))