def outer_fucntion():
    def inner_function():
        print("inner fucntion executed")
    return inner_function

closure = outer_fucntion()
# closure = outer_fucntion
# execute the closure now
print(closure)
closure()