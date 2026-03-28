def deco(func):
    def wrapper(a,b):
        print("called" + func.__name__ + str(a) + str(b))
        result = func(a,b)
        print("called" + func.__name__ + str(a) + str(b) + str(result))
        return result
    return wrapper
    

@deco
def add(a,b):
    print("called add")
    return a+b
    

print(add(3,5))