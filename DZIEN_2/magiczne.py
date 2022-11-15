#__call__

class CallClass:

    def __init__(self):
        print("instancja CallClass utworzona...")


    def __call__(self):
        print("instancja jest wołana przez funkcję magiczną call...")


er = CallClass()

er()

#__missing__

class MojSlownik(dict):
    def __missing__(self, key):
        self[key]=0
        return f"nie było takiego klucza! dodałem: {key}"




konkurs = {'Tomasz':67,'Alicja':73,'Roman':56}
md = MojSlownik(konkurs)

print(md['Alicja'])
print(md['Euzebiusz'])
print(md['Euzebiusz'])

#print(konkurs['Euzebiusz'])

#__getattribute__

class Funkcyjny:
    def __init__(self,abc):
        self.abc = abc

    def __getattribute__(self, name):
        return f"Funkcyjny nie posiada atrybutu: {name}"

f = Funkcyjny("abc")
print(f.abc)
print(f.drzewko)
