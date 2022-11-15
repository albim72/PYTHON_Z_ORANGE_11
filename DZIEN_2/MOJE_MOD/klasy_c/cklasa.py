from funkcje_c.bfunkcje import *

class CDane:
    def __init__(self,lista,dict):
        self.lista = lista
        self.dict = dict

    def czytaj_lista(self):
        return czytaj(self.lista)

    def czytaj_slownik(self):
        return czytaj_dict(self.dict)
