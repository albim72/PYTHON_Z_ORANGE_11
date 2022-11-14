animal = ("pies","kot","lew","mysz","krokodyl","pies")

print(animal)
print(type(animal))

print(animal.index("lew"))
print(animal.count("pies"))

print(animal[3])

for a in animal:
    print(a)

an = ("pająk","ryba")
animal = animal + an
print(animal)

#zamień "mysz" na "szczur"

an_list = animal[:animal.index("mysz")] + ("szczur",) + animal[animal.index("mysz")+1:]
print(an_list)

an_sec = list(animal)
an_sec[an_sec.index("mysz")] = "szczur"
animal = tuple(an_sec)

print(animal)

#zbiór

drzewa = {"topola","sosna","buk","dąb","baobab"}
print(drzewa)
print(drzewa)
print(drzewa)

las = ["grab","jodła","brzoza","grab","dąb"]
drzewa.update(las)
print(drzewa)

for i in drzewa:
    print(i)


l = [5,3,5,24,7,8,23,6,12,6,7,3,8,3,3,3,1,5,5,12,7,7,7,2,2,2,2,1,98,677]
l = list(set(l))
l.sort()
print(l)

nb = set({56,7,8,9,12,89,0,6,3,1,2,87})
print(nb)

#słowniki

samochod = {
    "marka":"Ford",
    "model":"Mustang",
    "rok":1976
}

print(samochod)
print(type(samochod))

print(samochod["marka"])
samochod["rok"] = 2017

print(samochod)

samochod["poj"] = 4.5
print(samochod)

print(samochod.items())
print(samochod.keys())
print(samochod.values())

print("_________ klucze _____________")
for i in samochod:
    print(i)

print("_________ wartości _____________")

for i in samochod.values():
    print(i)

print("__________ items ______________")

for i,j in samochod.items():
    print(f"{i}:{j}")
