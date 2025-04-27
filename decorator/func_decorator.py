def log_execution(param):
    print("Decorator function called")
    print(param.__name__)
    print(type(param))
    def inner_function(a,b):
        print("Inner function called")
        print("Executing the function...")
        print(a,b)
        param(a,b)
        print("Function executed successfully")
    return inner_function
    



@log_execution
def add(x,y):
    return x + y


print(add(1,2))

# Notes
# when no return statement is present in the decorator function, it throws an error
# Traceback (most recent call last):
#   File "/Users/rohitwtbs/Documents/github/Python_internals/decorator/func_decorator.py", line 12, in <module>
#     add(1,2)
# TypeError: 'NoneType' object is not callable


# when you donot give any param to inner function, it throws an error
# Traceback (most recent call last):
#   File "/Users/rohitwtbs/Documents/github/Python_internals/decorator/func_decorator.py", line 12, in <module>
#     add(1,2)
# TypeError: inner_function() takes 0 positional arguments but 2 were given