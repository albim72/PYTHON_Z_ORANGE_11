import math
import sys
from liczbaujemna import UjemnaSilnia

#n!=1*2*3*...*n
#double -> 1.8E+308 , min 2.4E-324
#???n -> 171!
sys.set_int_max_str_digits(1000000)
sys.setrecursionlimit(0x1000000)
def silnia(n):
    if n<0:
        raise UjemnaSilnia(n)
    wynik = 1
    for i in range(1,n+1):
        wynik*=i
    return wynik

def silnia_rek(n):
    if n<0:
        raise UjemnaSilnia(n)
    if n==0:
        return 1
    else:
        return n*silnia_rek(n-1)


try:
    n=int(input("podaj wartość argumentu n: "))
    print(f'silnia z n={n} wynosi: {silnia(n)}')
    print(f'silnia rekurencyjna z n={n} wynosi: {silnia_rek(n)}')
    print(f'silnia factorial: {math.factorial(n)}')
except ValueError as f:
    print(f)
except UjemnaSilnia as ve:
    print(ve)
except Exception as r:
    print(r)

#print(f'silnia z n={n} wynosi: {silnia(n)}')
print("Program nie został przerwany")

#stwórz w nowym module klasę błędu UjemnaSilnia, która będzie pobierać wartość  i opsywać przy wartościch
#ujemnych że wartość jest niewłaściwa dla dziedziny funkcji silnia
#zaimplementuj klasę błędu w roziwązaniu w zamian za klasę ValueError
