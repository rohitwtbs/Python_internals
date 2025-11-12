def increment():
    count = 0
    def inner():
        nonlocal count
        count = count + 1
    return inner



check = increment()

print(check())

print(check)
