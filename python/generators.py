#Python generators are a specialized type of function used to create iterators in a memory-efficient way.
# Unlike regular functions that return a single value and exit, generators yield values one at a time, pausing their execution state between each call. 
def simple_generator():
    yield 1
    yield 2
    yield 3
    yield 4
# Using the generator
gen = simple_generator()    
print(next(gen))  # Output: 1
print(next(gen))  # Output: 2
print(next(gen))  # Output: 3
print(next(gen))  # Output: 4
# If we call next() again, it will raise StopIteration
# print(next(gen))  # Uncommenting this line will raise StopIteration   
# Generator expression: A more concise way to create generators using a syntax similar to list comprehensions
squared_gen = (x**2 for x in range(5))  # Generator expression for squares of numbers 0-4
print(squared_gen) # but it is same as list comprehension but it will not store all values in memory
for square in squared_gen:  
    print(square)
    print(next(square))

import sys

# List comprehension
list_comp = [x for x in range(10000)]
# Generator expression
gen_exp = (x for x in range(10000))

print(sys.getsizeof(list_comp)) # Output: ~85,000 bytes
print(sys.getsizeof(gen_exp))   # Output: ~100 bytes (No matter how big the range!)

