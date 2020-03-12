from random import randint
vitoria = 0
print('-=-'*10)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('-=-'*10)
while True:
     jogador = int(input('Diga um valor : '))
     computador = randint(0, 10)
     total = jogador + computador
     tipo = ' '
     while tipo not in 'PI':
         tipo = str(input('PAR OU ÍMPAR [P/I] : ')).strip().upper()[0]
     print(f'você jogou {jogador} e o computador jogou {computador}.Total de {total} ', end= '')
     print('DEU PAR' if total % 2 == 0 else 'DEU IMPAR')
     if tipo == 'P':
         if total % 2 == 0:
             print('voce venceu ')
             vitoria += 1
         else :
             print('voce perdeu')
             break
     elif tipo == 'I':
         if total % 2 == 1 :
             print('voce venceu ')
             vitoria += 1
         else :
             print('voce perdeu')
             break
     print('vamos jogar novamente ...')
print(f'GAME OVER! . voce venceu {vitoria} vezes .')

