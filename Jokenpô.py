from random import randint
from time import sleep
itens = ('pedra' , 'papel' , 'tesoura')
computador=randint(0 , 2)
print('''suas opções:
[0] pedra 
[1] papel
[2] tesoura''')
jogador = int(input('qual é sua jogada?'))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('-=-'*10)
print('computador jogou {}'.format(itens[computador]))
print('o jogador jogou {}'.format(itens[jogador]))
print('-=-'*10)
if computador == 0: #computador jogou pedra
   if jogador==0:
       print('empate')
   elif jogador == 1:
        print('jogador venceu')
   elif jogador == 2:
        print('computador venceu')
   else:
       print('jogada inválida')
elif computador ==1: #computador jogou papel
     if jogador ==0:
         print('computador venceu')
     elif jogador == 1:
          print('empate')
     elif jogador == 2:
          print('jogador venceu')
     else:
         print('jogada inválida')
elif computador ==2: #computador jogou tesoura
     if jogador == 0:
         print('jogador venceu')
     elif jogador == 1:
         print('computador venceu')
     elif jogador == 2:
          print('empate')
     else:
         print('jogada inválida')
