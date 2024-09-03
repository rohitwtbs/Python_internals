from numba import njit

@njit
def fast_counter():
    counter = 0
    while counter < 1000000000:
        counter += 1
    return counter

counter = fast_counter()
print(counter)


# real    0m4.399s
# user    0m0.336s
# sys     0m0.136s