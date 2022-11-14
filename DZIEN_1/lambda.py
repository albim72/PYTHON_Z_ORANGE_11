print((lambda e:e**3)(5))
b = lambda u:u+98
print(b(6))

def bx(u:int)->int:
    return u+98

print(bx(6))
print(bx(8.8))

h = lambda a,b,c=5:a/(b-c)
print(h(5,8,2))
print(h(5,8))

def ob(k):
    return lambda a,b:a**k-b

print(ob(7)(6,8))

#zadanie1
#stwórz listę nparz i przekaż do niej wszysktie wartości parzyste z listy num
#użyj funkcji standardowej filter (funkcja wy zszego rzędu) - > paramtrem 0 tej funkcji jest inna funkcja,
#parametrem 1 -źródło danych.

num = [67,3,4,-9,0,14,7,99,56,79,1,1990]

h = filter(lambda x:x%2 == 0,num)
print(type(h))
nparz = list(filter(lambda x:x%2 == 0,num))
print(nparz)

def pp(x):
    return x%2==0

nparz = list(filter(pp,num))
print(nparz)

#stwórz listę cube i przekaż do niej wsyztskie wartości z listy num podniesione do potęgi 3!!

cube = list(map(lambda x:x**3,num))
print(cube)

