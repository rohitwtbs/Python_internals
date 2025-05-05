class MyStaticMethod:
    def __init__(self,func):
        self.func = func
        print("MyStaticClass called")

    def __get__(self, instance, owner):
        return self.func
    

class Car:
    def __init__(self):
        print("Car created")
        pass

    @MyStaticMethod
    def start():
        print("Car started")

class BMW:
    def __init__(self):
        print("Car created")
        pass

    def start():
        print("Car started")

Car.start()
BMW.start()

c= Car()
c.start()

b = BMW()
b.start()

