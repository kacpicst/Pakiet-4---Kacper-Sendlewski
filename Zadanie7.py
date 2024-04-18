def scalanie_słowników(*args):
    wynik = {}
    for słownik in args:
        for klucz, wartość in słownik.items():
            if klucz in wynik:
                wynik[klucz] += wartość
            else:
                wynik[klucz] = wartość
    return wynik

słownik1 = {'a': 10, 'b': 20, 'c': 30}
słownik2 = {'a': 5, 'b': 15, 'd': 25}
słownik3 = {'b': 10, 'c': 20, 'e': 30}

scalony_słownik = scalanie_słowników(słownik1, słownik2, słownik3)
print("Scalone słowniki:", scalony_słownik)
