import inspect


class Prime():
    def __init__(self):
        pass
    def is_prime(self):
        pass



def check_objects(obj):
    code = inspect.getsource(obj)
    print("Source code:\n", code)
    pass


p = Prime()
check_objects(p)