class Book:
    def __init__(self,id,tytul,autor,cena=10):
        self.idksiazki = id
        self.tytul = tytul
        self.autor = autor
        self.cena = cena
        self.oprawa = "miękka"
        self.create_book()


    def create_book(self):
        print("tworzenie nowej książki....")

    def print_book(self):
        print(f"Tytuł: {self.tytul}, autor: {self.autor}, cena: {self.cena} zł, oprawa: {self.oprawa}")

    def rabat(self):
        if self.cena >25:
            return 0.05*self.cena
        else:
            return 0

    def set_cena(self,nowacena):
        self.cena = nowacena

    def get_cena(self):
        return self.cena



b = Book(4,"Zielony Płomień","Jan Kos",30)
b.print_book()
print(f"rabat: {b.rabat()} zł")
c = Book(5,"Biały Płomień","Jan Kos")
c.oprawa = "twarda"
#c.cena = 23
c.set_cena(27)
c.print_book()
print(f"rabat: {c.rabat()} zł")
print(f"cena po rabacie: {c.get_cena()-c.rabat()} zł")
