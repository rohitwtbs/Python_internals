def outer_fucntion(msg):
    def inner_function():
        print("inner fucntion executed",msg)
    return inner_function

closure = outer_fucntion("new msg")
# closure = outer_fucntion
# execute the closure now
print(closure)
closure()