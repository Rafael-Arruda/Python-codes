def multiplica(mat1, mat2):
    matrizes = []
    for i in range(len(mat1)):
        linha = []
        for j in range(len(mat2[0])):
            elemento = 0
            for k in range(len(mat2)):
                elemento = elemento + mat1[i][k] * mat2[k][j]
            linha.append(elemento)
        matrizes.append(linha)
    return matrizes

print(multiplica([[2,-1,3],[3,5,-7]],[[3,4,5,6],[-1,-7,0,9],[9,5,-3,2]]))



