a = 'A'
b = 'B'
c = 1.1
formato = 'a={nome1} b={nome2} c={nome3:.2f}'.format(nome1=a, nome2=b, nome3=c)

print(formato)


nome = "Luiz"
idade = 23
formatoa = '{0} tem {1} anos'
print(formatoa.format(nome, idade))