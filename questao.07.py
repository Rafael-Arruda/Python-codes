def troca_linhas(mat, indice_lin1, indice_lin2):
     aux = mat[indice_lin1]
     mat[indice_lin1] = mat[indice_lin2]
     mat[indice_lin2] = aux
     return mat

print(troca_linhas([[1,2],[3,4],[5,6]],0 , 2))
