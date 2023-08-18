primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite outro valor: ')

int_primeiro_valor = int(primeiro_valor)
int_segundo_valor = int(segundo_valor)


if int_primeiro_valor >= int_segundo_valor:
    print(f'{int_primeiro_valor} é maior ou igual que o {int_segundo_valor}')
else:
    print(f'{int_segundo_valor} é maior do que o {int_primeiro_valor}')

print(type(int_primeiro_valor))