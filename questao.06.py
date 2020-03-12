def inverte_lista(lista):
    if len(lista) == 1:
        return [lista[0]]
    else:
        return [lista[-1]] + inverte_lista(lista[:-1])

def inverter_linhas(mat):
    for c in range(len(mat)):
        mat[c] = inverte_lista(mat[c])
    return mat

print(inverter_linhas([[1,2,5,3],[4,5,2,6]]))



