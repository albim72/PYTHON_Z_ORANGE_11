liczby = [434,4,2,56,2,-6,0,2,13,166,58,556,-999]
print(liczby)
print(type(liczby))
print(liczby[3])
print(liczby[2:6])

s = "lajkonik"
print(s)
print(type(s))
print(s[0])
print(s[1])
print(s[3:5])

elements = [[45,"jedynka",False],45,12,True]

print(elements[0])
print(elements[0][1])
print(elements[0][1][2])
print(True+4)

nb = liczby
np = list(liczby)
nq = liczby[:]
print(f"nb: {nb}")
print(f"liczby: {liczby}")
print(f"np: {np}")
print(f"nq: {nq}")

liczby[2:4] = [34,1,7,8,99,2,"Leon",True]

print(f"nb: {nb}")
print(f"liczby: {liczby}")
print(f"np: {np}")
print(f"nq: {nq}")

liczby[len(liczby):] = [45,7,"t"]
liczby[-1:] = [45,7,"t"]
print(liczby)

print(liczby[-1])
print(liczby[-16:0])

nm = [4,5]

liczby = liczby + nm

lb = [5,3,6,26,-2]
print(sorted(lb))
print(lb)
lb.sort()
print(lb)

#z lity liczby wybierz wszyskie elmenty z pozycji nieparzystch i ulokuj w nowej liście nbnieparz

nbnieparz = liczby[1::2]
print(nbnieparz)

#wypisz słowo odwrotnie
s = "Pomarańcza"
sw = s[::-1]
print(f"{s} -> {sw}")
