def add_numbers(x, y):
    return x + y

add_five = lambda y: add_numbers(5, y)

from functools import partial

add_five_anotherVersion = partial(add_numbers, 5)

print(add_five(10))
print(add_five_anotherVersion(11))