def zastosuj_funkcje_do_listy(lista, funkcja):
    return [funkcja(element) for element in lista]

def podwoj(x):
    return 2 * x

moja_lista = [1, 2, 3, 4, 5]

nowa_lista = zastosuj_funkcje_do_listy(moja_lista, podwoj)

print("Oryginalna lista:", moja_lista)
print("Nowa lista po zastosowaniu funkcji podwajającej:", nowa_lista)
