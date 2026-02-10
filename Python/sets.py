## sets are unordered collections of unique elements
my_fruits = {"apple", "banana", "cherry"}
print(my_fruits) # Output may be in any order as sets are unordered

## No duplicate elements allowed in sets
my_fruits = {"apple", "banana", "cherry", "apple"}
print(my_fruits) # Output will only contain unique elements: {'apple', 'banana', 'cherry'}

## Length of the set
my_fruits = {"apple", "banana", "cherry"}
print(len(my_fruits)) # Output: 3   

# elements have no indexes 
print(my_fruits[0]) # This will raise a TypeError as sets do not support indexing   

# You cant add mutable objects like lists or dictionaries to a set  
list_set = {1, 2, [3, 4]} # This will raise a TypeError as lists are mutable and cannot be added to a set
dict_set = {1, 2, {'key': 'value'}} # This will raise a TypeError as dictionaries are mutable and cannot be added to a set
print(dict_set)