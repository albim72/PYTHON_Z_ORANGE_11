def liczby():
    for i in range(11):
        yield i*2

print(type(liczby()))
for p in liczby():
    print(p)

def wznowienia(n,k):
    print("wstrzymanie działania...")
    yield 33*n-k
    print("wznowienie działania...")

    print("wstrzymanie działania...")
    yield 188*n+k
    print("wznowienie działania...")

    print("wstrzymanie działania...")
    yield 456*n/k
    print("wznowienie działania...")

    print("wstrzymanie działania kolejnego")
    yield 987%(n-k)
    print("wznowienie działania ostatniego")
    yield 9
    print("ekstra tekst")

for i in wznowienia(4,7):
    print("________________________")

    print(type(i))
    print(f"zwrócono wartość: {i}")


print("_______________________________________________________")

def genret():
    for i in range(7):
        if i==5:
            print("przerywamy...")
            return 
        else:
            yield i

for t in genret():
    print(t)

