class CountMeta(type):
    count = 0
    def __new__(cls, name, bases, dct):
        cls.count += 1
        return super().__new__(cls, name, bases, dct)

class A(metaclass=CountMeta): pass
class B(A): pass
class C(B): pass

print(CountMeta.count)
