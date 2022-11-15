from prostokat import  Prostokat
from trojkat import Trojkat
from trapez import Trapez
from kolo import Kolo

print("POLA FIGUR")

pr = Prostokat(6.6,4.8)
tr = Trojkat(4.7,6.2)

print(f"pole trójkąta wynosi {tr.policz_pole():.2f}")
print(f"pole prostokąta wynosi {pr.policz_pole():.2f}")


trp = Trapez(8.4,6.8,4.9)
print(f"pole trapezu wynosi {trp.policz_pole():.2f}")

#utworz klasę Kolo(Figura) i utwórz właściwy konstruktor z jednym atrybutem a, oznaczającym promkień
#pole = math.pi * a**2
#policz pole koła dla promienia 5.5

kl = Kolo(5.5)
print(f"pole koła wynosi {kl.policz_pole():.2f}")

