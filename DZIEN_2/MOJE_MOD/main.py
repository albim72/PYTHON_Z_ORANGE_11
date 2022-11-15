#import dane
#import dane as dn
from funkcje_c.bfunkcje import czytaj,czytaj_dict

from dane import book as ksiazka
from dane import nb as liczby

print(ksiazka)
print(liczby)

print(list(enumerate(ksiazka)))
print(list(enumerate(liczby,101)))

czytaj(liczby)
czytaj_dict(ksiazka)
