#budowa słownika poprzez zadanie listy lub krotki z kluczami i wartościami
#wartości słownika mogą być tylko typu int albo float

class IntFloatValueError(Exception):
    def __init__(self,value):
        self.value = value

    def __str__(self):
        return f"wartość: {self.value} jest niewłaściwa! Akceptowalne są tylko wartości w typie:" \
               f" int oraz float."

class KeyValueConstructError(Exception):
    def __init__(self,key,value):
        self.key=key
        self.value=value

    def __str__(self):
        return f"klucze i wartości powinny być przekazywane w listach lub krotkach. " \
               f"klucz: {self.key} jest w typie: {type(self.key)}, " \
               f"wartość: {self.value} jest w typie: {type(self.value)}."
