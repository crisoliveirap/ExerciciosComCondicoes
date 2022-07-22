# Ex 02: Radar eletrônico
velocidade = float(input('Digite a velocidade do carro:'))
if velocidade > 80:
    print('MULTADO! Você excedeu o limite permitido que é de 80km/h.')
    multa = (velocidade -80) * 7
    print('Você deve pagar uma multa de R${:.2f}.'.format(multa))
else:
    print('Tenha um bom dia! Dirija com segurança!')

