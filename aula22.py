#Or
#Se uma condição for verdadeira , considera todas verdadeira


entrada = input('[E]ntrada  [S]air: ')
senha_digitada = input('Senha: ')
senha_permitida = '123456'


if entrada == ('E' or entrada == 'e') and senha_digitada == senha_permitida:
    print('Entrar')
else:
    print('Sair')