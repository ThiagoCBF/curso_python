'''
Sets - Conjuntos em Python (tipo set)
Representações graficamente 'Diagrama Venn'
Sets em Python são mutáveis, porém aceitam apenas tipos imutáveis como valor interno

Não Garante Ordem
Remove Valores Duplicados 
Não tem índices
'''

#Métodos Úteis
s1 = set()
s1 = {'Thiago', 1, 2, 3, 3, 3,}
print(s1)

s2 = set()
s2.add('Thiago')
s2.clear()
s2.add(2)
s2.update(('Olá mundo,', 1, 2, 3, 4,))
s1.discard('Olá Mundo')
print(s2)


#Operadores úteis
'''
União | 
Intersecção &
Diferença - (Itens presente no set da esquerda)
Diferença Simétrica ^ (Não esta presente em Ambos)
'''

s3 = {1, 2, 3}
s4 = {2, 3, 4}
s5 = s3 | s4
print(s3)