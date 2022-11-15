class Sport:
    def __init__(self,dyscyplina,lata_upr,best_wynik):
        self.best_wynik = best_wynik
        self.lata_upr = lata_upr
        self.dyscyplina = dyscyplina
        
    def infosport(self):
        print(f"dyscyplina: {self.dyscyplina}, lata uprawiania: {self.lata_upr}, "
              f"życiówka: {self.best_wynik}")
