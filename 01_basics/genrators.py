
"""Python generators are a powerful tool for creating iterators using a memory-efficient approach known as lazy evaluation"""

def my_gen():
    yield 1
    yield 2
    yield 3


x=my_gen()
print(next(x))  # Output: 1
print(next(x))  # Output: 2
print(next(x))  # Output: 3