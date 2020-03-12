n = int(input('digite um número para calcular o seu fatorial :'))
print('Calculando {}! = '.format(n),end='')
f = 1
c = n
while c > 0:
    print('{}'.format(c),end='')
    print(' x' if c > 1 else '= ', end=' ')
    f*=c
    c-=1
print('{}'.format(f))
