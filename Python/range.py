my_range = range(5)
for num in my_range:
    print(num)

# range is an immutable sequence type that generates a sequence of numbers based on the specified start, stop, and step values. It is commonly used in for loops to iterate over a sequence of numbers. The range() function can take one, two, or three arguments:


## Built in functions for sequences 
len()
sum()
filter()
map()
sorted() 
reversed()
zip() #  
fruits = ['apple', 'banana', 'cherry']
quantity = [5, 3, 8]
zipped = zip(fruits, quantity) # Combines the two lists into a list of tuples
print(list(zipped)) # Output: [('apple', 5), ('banana', 3), ('cherry', 8)]


min()
max() 

