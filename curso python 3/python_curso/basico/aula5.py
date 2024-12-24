velocidade = 60
local_carro = 101

RADAR_1 = 61
LOCAL_1 = 100
RADAR_RANGE = 1

velocidade_carro_pass_radar_1 = velocidade > RADAR_1
carro_multado_radar_1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and local_carro  <= (LOCAL_1 + RADAR_RANGE) and velocidade > RADAR_1

if velocidade_carro_pass_radar_1:
    print('Velocidade do carro passou do rada 1')
if velocidade_carro_pass_radar_1:
    print('Carro passou radar 1')
if carro_multado_radar_1:
    print('Carro foi multadoem redar 1')
