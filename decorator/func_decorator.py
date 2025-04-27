def log_execution(param):
    print("Decorator function called")
    pass



@log_execution
def add(x,y):
    return x + y


add(1,2)