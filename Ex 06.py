# Ex 06: Maior e menor valores
a = int(input('Digite o primeiro número:'))
b = int(input('Digite o segundo número:'))
c = int(input('Digite o terceiro número:'))
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c

maior = a
if b > a and b > c:
    maior = b
if c > b and c > a:
    maior = c
print('O menor número digitado foi {}.'.format(menor))
print('O maior número digitado foi {}.'.format(maior))