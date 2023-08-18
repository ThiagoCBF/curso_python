# Constante = "Variaveis" que não vão mudar

velocidade_carro = 61
posição_carro = 100

RADAR_1 = 60
LOCAL_1 = 100
RADAR_RANGE = 1

vel_carro_pass_radar_1 = velocidade_carro > RADAR_1
carro_passou_radar = posição_carro >= (LOCAL_1 - RADAR_RANGE) and posição_carro <= (LOCAL_1 + RADAR_RANGE)
carro_multado = carro_passou_radar and vel_carro_pass_radar_1

if vel_carro_pass_radar_1:
    print('Sua velocidade excedeu a velocidade permitida')
else:
    print('Sua velocidade esta nas velocidades permitidas')
if carro_passou_radar:
    print('Carro passou radar 1')

if carro_multado:
    print('Carro multado em radar 1')