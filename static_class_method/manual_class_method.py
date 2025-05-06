

class Myclasmethod:
    def __init__(self, func):
        self.func = func
        print("MyClassMethod called")
    

    def __get__(self, instance, owner):
        return self.func.__get__(None, owner)

class Car:
    def __init__(self):
        print("car created")
    @Myclasmethod
    def start(cls):
        print("car started")