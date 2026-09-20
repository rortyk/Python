class Temperature(object):

    def __init__(self, value):
        self.value = float(value)

    def __eq__(self, tmp_value):
        return self.value == tmp_value.value

    def __str__(self):
        return str(self.value) + '°C'

    def __lt__(self, tmp_value):
        return self.value < tmp_value.value

    def __repr__(self):
        return f'{self.__class__.__name__}({self.value})'

t1 = Temperature(25)
t2 = Temperature(25.0)
t3 = Temperature(-3.5)

print(t1)
print(t1 == t2)
print(t3 < t1)
print([str(t) for t in sorted([t1, t3, Temperature(100)])])
print(sorted([t1, t3, Temperature(100)]))