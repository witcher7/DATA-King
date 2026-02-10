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

# cant delete an element from a set using index as sets are unordered and do not support indexing
my_fruits = {"apple", "banana", "cherry"}   
del my_fruits[0] # This will raise a TypeError as sets do not support indexing and cannot delete elements by index


## To create empty set ,
# you need to use the set() constructor, as using {} will create an empty dictionary instead of a set.
my_set = set()  


## SET METHODS 
my_set.add(1) # Adds an element to the set
my_set.union({2, 3}) # Returns a new set that is the union of the set and another set

p1 = {1, 2, 3}
p2 = {1, 2,}
all = p1.union(p2) # Returns a new set that is the union of p1 and p2
print(all) # Output: {1, 2, 3}

my_set.remove(1) # Removes an element from the set; raises KeyError if the element is not found
my_set.discard(2) # Removes an element from the set if it is present; does nothing if the element is not found
my_set.intersection({2, 3}) # Returns a new set that is the intersection of the set and another set
my_set.difference({2, 3}) # Returns a new set that is the difference of the set and another set
my_set.clear() # Removes all elements from the set
my_set.copy() # Returns a shallow copy of the set
my_set.pop() # Removes and returns an arbitrary element from the set; raises KeyError if    