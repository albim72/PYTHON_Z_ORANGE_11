class Osoba:
    def __init__(self,imie,wiek,waga,wzrost):
        self.wzrost = wzrost
        self.waga = waga
        self.wiek = wiek
        self.imie = imie
        self.kolor_oczu = "brązowy"
        self.info()
        
    def info(self):
        print("Utworzono nową instancję klasy Osoba...")
        
    def print_osoba(self):
        print(f"dane osoby -> imię: {self.imie}, wiek: {self.wiek} lat, waga: {self.waga} kg, "
              f"wzrost: {self.wzrost} cm, kolor oczu: {self.kolor_oczu}")
        
    def wiekza10lat(self):
        return self.wiek + 10
    
    def czypracownik(self):
        return False
