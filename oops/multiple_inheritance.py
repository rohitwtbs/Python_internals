

class A():
    def __init__(self):
        pass
    def check(self):
        a=10
        print(a)

class B():
    def __init__(self):
        pass

    def check(self):
        a=11
        print(a)

class C(A,B):
    def __init__(self):
        pass
    def call(self):
        super().check()
    def check(self):
        a=12
        print(a)

class D(B,A):
    def __init__(self):
        pass
    def call(self):
        super().check()
    def check(self):
        a=13
        print(a)

obj_c = C()
obj_c.check()
obj_c.call()

obj_d = D()
obj_d.check()
obj_d.call()
# check the method order for a particular class 
# python uses C3 linearization algorithm to evaluate the order
# sample output (<class '__main__.D'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>)
print(D.__mro__)