

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

obj_c = C()
obj_c.check()
obj_c.call()
