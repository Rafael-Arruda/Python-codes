tot = 0
num = int(input('digite um número:'))
for c in range(1,num+1):
    if num % c == 0:
        print('\033[33m',end =' ')
        tot += 1
    else:
        print('\033[31m', end=' ')
    print('{}'.format(c), end=' ')
print('\n\033[mO número {} foi divisível {} vezes'.format(num,tot))
if tot == 2:
    print('e por isso ELE É PRIMO')
else:
    print(' e por isso ele NÃO É PRIMO')

