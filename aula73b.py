#Exercício 2x 3x 4x

def criar_multiplocador(multiplocador):
    def multiplicar(numero):
        return numero * multiplocador
    return multiplicar

duplicar = criar_multiplocador(2)
triplicar = criar_multiplocador(3)
quadruplicar = criar_multiplocador(4)


print(duplicar(2))
print(triplicar(2))
print(quadruplicar(2))