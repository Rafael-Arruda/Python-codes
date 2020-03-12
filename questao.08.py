def transposta(matriz):
    transposta = []
    for c in range(len(matriz[0])):
        linha = []
        for l in range(len(matriz)):
            elemento = matriz[l][c]
            linha.append(elemento)
        transposta.append(linha)
    return transposta
print(transposta([[2,3,0],[-1,-2,-1]]))


