# Ex 07: Aumento de salário
salario = float(input('Qual o valor do seu salário? R$'))
if salario > 1250:
    aumento = salario + (salario * 0.10)
else:
    aumento = salario + (salario * 0.15)
print('Seu salário aumentou para R${:.2f}.'.format(salario))