class MojaMeta(type):
    def __new__(cls,clsname,superclasses,attribdict):
        print("*************************************************")
        print(f"nazwa klasy: {clsname}")
        print(f"dziedziczone klasy: {superclasses}")
        print(f"zbiór atrybutów: {attribdict}")
        return type.__new__(cls,clsname,superclasses,attribdict)

class S:
    pass
class F:
    pass

class specjalna(S,metaclass=MojaMeta):
    pass

class B(specjalna):
    pass

class C(F,B):
    pass
