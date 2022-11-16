class MojaKlasaBledu(Exception):
    def __init__(self,*args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        print('wywołanie funkcji string')
        if self.message:
            return f'MojaKlasaBledu: {self.message}'
        else:
            return f'MojaKlasaBledu została wykonana'

n = input("podaj literę alfabetu: ")
try:
    if n == "a":
        raise MojaKlasaBledu("mamy duży problem...nie podawaj a!")
    else:
        print("wszytko OK")

except MojaKlasaBledu as mkb:
    print(mkb)
