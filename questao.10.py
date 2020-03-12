def permutacoes(lista):
   if len(lista) == 1:
       return [lista]
   resp = []
   for i in range(len(lista)):
       x = lista[i]
       resto = lista[:i] + lista[i+1:]
       perms = permutacoes(resto)
       for perm in perms:
           perm.append(x)
       resp = resp + perms

   return resp


print(permutacoes([1, 2, 3, 4]))
