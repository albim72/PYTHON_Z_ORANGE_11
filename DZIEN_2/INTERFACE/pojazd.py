from ipojazd import IPojazd

class Pojazd(IPojazd):

    def silnik(self, rodzaj_pojazd, kategoria, marka, model, rodzaj_silnika, poj):
        return f"Pojazd -> {rodzaj_pojazd}, {kategoria}, marka: {marka}, model: {model}, " \
               f"rodzaj silnika: {rodzaj_silnika}, pojemność: {poj} l."

    def trasa(self, start, koniec, odl, czas_przejazdu):
        trasa = f"początek trasy: {start}, koniec trasy: {koniec}"
        przej = f"odlgłość: {odl} km, czas przejazdu: {czas_przejazdu} h"
        return trasa,przej

    def spal_100(self, odl, litry):
        return litry*100/odl

    def koszt_przejazdu(self, odl, litry, cena_l):
        return self.spal_100(odl,litry)*(odl/100)*cena_l
