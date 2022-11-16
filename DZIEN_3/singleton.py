class Singleton(type):
    _instances ={}
    def __call__(cls,*args,**kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args,**kwargs)
        return cls._instances[cls]

class RegularClass:
    pass

a = RegularClass()
b = RegularClass()

print(a==b)

class Sing(metaclass=Singleton):
    pass

x = Sing()
y = Sing()

print(x==y)


