# Ex 16: Índice de Massa Corporal
peso = float(input('Digite seu peso (Kg):'))
altura = float(input('Digite sua altura (m):'))
imc = peso / (altura ** 2)
print('O IMC dessa pessoas é de {:.2f}.'.format(imc))
if imc < 18.5:
    print('Você está ABAIXO DO PESO.')
elif 25 > imc >= 18.5:
    print('Você está em PESO IDEAL.')
elif 30 > imc >= 25:
    print('Você está em SOBREPESO.')
elif 40 > imc >= 30:
    print('Você está em OBESIDADE.')
else:
    print('Você está em OBESIDADE MÓRBIDA. Cuidado!')
