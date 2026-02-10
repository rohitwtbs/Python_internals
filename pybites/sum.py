def sum_numbers(numbers=None):
    print(numbers)
    if(numbers == None):
        return sum(range(1,101))
    else:
        return sum(numbers)
    pass


print(sum_numbers([1,2,3,4,5]))
print(sum_numbers(range(1,11)))