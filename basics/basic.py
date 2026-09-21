class Money:

    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f'{self.__class__.__name__}({self.value})'

    def __str__(self):
        return f'¥{self.value}'

    def __eq__(self, other):
        if not isinstance(other, Money):
            return NotImplemented
        return self.value == other.value

    def __add__(self, other):
        return Money(self.value + other.value)

m1 = Money(100)
m2 = Money(250)

print(m1)                    # ¥100
print([m1, m2])              # [Money(100), Money(250)]
print(m1 == Money(100))      # True
print(m1 == m2)              # False
print(m1 + m2)               # ¥350
print(type(m1 + m2))         # <class '__main__.Money'>

print(Money(100) == 100)                   # False
print(Money(100) == '100')                 # False
print(Money(100) != 100)                   # True
print(Money(100) in [1, 2, Money(100)])    # True
