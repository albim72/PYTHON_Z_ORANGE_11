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

    def bmi(self):
        return self.waga/(self.wzrost/100)**2

    def opis_bmi(self):
        if self.bmi()<18.5:
            return "niedowaga"
        elif self.bmi()<=25:
            return "waga prawidłowa"
        elif self.bmi()<=30:
            return "nadwaga"
        else:
            return "otyłość"
        
    def policz_ppm(self,plec):
        if plec == "k":
            return 655.1 + 9.563*self.waga + 1.85*self.wzrost -4.676*self.wiek
        elif plec == "m":
            return 66.5 + 13.75 * self.waga + 5.003 * self.wzrost - 6.775 * self.wiek
        else:
            return "wpisz k - kobieta, m - mężczyzna"
