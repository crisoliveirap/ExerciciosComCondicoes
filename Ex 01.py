# Ex 01: Usuário tenta descobrir qual número o computador pensou
from random import randint
from time import sleep
computador = randint(0, 10) # Computador sorteia um número
print('-=-'*20)
print('Vou pensar em um número entre 0 e 10. Tente adivinhar...')
print('-=-'*20)
jogador = int(input('Em qual número eu pensei?'))
print('PROCESSANDO...')
sleep(3)
if jogador == computador:
    print('Você ACERTOU! O número pensado foi {}.'.format(jogador))
else:
    print('Você ERROU! O número certo era {}.'.format(computador))

