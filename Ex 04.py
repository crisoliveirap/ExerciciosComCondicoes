# Ex 04: Calculando o custo da viagem
viagem = float(input('Digite a distância da viagem em km:'))
if viagem <= 200:
    print('O preço da viagem será de R${:.2f}.'.format(0.50*viagem))
else:
    print('O preço da viagem será de R${:.2f}.'.format(0.45*viagem))

