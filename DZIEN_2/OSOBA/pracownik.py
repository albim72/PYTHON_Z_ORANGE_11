from osoba import Osoba

class Pracownik(Osoba):
    def __init__(self,imie,wiek,waga,wzrost,firma,stanowisko,lata_pracy,wynagrodzenie):
        super().__init__(imie,wiek,waga,wzrost)
        self.wynagrodzenie = wynagrodzenie
        self.lata_pracy = lata_pracy
        self.stanowisko = stanowisko
        self.firma = firma
        
    
    def print_pracownik(self):
        print(f"dane pracownika -> firma: {self.firma}, stanowisko pracy: {self.stanowisko}, "
              f"lata pracy: {self.lata_pracy}, wynagrodzenie: {self.wynagrodzenie} zł")

    def czypracownik(self):
        return True
