import gc

gc.disable()

class Student():
    def __init__(self):
        print("object created")
        pass
    def __del__(self):
        print("object deleted")
        pass


obj = Student()
# Question why calling this executes the __del__ two times ??
# obj.__del__()

del obj
