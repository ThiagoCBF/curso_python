'''
Escopo de funções em Python
Escopo = local onde o código pode atingir
Escopo 'local' e 'global
local = onde nomes do mesmo local podem ser alcançados
global = todo o código pode alcançar
'''
x = 1

def escopo():
    global x 
    x = 10

    def outra_funcao():
        x = 11
        y = 2
        print(x, y)

    outra_funcao()
    print(x)

print(x)
escopo()
print(x)