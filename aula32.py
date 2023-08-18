#Exercicio 1 (Nome impar ou par)

numero = input('Digite um número inteiro: ')

try:
    numero_int = int(numero)
    if (numero_int % 2) == 0:
        print('Este número é par')
    elif (numero_int % 2) != 0:
        print('Este número é impar')
    else:
        print('Isso não é um número inteiro')
except:
    print('Isso não é um número inteiro')

#Exercicio 2 (Saudações em relação horario)

horas_atual = input('Digite que horas são: ')

try:
    horas_autal_float = float(horas_atual)
    if horas_autal_float >= 0 and horas_autal_float <= 11:
        print('Bom dia')
    if horas_autal_float > 11 and horas_autal_float <= 17:
        print('Boa Tarde')
    if horas_autal_float > 17 and horas_autal_float < 24:
        print('Boa Noite')
except:
    print('Isso não é um horário')




#Exercicio 3 (Avaliador Tamanho Nome)

primeiro_nome = input('Qual é o seu primeiro nome? ')

try:
    teste_primeiro_nome = float(primeiro_nome)
    
    print('Isso não é um nome')
except:
    str_nome = str(primeiro_nome)
    if len(str_nome) <= 4:
        print('Seu nome é curto')
    elif len(str_nome) >= 5 and len(str_nome) <= 6:
        print('Seu nome é normal')
    elif len(str_nome) > 6:
        print('Seu nome é grande')
        
