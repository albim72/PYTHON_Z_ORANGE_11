odp = input("Czy Ziemia jest płaska? Chcesz znać odpowedź? (t/n) ")
if odp.lower() == "t":
    required = True
else:
    required = False

def odpowiedz(self,*args):
    return "Tak! Ziemia jest płaska!"

def _odpowiedz(self, *args):
    return "Nie! Ziemia jest okrągła!"

class SednoOdpowiedzi(type):
    def __init__(cls,clsname,bases,atrribs):
        if required:
            if clsname =="Einstein":
                cls.odpowiedz = _odpowiedz
            else:
                cls.odpowiedz = odpowiedz

class Arystoteles(metaclass=SednoOdpowiedzi):
    pass

class Platon(metaclass=SednoOdpowiedzi):
    pass

class SwTomasz(metaclass=SednoOdpowiedzi):
    pass

class Einstein(metaclass=SednoOdpowiedzi):
    def __init__(self,lpub):
        self.lpub = lpub
        # self.odpowiedz = self._odpowiedz

    def get_lpub(self):
        return f"liczba publikacji: {self.lpub}"

    # def _odpowiedz(self, *args):
    #     return "Nie! Ziemia jest okrągła!"

fil1 = Arystoteles()
print(fil1.odpowiedz())

fil2 = Platon()
print(fil2.odpowiedz())

fil3 = SwTomasz()
print(fil3.odpowiedz())

fil4 = Einstein(89)
print(fil4.odpowiedz())
print(fil4.get_lpub())
