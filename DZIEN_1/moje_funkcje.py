

#funkcja nr 1
n=55
def policz(a,b,c,y):
    global n
    n = (a+b)*y-c + n
    return n

print(policz(3,6,1,5))
print(n)

#funckja nr 2
def zewnetrzna():
    x = "lokalnie"
    def wewnetrzna():
        nonlocal x
        x = "nielokalnie"
        print(f"wewnętrzne: {x}")
    wewnetrzna()
    print(f"zewnętrzna: {x}")

zewnetrzna()

#funkcja nr 3

def rank(*lang,nrrank):
    print(f"ranking języków programowania -> pierwsze miejsce: {lang[0]}, drugie miejsce: {lang[1]},"
          f"trzecie miejsce: {lang[2]} - ranking nr {nrrank}")

rank("Python","Java","C++","C#",nrrank=89)
