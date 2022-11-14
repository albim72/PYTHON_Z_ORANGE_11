#przykład 1
def witaj(imie):
    return f"Miło Cię ponownie widzieć {imie}"

def konkurs(imie,punkty):
    return f"uczestnik konkursu: {imie}, liczba punktów: {punkty}"

def osoba(funkcja,*args):
    return funkcja(*args)

print(osoba(witaj,"Leon"))
print(osoba(konkurs,"Olga",56))

#przykład 2

def rejestracja(oplata):
    def lista():
        return "jesteś na liście zawodników"
    def brak():
        return "jeśli chcesz potwierdzić swoją obecność na liście startowej uzupełnij wpłatę."
    def error():
        return "wpisz 1 - wpłata, 0 - brak wpłaty"

    if oplata == 1:
        return lista
    elif oplata == 0:
        return brak
    else:
        return error

print(rejestracja(1)())
print(rejestracja(0)())
print(rejestracja(12)())


#przykład 3

def startstop(funkcja):
    def wrapper(*args):
        print("startowanie procesu....")
        funkcja(*args)
        print("kończenie procesu...")
    return wrapper

def zawijanie(w_co):
    print(f"zawijanie czekoladek w {w_co}")

zw = startstop(zawijanie)
zw("sreberka")

@startstop
def dmuchanie(czego):
    print(f'dmuchanie {czego} na imprezę...')

dmuchanie("baloników")

@startstop
def fx(n):
    print(f"wynik = {n*2-1}")

