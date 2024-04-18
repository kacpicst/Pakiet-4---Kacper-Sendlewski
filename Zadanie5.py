def podziel_na_czesci(lista, maks_dlugosc):
    podzielone_czesci = []
    for i in range(0, len(lista), maks_dlugosc):
        podzielone_czesci.append(lista[i:i + maks_dlugosc])
    return podzielone_czesci

moja_lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
czesci = podziel_na_czesci(moja_lista, 4)
print("Podzielona lista:", czesci)
