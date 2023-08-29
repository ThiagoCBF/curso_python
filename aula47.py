palavra_secreta = 'limonada'
palavra_formatada = '********'
chute = ''
contador = 0
while palavra_secreta != palavra_formatada:
    
    letra_usuario = input('Digite uma letra: ')

    if len(letra_usuario) > 1:
        print('Digite apenas uma letra')
        continue
    if letra_usuario in palavra_secreta:
        chute = letra_usuario
        contador += 1
        if chute == 'a':
            palavra_formatada = f'{palavra_formatada[:5]}a{palavra_formatada[6:]}'
            palavra_formatada = f'{palavra_formatada[:7]}a{palavra_formatada[8:]}'
            print(f'Palavra Secreta é : {palavra_formatada}')
            continue
        if chute == 'l':
            palavra_formatada = f'{palavra_formatada[:0]}l{palavra_formatada[1:]}'
            print(f'Palavra Secreta é : {palavra_formatada}')
            continue
        if chute == 'i':
            palavra_formatada = f'{palavra_formatada[:1]}i{palavra_formatada[2:]}'
            print(f'Palavra Secreta é : {palavra_formatada}')
            continue
        if chute == 'm':
            palavra_formatada = f'{palavra_formatada[:2]}m{palavra_formatada[3:]}'
            print(f'Palavra Secreta é : {palavra_formatada}')
            continue
        if chute == 'o':
            palavra_formatada = f'{palavra_formatada[:3]}o{palavra_formatada[4:]}'
            print(f'Palavra Secreta é : {palavra_formatada}')
            continue
        if chute == 'n':
            palavra_formatada = f'{palavra_formatada[:4]}n{palavra_formatada[5:]}'
            print(f'Palavra Secreta é : {palavra_formatada}')

        if chute == 'd':
            palavra_formatada = f'{palavra_formatada[:6]}d{palavra_formatada[7:]}'
            print(f'Palavra Secreta é : {palavra_formatada}')
            continue
    if letra_usuario not in palavra_secreta:
        print(f'{letra_usuario} não está na palavra secreta')
        continue

   
    
print(f'A palavra secreta era {palavra_formatada} ')
print(f'Voce conseguiu em {contador} tentativas')