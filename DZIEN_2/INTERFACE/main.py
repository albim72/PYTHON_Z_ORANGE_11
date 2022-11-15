from pojazd import Pojazd

p = Pojazd()

print(p.silnik("samochód","osobowy","Opel","Vectra","diesel",1.9))
print("*****************************************************")
tr,pr = p.trasa("Lublin","Warszawa",178,1.5)
print(f"trasa: {tr}, {pr}")
print("*****************************************************")
print(f'spalanie silnika [1l/100]: {p.spal_100(178,19):.2f}')
p.paliwo = 8.09
print(f"cena paliwa za 1l: {p.paliwo}")
print(f'koszt przejazdu: {p.koszt_przejazdu(178,19,p.paliwo)} zł')
