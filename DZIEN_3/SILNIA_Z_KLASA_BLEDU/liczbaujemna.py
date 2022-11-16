class UjemnaSilnia(Exception):

    def __init__(self,n):
        self.n = n

    def __str__(self):
        return f"Została zadana wartość: {self.n}. Wartość argumentu silnii nie możę być ujemna!"
