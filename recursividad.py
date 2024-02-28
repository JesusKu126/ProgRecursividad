def permutaciones(lista):
    if len(lista) == 0:
        return [[]]
    else:
        permutations = []
        for i in range(len(lista)):
            elemento_actual = lista[i]
            lista_sin_elemento_actual = lista[:i] + lista[i+1:]
            for p in permutaciones(lista_sin_elemento_actual):
                permutations.append([elemento_actual] + p)
        return permutations

# Ejemplo de uso
lista_ejemplo = [1, 2, 3]
print("Permutaciones de", lista_ejemplo, ":")
for perm in permutaciones(lista_ejemplo):
    print(perm)
