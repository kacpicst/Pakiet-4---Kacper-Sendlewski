def zastosuj_funkcje_do_krotek(lista_krotek, funkcja):
    return [funkcja(*krotka) for krotka in lista_krotek]

def dodaj(a, b):
    return a + b

krotki = [(1, 2), (3, 4), (5, 6)]
wyniki = zastosuj_funkcje_do_krotek(krotki, dodaj)
print("Wyniki zastosowania funkcji do krotek:", wyniki)
