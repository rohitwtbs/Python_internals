def sum_numbers(numbers=None):
    print(numbers)
    if(numbers == None):
        return sum(range(1,101))
    else:
        sum(numbers)
    pass



sum_numbers(range(1,11))