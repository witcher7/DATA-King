## Python Data types 
# Integer
from tokenize import String


a = 10
print("Integer:", a)
# Float
b = 10.5
print("Float:", b)
# String
c = "Hello, World!" 
print("String", c)    

# Boolean 
d = True 
print("Bool: ",d)

# List == Array 
list = [1,2,3,4,5]
print(list)

# Dictionary 
our = {
     'min': 5,
     'max': 10
}
print(type(our)) # type is used to print the type of data


### Functions are piece of code that could be used again and again
def my_func(a,b): ## parameters of function describe the values and arguments
    a = a+ 1 
    c = a+b   
    return c  ## return result 

## BUilt in functions 
# print() 
# type() 
# id()  ## tells the memory location of variable 
# sum() 
# input() 
# round()
# min() 
# max()
a = 100 
b = 200 
print(min(a,b))

print(dir(__builtins__))

## static and dynamic typing
# String a = "abc"

# int b = 10 
#  In python we don't need to declare data types
# it is dynamically typed language
a = "abc"
a = 100 
## this is allowed in python 


            MEMORY 
Myname ----> object 
profile_photo ----> object
age ----> object
# variable name points to object in memory

## REFERENCES TO ONE OBJECT
x = 100
y = x
print(id(x))# same location 
print(id(y)) # same location

## isinstance() function is used to check the type of object 
print(id(x))
print(isinstance(x, type))