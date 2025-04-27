def log_execution(param):
    print("Decorator function called")
    pass



@log_execution
def add(x,y):
    return x + y


add(1,2)

# Notes
# when no return statement is present in the decorator function, it throws an error
# Traceback (most recent call last):
#   File "/Users/rohitwtbs/Documents/github/Python_internals/decorator/func_decorator.py", line 12, in <module>
#     add(1,2)
# TypeError: 'NoneType' object is not callable