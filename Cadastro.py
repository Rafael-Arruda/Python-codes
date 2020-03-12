print('-=-'*10)
print('    CADASTRE UMA PESSOA')
print('-=-'*10)
tot18 = toth = totm20 = 0
while True:
    idade = int(input('idade :'))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('sexo [M/f]:')).strip().upper()[0]
    if idade > 18 :
        tot18 += 1
    if sexo == 'M':
        toth += 1
    if sexo == 'F' and idade < 20:
        totm20 += 1
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resposta == 'N':
        break
    print('-=-'*10)
    print('    CADASTRE UMA PESSOA')
    print('-=-'*10)
print(f'Total de pessoas com mais de 18 anos : {tot18}')
print(f'Ao todo temos {toth} homens cadastrados')
print(f'E temos {totm20} mulheres com menos de 20 anos ')



