qtd_linhas = int(input('digite o número de linhas:'))
qtd_colunas = int(input('digite o número de colunas:'))
matriz = []
maior = 0
for l in range(qtd_linhas):
    linha = []
    for c in range(qtd_colunas):
        elemento = int(input(f'digite um elemento para [{l},{c}]:'))
        linha.append(elemento)
        if elemento > maior:
            maior = elemento
    matriz.append(linha)
print(matriz)
print(f'o maior elemento da matriz é {maior}')
for l in range(qtd_linhas):
    for c in range(qtd_colunas):
        matriz[l][c] = matriz[l][c] * maior
print(matriz)
