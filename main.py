class Teste:
    def __init__(self, i, j):
        self.__i = i
        self.j = j

    @property
    def i(self):
        return self.__i

    @i.setter
    def i(self, v):
        self.__i = v
 
    @property
    def i_only(self):
        return str(self.i) + 'test'

    @i_only.setter
    def i_only(self, value):
        self.__i = value

    def __str__(self):
        return f'i = {self.i} - j = {self.j}'



t = Teste(3 , 4)
print(t)
t.i = 5
print(t)

print(t.i_only)
t.i_only = 12
print(t.i_only)
# List Attributes
print(t.__dict__)
