from collections import Counter

def najczestszy_element(lista):
    licznik = Counter(lista)
    return max(licznik, key=licznik.get)

moja_lista = [1, 2, 3, 2, 2, 4, 5, 2, 3, 3]
najczestszy = najczestszy_element(moja_lista)
print("Najczęściej występujący element:", najczestszy)
