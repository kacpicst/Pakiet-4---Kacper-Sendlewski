def generuj_potegowanie(exponent):
    def potegowanie(x):
        return x ** exponent
    return potegowanie

podnies_do_kwadratu = generuj_potegowanie(2)
print("5 do potęgi 2 wynosi:", podnies_do_kwadratu(5))

podnies_do_szescianu = generuj_potegowanie(3)
print("8 do potęgi 3 wynosi:", podnies_do_szescianu(8))
