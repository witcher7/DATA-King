print("")
 #-> print("") is a python builtin function that outputs an empty line to the console.
 #-> it prints whatever valid value or values are given 
 #-> () are representation of a function  

print(12.6)
print("Hello World")
print("Welcome","Hi","Good Bye")
print("Welcome",30,"True",True)

# Data Types in Python 
# -> int - Integer (Whole Numbers) # -> ex 10, -5, 0
# -> float - Floating Point Numbers (Decimal Numbers) # -> represented with a decimal point ex 12.6
# -> str - String (Text) # -> enclosed in single or double quotes ex 'Hello' or "Hello" 
# -> bool - Boolean (True or False) # -> represents truth values ex True or False
#-> print() can take multiple arguments separated by commas and prints them with a space in between

# to know data type of a value use type() function
print(type(10))        #-> <class 'int'>
print(type(12.6))     #-> <class 'float'>
print(type("Hello"))  #-> <class 'str'>
print(type(True))     #-> <class 'bool'>

print('Rishabh','Gulati', sep="-")
# -> sep is a parameter of print() function that specifies the separator between multiple values
# -> default separator is a space " "
# -> in this case, the separator is set to "-" so the output will be Rishabh-Gulati
print("My age is 30", end ='\t')
# \t is an escape sequence that represents a tab space
print("I live in India")
# -> end is a parameter of print() function that specifies what to print at the end of the output
# -> default end character is a newline '\n'
# -> in this case, the end character is set to a tab space '\t' so the output will be printed in the same line with a tab space in between  
print("Hello", end=' ')
print("World")
# -> here end is set to a space ' ' so the output will be Hello World in the same line with a space in between          

# MATHEMATICAL OPERATIONS
# + : Addition
# - : Subtraction
# * : Multiplication
# / : Division
# // : Floor Division
# % : Modulus
# ** : Exponentiation

# COMPARISON OPERATORS
# == : Equal to
# != : Not equal to
# > : Greater than
# < : Less than
# >= : Greater than or equal to
# <= : Less than or equal to
# Comparison operators return boolean values (True or False)

# LOGICAL OPERATORS
# and : Logical AND
# or : Logical OR
# not : Logical NOT 

# isinstance() function
# -> used to check if an object is an instance of a specific class or data type
print(isinstance(10, int))        #-> True
print(isinstance(12.6, float))    #-> True
print(isinstance("Hello", str))   #-> True
print(isinstance(True, bool))      #-> True
print(isinstance(10, float))      #-> False


### PYTHON DATA STRUCTURES ###
# LIST
my_list = [10, 20.5, "Hello", True]
print(my_list)
# -> list is a collection of items that can be of different data types
# -> list is mutable (can be changed)
# -> list is defined using square brackets []
# type(list) -> <class 'list'>
# len() function returns the number of items in a list
print(len(my_list))  #-> 4  
# Retrieving items from a list using indexing
print(my_list[0])    #-> 10
print(my_list[2])    #-> Hello
# Modifying items in a list
my_list[1] = 30.5
print(my_list)       #-> [10, 30.5, 'Hello', True]
# Adding items to a list using append() method
#   -> append() adds an item to the end of the list
my_list.append("World")
print(my_list)       #-> [10, 30.5, 'Hello', True
# inserting items to a list using insert() method
#   -> insert() adds an item at a specific index
my_list.insert(1, "New Item")
print(my_list)       #-> [10, 'New Item', 30.5, 'Hello', True, 'World']
# Removing items from a list using remove() method
#   -> remove() removes the first occurrence of a specific item
my_list.remove("Hello")
print(my_list)       #-> [10, 'New Item', 30.5, True, 'World']
# Removing items from a list using pop() method
#   -> pop() removes an item at a specific index and returns it
removed_item = my_list.pop(2)
print(removed_item)  #-> 30.5
print(my_list)       #-> [10, 'New Item', True, 'World']
# Checking if an item exists in a list using 'in' keyword
print("World" in my_list)  #-> True
print(50 in my_list)       #-> False
# Iterating through a list using a for loop
for item in my_list:    
    print(item)
# del - used to delete an entire list or specific item from a list
del my_list[1]  # deletes item at index 1
print(my_list)  #-> [10, True, 'World']
del my_list     # deletes the entire list
# print(my_list)  #-> This will raise an error as my_list is deleted

# ALL METHODS FOR LIST 
# append(), insert(), remove(), pop(), clear(), index(), count(), sort(), reverse(), copy(), push(),del(), extend()

