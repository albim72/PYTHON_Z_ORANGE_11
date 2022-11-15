from pracownik import Pracownik
from Sport import Sport
from ekstra import Ekstra

class Student(Pracownik,Sport,Ekstra):
    def __init__(self,imie,wiek,waga,wzrost,id_studenta,wydzial,kierunek,rok_stud,
                 firma="",stanowisko="",lata_pracy="",wynagrodzenie="",dyscyplina="",lata_upr="",best_wynik=""):
        Pracownik.__init__(self,imie,wiek,waga,wzrost,firma,stanowisko,lata_pracy,wynagrodzenie)
        Sport.__init__(self,dyscyplina,lata_upr,best_wynik)
        self.rok_stud = rok_stud
        self.kierunek = kierunek
        self.wydzial = wydzial
        self.id_studenta = id_studenta

    def print_student(self):
        print(f"dane studenta nr {self.id_studenta}, wydział: {self.wydzial}, kierunek studiów: {self.kierunek}, "
              f"rok studiów: {self.rok_stud}.")

    def czypracownik(self):
        return self.firma != ""
        
