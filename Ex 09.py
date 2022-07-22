# Ex 09: Simulando um empréstimo
casa = float(input('Qual o valor da casa que deseja comprar? R$'))
salario = float(input('Qual o valor do seu salário? R$'))
tempo = int(input('Em quantos anos deseja pagar?'))
parcela = casa / (tempo * 12)
print('Para pagar uma casa de R${:.2f} em {} anos, a prestação será de R${:.2f}.'.format(casa, tempo, parcela))
if parcela <= (salario * 0.30):
    print('O empréstimo foi aprovado!')
else:
    print('O empréstimo foi negado!')