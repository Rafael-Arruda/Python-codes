qtd_linhas = int(input('digite a quantidade de linhas da matriz :'))
qtd_colunas = int(input('digite a quantidade de colunas da matriz:'))
matriz = []
soma_cada_linha = []
soma_cada_coluna = []
soma_d_principal = 0
soma_d_secundaria = 0
#MONTANDO O ESQUELETO DA MATRIZ COM DIMENSOES DEFINIDAS PELO USUARIO E JA PEGANDO  A SOMA DE CADA LINHA E DE CADA COLUNA!!
for l in range(qtd_linhas):
    linhas = []
    soma_l = 0
    for c in range(qtd_colunas):
        elemento = int(input(f'digite um valor para a posição [{l}][{c}] da matriz:'))
        linhas.append(elemento)
        soma_l = soma_l + elemento
    soma_cada_linha.append(soma_l)
    matriz.append(linhas)
for c in range(qtd_colunas):
    soma_c = 0
    for l in range(qtd_linhas):
         soma_c = soma_c + matriz[l][c]
    soma_cada_coluna.append(soma_c)
#PEGANDO A SOMA DA DIAGONAL PRINCIPAL
for k in range(qtd_linhas):
    soma_d_principal = soma_d_principal + matriz[k][k]
#PEGANDO A SOMA DA DIAGONAL SECUNDÁRIA
for i in range(qtd_linhas):
    soma_d_secundaria = soma_d_secundaria + matriz[i][-i-1]
#VERIFICANDO SE TODAS AS LINHAS POSSUEM A MESMA SOMA
soma_l = soma_cada_linha[0]
while True:
    for elem in soma_cada_linha:
        if elem == soma_l:
            soma_l = elem
        else:
            break
    break
#VERIFICANDO SE TODAS AS COLUNAS POSSUEM A MESMA SOMA
soma_c = soma_cada_coluna[0]
while True:
    for elem in soma_cada_coluna:
        if elem == soma_c:
            soma_c = elem
        else:
            break
    break
#VERIFICANDO SE A MATRIZ É UM QUADRADO MÁGICO
if soma_l == soma_c == soma_d_principal == soma_d_secundaria:
    print(matriz)
    print(soma_cada_linha)
    print(soma_cada_coluna)
    print(soma_d_principal)
    print(soma_d_secundaria)
    print('A matriz é um quadrado mágico...')
else:
    print(matriz)
    print(soma_cada_linha)
    print(soma_cada_coluna)
    print(soma_d_principal)
    print(soma_d_secundaria)
    print('a matriz não é um quadrado mágico ')
