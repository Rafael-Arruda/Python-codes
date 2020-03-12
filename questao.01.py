linha = int(input('informe o número de linhas da matriz:'))
coluna = int(input('informe o número de colunas da matriz:'))
matriz = []
soma_impares = 0
for l in range(linha):
    linha_matriz = []
    for c in range(coluna):
        elemento = int(input(f"digite um elemento para [{l},{c}]"))
        linha_matriz.append(elemento)
        if elemento % 2 != 0:
            soma_impares = soma_impares + elemento
    matriz.append(linha_matriz)
print(matriz)
print('A soma dos valores ímpares da matriz é {}'.format(soma_impares))

