import math
import time

def pomiarczasu(funkcja):
    def wrapper():
        wynik =[]
        starttime = time.perf_counter()
        #print(f"czas startu:{starttime} s")
        funkcja()
        endtime = time.perf_counter()
        #print(f"czas końca:{endtime} s")
        wynik.append(endtime - starttime)
        print(wynik[0])
    return wrapper

def sleep(funkcja):
    def wrapper():
        time.sleep(0)
        return funkcja()
    return wrapper


@sleep
@pomiarczasu
def big_lista():
    sum([i**2 for i in range(1000000)])

big_lista()
big_lista()
big_lista()

# xtime =time.time()
# print(f"{xtime}")

lt = [i**2 for i in range(1000000)]


@sleep
@pomiarczasu
def big_lista_out():
    sum(lt)

big_lista_out()


def debug(funkcja):
    def wrapper(*args,**kwargs):
        print(f'wołana funkcja to: {funkcja.__name__}')
        funkcja(*args)
    return wrapper


@debug
def info(i):
    print(f"informacja: {i}")

info("kod nr 453434534")


def argumenty_dict(**kwargs):
    for key,value in kwargs.items():
        print(f"{key} -> {value}")

argumenty_dict(pierwszy = "Marcin", liczba_punkt = 5, czypracownik = True)

osoba = {
    "imie":"Jacek",
    "wiek":45,
    "33":"coś"
}

argumenty_dict(**osoba)


class cars():
    def __init__(self,*args,**kwargs):
        self.speed = args[0]
        self.color = args[1]
        self.maxspeed = kwargs["vmax"]
        self.engine = kwargs["eng"]

audi = cars(140,'czerwony',vmax=240,eng="diesel",typ="sedan")
bmw = cars(170,'czarny',45678,vmax=250,eng="elektryk")

print(audi.color)
print(audi.engine)
print(bmw.speed)
print(bmw.maxspeed)

bmw.model = "combi"
print(bmw.model)






