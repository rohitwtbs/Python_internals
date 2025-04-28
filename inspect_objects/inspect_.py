import inspect


class Prime():
    def __init__(self):
        pass
    def is_prime(self):
        pass



def check_objects(obj):
    #  this is not working as an instance is passed
    # code = inspect.getsource(obj)
    code = inspect.getsource(obj.__class__)
    print("Source code:\n", code)
    pass


p = Prime()
check_objects(p)