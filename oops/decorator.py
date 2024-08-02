
def call_before_add(func):
    def wrapper(a,b):
        print("call in decorator")
        print("call was from", func.__name__)
        return func(a+2,b+2)
    return wrapper


def decrement_two(func):
    def wrapper(a,b):
        print("call was from-> ", func.__name__)
        return func(a-2,b-2)
    return wrapper


@decrement_two
@call_before_add
def add(a,b):
    print(a+b)
    return a+b


add(2,4)



# def make_pretty(func):

#     def inner():
#         print("I got decorated")
#         func()
#     return inner

# @make_pretty
# def ordinary():
#     print("I am ordinary")

# ordinary()  


# def smart_divide(func):
#     def inner(a, b):
#         print("I am going to divide", a, "and", b)
#         if b == 0:
#             print("Whoops! cannot divide")
#             return

#         return func(a, b)
#     return inner

# @smart_divide
# def divide(a, b):
#     print(a/b)

# divide(2,5)

# divide(2,0)