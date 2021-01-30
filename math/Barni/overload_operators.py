class Barni_Operators():
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    
    # teilen
    def teilen(self, other):
        return self.num1 / self.num2

    # subtrahieren
    def subtrahieren(self, other):
        return self.__sub__(other)

    #def write(self):

    # / operator
    def __truediv__(self, other):
        return self.teilen(other)
    
    # - operator
    def __sub__(self, other):
        return Barni_Operators(self.num1 - other.num1, self.num2 - other.num2)

    # write
    def __str__(self):
        return "Subtrahieren: %d - %d" % (self.num1, self.num2)

a = Barni_Operators(2,3)
b = Barni_Operators(3,2)

c = a - b
d = a.subtrahieren(b)
print(c)
print(d)