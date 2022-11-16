def dodawanie(self,x,y):
    return x+y

def odejmowanie(self,x,y):
    return x-y

def mnozenie(self,x,y):
    return x*y

def inna(self,x=0,y=0):
    return 0

class Dzialanie(type):
    def __init__(cls,clsname,bases,attrs):
        if clsname == "Dodaj":
            cls.operacja = dodawanie
        elif clsname == "Odejmij":
            cls.operacja = odejmowanie
        elif clsname == "Pomnoz":
            cls.operacja = mnozenie
        else:
            cls.operacja = inna


class Opisz(metaclass=Dzialanie):
    pass
class Dodaj(metaclass=Dzialanie):
    pass
class Odejmij(metaclass=Dzialanie):
    pass
class Pomnoz(metaclass=Dzialanie):
    pass

p1 = Opisz()
print(f"wynik działamnia {p1.__class__.__name__} = {p1.operacja()}")
p2 = Dodaj()
print(f"wynik działamnia {p2.__class__.__name__} = {p2.operacja(5,6)}")
p3 = Odejmij()
print(f"wynik działamnia {p3.__class__.__name__} = {p3.operacja(5,6)}")
p4 = Pomnoz()
print(f"wynik działamnia {p4.__class__.__name__} = {p4.operacja(5,6)}")


