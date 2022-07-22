# Ex 17: Gerenciador de pagamentos
print('=' * 10, 'LOJA DA CRIS', '=' * 10)
compra = float(input('Qual o valor total da compra?'))
print('''FORMAS DE PAGAMENTO:
[ 1 ] À vista dinheiro/cheque
[ 2 ] À vista cartão
[ 3 ] 2 vezes no cartão
[ 4 ] 3 vezes ou mais no cartão''')
pagamento = int(input('Escolha uma forma de pagamento:'))
if pagamento == 1:
   total = compra - (compra * 0.10)
   print('Você ganhou 10% de desconto! Total da compra: R${:.2f}.'.format(total))
elif pagamento == 2:
   total = compra - (compra * 0.05)
   print('Você ganhou 5% de desconto! Total da compra: R${}'.format(total))
elif pagamento == 3:
   total = compra / 2
   print('Sua compra será parcelada em 2 vezes de R${}.'.format(total))
elif pagamento == 4:
   parc = int(input('Quantas parcelas?'))
   final = compra + (compra * 0.20)
   if parc >= 3:
       print('Sua compra será parcelada em {} vezes de R${:.2f} com juros.'.format(parc, final / parc))
       print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(compra, final))