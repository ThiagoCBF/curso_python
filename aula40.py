#Calculadora While
num1 = 0
num2 = 0
while True:
    num1 = input('Digite um número: ')
    num2 = input('Digite outro número: ')
    operador = input('Digite uma operação (*+-/): ')
    
    numeros_validos = None
    num_1_float = 0
    num_2_float = 0

    try:
        num_1_float = float(num1)
        num_2_float = float(num2)
        numeros_validos = True
    except:
        numeros_validos = None
    
    if numeros_validos is None:
        print('Um dos números é inválido')
        continue

    operadores_permitidos = "+-/*"

    if operador not in operadores_permitidos:
        print('Operador inválido')
        continue

    if len(operador) > 1:
        print('Digite apenas um operador')
        continue

    if operador == '*' :
        print(num_1_float * num_2_float)
        
    elif operador == '+':
        print(num_1_float + num_2_float)
        
    elif operador == '-':
        print(num_1_float - num_2_float)
        
    elif operador == '/':
        print(num_1_float / num_2_float)
        
    else:
        print('Não deve chegar aqui')



    sair = input('Quer sair? [s]im: ').lower().startswith('s')
    if sair is True:
        break