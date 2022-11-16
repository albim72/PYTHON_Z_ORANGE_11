class MultiBases(type):
    def __new__(cls, clsname,bases,attrs):
        if len(bases) >1:
            raise TypeError("zabraniamy wielodziedziczenia!")
        return super().__new__(cls, clsname,bases,attrs)

class Base(metaclass=MultiBases):
    pass

class A(Base):
    pass

class B():
    pass

class C(A,B):
    pass
