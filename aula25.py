# Interpolação básica de strings
#s  string
#d e i int
#f float
#x e X Hexadecimal


nome = 'Thiago'
preco = 1000.9589764
variavel = '%s, o preço é R$%.2f' % (nome, preco)
print(variavel)
print('O hexadecimal de %d é %08x' % (1500, 1500))