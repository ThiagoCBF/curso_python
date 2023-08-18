# tRY -> tenta executar o codigo
#except -> ocorreu algum erro ao tentar executar

numero_str = input('Dobrar o número que vc digitar: ')

try:
    numero_float = float(numero_str)
    print('FLOAT:', numero_float)
    print(f'O dobro de {numero_str} é {numero_float * 2:.2f}')
except:
    print('Isso não é um número')