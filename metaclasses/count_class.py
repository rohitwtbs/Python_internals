class CountMeta(type):
    count = 0
    def __new__(cls, name, bases, dct):
        print(f"Creating class {name} with bases {bases} and dct {dct}")
        cls.count += 1
        return super().__new__(cls, name, bases, dct)

class A(metaclass=CountMeta): pass
class B(A): pass
class C(B): pass

print(CountMeta.count)


# what happens if this is a normal class ?


class CountClass:
    count = 0
    def __init__(self):
        CountClass.count += 1
class A(CountClass): pass
class B(A): pass
class C(B): pass
print(CountClass.count)