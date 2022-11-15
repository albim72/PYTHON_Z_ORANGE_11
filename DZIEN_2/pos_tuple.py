#dziedziczenie typu immutable
class PositiveNumberTuple(tuple):

    def __new__(cls, *numbers):
        skipped = 0
        pos_numbers = []
        for x in numbers:
            if x>=0:
                pos_numbers.append(x)
            else:
                skipped+=1
        instance = super().__new__(cls,pos_numbers)
        instance._skipped = skipped
        return instance

posnb = PositiveNumberTuple(9,4,-2,-1,0,34,-9,12,21,467,-11)
print(type(posnb))
print(posnb)
print(posnb._skipped)
