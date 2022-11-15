#import dane
#import dane as dn
from funkcje_c.bfunkcje import czytaj,czytaj_dict
from klasy_c.cklasa import CDane

from dane import book as ksiazka
from dane import nb as liczby

print(ksiazka)
print(liczby)

print(list(enumerate(ksiazka)))
print(list(enumerate(liczby,101)))

czytaj(liczby)
czytaj_dict(ksiazka)

print("_________________ działanie z klasy __________________")

cd = CDane(liczby,ksiazka)
cd.czytaj_lista()
cd.czytaj_slownik()
