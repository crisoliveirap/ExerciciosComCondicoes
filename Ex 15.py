# Ex 15: Analisando triângulos
a = float(input('Primeiro segmento:'))
b = float(input('Segundo segmento:'))
c = float(input('Terceiro segmento:'))
if a < b + c and b < a +c and c < a + b:
    if a == b == c:
        print('Os segmentos acima PODEM formar um triângulo EQUILÁTERO.')
    elif a != b != c != a:
        print('Os segmentos acima PODEM formar um triângulo ESCALENO.')
    else:
        print('Os segmentos acima PODEM formar um triângulo ISÓSCELES.')
else:
    print('Os segmentos não podem formar um triângulo.')