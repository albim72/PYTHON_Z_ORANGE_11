from abc import ABC, abstractmethod

class Prototyp(ABC):

    def __init__(self,x):
        self.x = x

    def msg(self):
        return "to jest metoda nieabstrakcyjna klasy abstrakcyjnej"

    @abstractmethod
    def policz(self):
        pass

    @abstractmethod
    def policz_x(self):
        return self.x*3

class ZwKlasa(Prototyp):
    def __init__(self,x,y):
        super().__init__(x)
        self.y=y

    def policz(self):
        return 999

    def policz_x(self):
        return super().policz_x() + self.y*4


zw = ZwKlasa(4,8)
