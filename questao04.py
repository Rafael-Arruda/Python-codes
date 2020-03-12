def soma_diagonal_secundaria(matriz):
    soma = 0
    for i in range(len(matriz)):
        soma = soma + matriz[i][-i-1]
    return soma

soma_diagonal = soma_diagonal_secundaria([[4, 5, 8], [-7, 8, 9], [8, -3, 2]])
print(f'A soma dos elementos da diagonal secundária da matriz é {soma_diagonal}')