# list.append(item) - adds an item to the end of the list
list.append(50)
print(my_list)  #-> [10, True, 'World', 50]

# list.insert(index, item) - adds an item at a specific index
list.insert(2, "Inserted Item")
print(my_list)  #-> [10, True, 'Inserted Item', 'World', 50]

# list.remove(item) - removes the first occurrence of a specific item
list.remove(True)
print(my_list)  #-> [10, 'Inserted Item', 'World', 50]

# list.pop(index) - removes an item at a specific index and returns it
list.pop(1)
print(my_list)  #-> [10, 'World', 50]   

# list.clear() - removes all items from the list
list.clear()
print(my_list)  #-> []  
# list.index(item) - returns the index of the first occurrence of a specific item
list = [10, 20, 30, 20]
print(list.index(20))  #-> 1    

# list.count(item) - returns the number of occurrences of a specific item
list = [10, 20, 30, 20]
print(list.count(20))  #-> 2    

# list.sort() - sorts the items in the list in ascending order
list.sort()
print(list)  #-> [10, 20, 20, 30]   

# list.reverse() - reverses the order of items in the list
list.reverse()
print(list)  #-> [30, 20, 20, 10]   

# list.copy() - returns a shallow copy of the list
list_copy = list.copy()
print(list_copy)  #-> [30, 20, 20, 10]
# if I do list_copy[0] = 100, it will not affect the original list
# if num= [10,20,30] 
# num = num2
# id(num) and id(num2) will be same
# but if I do num2 = num.copy()
# id(num) and id(num2) will be different    

# list.extend(iterable) - adds items from an iterable (like another list) to the end of the list
list2 = [40, 50]
list.extend(list2)
print(list)  #-> [30, 20, 20, 10, 40, 50]   
# push() - not a built-in method for lists in Python, but can be simulated using append()
list.append(60)  # simulating push operation
print(list)  #-> [30, 20, 20, 10, 40, 50, 60]   
# del() - used to delete an entire list or specific item from a list
del list[0]  # deletes item at index 0
print(list)  #-> [20, 20, 10, 40, 50, 60]

# Shallow copy vs Deep copy
import copy     
original_list = [[1, 2, 3], [4, 5, 6]]
shallow_copied_list = copy.copy(original_list)
deep_copied_list = copy.deepcopy(original_list) 
# The difference between shallow copy and deep copy is that a shallow copy creates a new object but does not create copies of nested objects, while a deep copy creates a new object and recursively copies all nested objects.
original_list[0][0] = 10
print(shallow_copied_list)  #-> [[10, 2, 3], [4, 5, 6]] (affected by change in original list)
print(deep_copied_list)     #-> [[1, 2, 3], [4, 5, 6]] (not affected by change in original list)    


## SLICING 
# Slicing is a way to extract a portion of a list (or other sequence types) using a range of indices
my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# Syntax: list[start:end:step]
# start - starting index (inclusive)
# end - ending index (exclusive)        
# step - step size (optional)
# Examples of slicing
print(my_list[2:5])      #-> [30, 40, 50] (from index 2 to 4)
print(my_list[:4])       #-> [10, 20, 30, 40] (from start to index 3)
print(my_list[5:])       #-> [60, 70, 80, 90, 100] (from index 5 to end)
print(my_list[::2])     #-> [10, 30, 50, 70, 90] (every second item)
print(my_list[1:8:3])   #-> [20, 50, 80] (from index 1 to 7 with step size of 3)
print(my_list[-5:-1])    #-> [60, 70, 80, 90] (from index -5 to -2)
print(my_list[::-1])    #-> [100, 90, 80, 70, 60, 50, 40, 30, 20, 10] (reverses the list)   

# List comprehension
# List comprehension provides a concise way to create lists
# Common applications are to make new lists where each element is the
# result of some operations applied to each member of another sequence 
# or iterable, or to create a subsequence of those elements that satisfy a certain condition
# Syntax: [expression for item in iterable if condition]
# Example:
squares = [x**2 for x in range(10)]
print(squares)  #-> [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
# Example with condition:
even_squares = [x**2 for x in range(10) if x % 2 == 0]
print(even_squares)  #-> [0, 4, 16, 36, 64]
[input("enter name") for name in range(5)]


numbers = [int(num) for num in input("enter numbers").split(",")]
print(numbers)
# In above example we are taking input from the user as numbers and spliting them 
