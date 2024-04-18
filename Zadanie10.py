def generuj_permutacje(lista):
    if len(lista) == 0:
        return [[]]
    if len(lista) == 1:
        return [lista]

    permutacje = []
    for i in range(len(lista)):
        pierwszy_element = lista[i]
        reszta_listy = lista[:i] + lista[i+1:]
        reszta_permutacji = generuj_permutacje(reszta_listy)
        for permutacja in reszta_permutacji:
            permutacje.append([pierwszy_element] + permutacja)
    return permutacje

moja_lista = [1, 2, 3]
wszystkie_permutacje = generuj_permutacje(moja_lista)
print("Wszystkie permutacje:", wszystkie_permutacje)
