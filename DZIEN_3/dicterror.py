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

class CustomInFloatDict(dict):
    empty_dict ={}

    def __init__(self,key=None, value=None):
        if key is None or value is None:
            self.get_dict()
        elif not isinstance(key,(tuple,list,)) or not isinstance(value,(tuple,list,)):
            raise KeyValueConstructError(key,value)
        else:
            zipped = zip(key,value)
            for k,val in zipped:
                if not isinstance(val,(int,float)):
                    raise IntFloatValueError(val)
                dict.__setitem__(self,k,val)
                
    def get_dict(self):
        return self.empty_dict
    
    def __setitem__(self, key, value):
        if not isinstance(value,(int,float)):
            raise IntFloatValueError(value)
        return dict.__setitem__(self,key,value)
            
