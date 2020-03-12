qtd_linhas = int(input('digite a qtd de linhas:'))
qtd_colunas = int(input('digite a qtd de colunas:'))
matriz = []
for l in range(qtd_linhas):
    linha = []
    for c in range(qtd_colunas):
        elemento = int(input(f'digite um valor para [{l},{c}]'))
        linha.append(elemento)
    matriz.append(linha)
print(matriz)
for l in range(qtd_linhas):
    maior = menor = matriz[l][0]
    for c in range(qtd_colunas):
        if matriz[l][c] > maior:
            maior = matriz[l][c]
        if matriz[l][c] < menor:
            menor = matriz[l][c]
    print(f'O menor e maior elemento da linha {l+1} são respectivamente : {menor} e {maior}')

