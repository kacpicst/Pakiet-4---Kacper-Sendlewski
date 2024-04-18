def filtrowanie_parzystych(słownik):
    wynik = {}
    for klucz, wartość in słownik.items():
        if isinstance(wartość, int) and wartość % 2 == 0:
            wynik[klucz] = wartość
    return wynik

słownik = {'a': 3, 'b': 6, 'c': 9, 'd': 12, 'e': 15}
wynik = filtrowanie_parzystych(słownik)
print("Oryginalny słownik:", słownik)
print("Słownik po filtrowaniu:", wynik)
