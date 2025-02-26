def Stack():
    _items = []

    def push(item):
        _items.append(item)

    def pop():
        return _items.pop()

    def closure():
        pass

    closure.push = push
    closure.pop = pop
    return closure

s = Stack()
s.push(2)
s.push(7)
s.push(9)
s._items
#Traceback (most recent call last):
# Traceback (most recent call last):
#   File "C:\Users\rohit\OneDrive\Documents\github\Python_internals\closures\protected_variable_mimic.py", line 21, in <module>
#     s._items
# AttributeError: 'function' object has no attribute '_items