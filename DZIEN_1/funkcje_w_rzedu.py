def filtrowanie(dane,test):
    plus=[]
    for element in dane:
        if (test(element)):
            plus.append(element)
    return plus

def ekstra_liczba(n):
    return n>=100

nb = [119,0,-6,17,95,121,-70,231]
print(filtrowanie(nb,ekstra_liczba))

def mapowanie(dane,transformacja):
    mapa=[]
    for element in dane:
        mapa.append(transformacja(element))
    return mapa

def add_five(n):
    return n+5

print(mapowanie(nb,add_five))
