 

cpf_usuario = input('Digite seu CPF: ')
cpf_usuario_ponto = f'{cpf_usuario[:3]}{cpf_usuario[3:3]}{cpf_usuario[4:7]}{cpf_usuario[7:7]}\
{cpf_usuario[8:11]}{cpf_usuario[11:11]}{cpf_usuario[12:]}'



lista_cpf_numeros = list(cpf_usuario_ponto)
lista_cpf_numeros = [int(numero) for numero in lista_cpf_numeros]

#Validação Primeiro Dígito

validacao_digito_1 = ((lista_cpf_numeros[0] * 10) + (lista_cpf_numeros[1] * 9) + (lista_cpf_numeros[2] * 8) + \
(lista_cpf_numeros[3] * 7) + (lista_cpf_numeros[4] * 6) + (lista_cpf_numeros[5] * 5) + \
(lista_cpf_numeros[6] * 4) + (lista_cpf_numeros[7] * 3) + (lista_cpf_numeros[8] * 2)) * 10 % 11

if validacao_digito_1 > 9:
    primeiro_digito = 0
else:
    primeiro_digito = validacao_digito_1

print(f'O primeiro digito é {primeiro_digito}')


#Validação Segundo dígito 

validacao_digito_2 = ((lista_cpf_numeros[0] * 11) + (lista_cpf_numeros[1] * 10) + (lista_cpf_numeros[2] * 9) + \
(lista_cpf_numeros[3] * 8) + (lista_cpf_numeros[4] * 7) + (lista_cpf_numeros[5] * 6) + \
(lista_cpf_numeros[6] * 5) + (lista_cpf_numeros[7] * 4) + (lista_cpf_numeros[8] * 3) + \
(lista_cpf_numeros[9] * 2)) * 10 % 11

if validacao_digito_2 > 9:
    segundo_digito = 0
else:
    segundo_digito = validacao_digito_2

print(f'O segundo digito é {segundo_digito}')



if lista_cpf_numeros[9] == primeiro_digito and lista_cpf_numeros[10] == segundo_digito:
    print(f'{cpf_usuario} é valido')
else:
    print('Cpf inválido')

'''
.replace('.', '')
.replace('-', '')

'''

'''
import re
re.sub(r'[^0-9])
'''