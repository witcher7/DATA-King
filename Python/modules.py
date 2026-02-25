# # module_one.py 
# def print__name():
#     print(name) 

# # module_two.py
# import module_one as n 
# print(module_one.__name__)
# print(type(module_one))
# print(dir(module_one))
# module_one.print__name("Rishabh")
# n.print__name("Rishabh") # if module is imported with as alias 


# from utils import Comment,hello, my_name 
# from utils import * # imports everything from the module but is not recommended as it can lead to namespace pollution and make code harder to read and maintain

# from folder.file import function_name # to import a specific function from a module located in a folder.

# BUilt in modules
# import math
# import random
# import os 
# import sys 
# import time  
# import smtplib 
# import csv 
# import calender 
# import datetime 
# import zipfile 

# import math 
# print(math.pi)
# print(math.pow(2, 3))
# print(dir(math))


## if __name__ == "__main__": # this is a common Python idiom used to check if a script is being run directly
#  or imported as a module. 
# #When a Python file is run directly, the special variable __name__ is set to "__main__". 
# If the file is imported as a module in another script, __name__ will be set to the name of the module. 
# By using this condition, you can ensure that certain code only runs when the script is executed directly, and not when it is imported.
##    print()
print(__name__)

# for example, if you have a Python file named my_module.py with the following code:
# def greet():
#     print("Hello, World!")
# if __name__ == "__main__":
#     greet()
# When you run my_module.py directly, it will output "Hello, World!" because the condition __name__ == "__main__" is true.
#  However, if you import my_module in another script, the greet() function will be available for use, but it will not execute 
# automatically because the condition will be false.
# for example, if you have another Python file named main.py with the following code:
import other as np 
np.greet() 
# When you run main.py, it will also output "Hello, World!" because you are explicitly calling the greet() 
# function from the my_module.
# in short the __name__ == "__main__" condition is used to control the execution of code in a Python script, allowing you to differentiate between when the script is run directly and when it is imported as a module.

def initialise():
    print("This is the initialise function")
def main() :
    print("Running the main function") 
    
if __name__ == "__main__":
    initialise()
    main()
    print("This code is running directly and not imported as a module")




# Random module example
import random
# Generate a random integer between 1 and 10
random_integer = random.randint(1, 10)
random_float = random.random() # generates a random float between 0 and 1
print(random_integer)
print(random_float)
print(random.choice(['apple', 'banana', 'cherry'])) # randomly selects an element from a list

# Shuffle 
mylist = [1,2,3,4,5,6,7]
random.shuffle(mylist)
 
 #
 # print(random.choice("bodgan"))
 # print(random.choice((1,3,4,10)))
 # print(random.choice({'a': 10,'b':True}))

 #   Choices
print(random.choices(['apple', 'banana', 'cherry'], k=3)) # randomly selects 3 elements from a list with replacement
# choices can select the same element multiple times, while choice will select only one element.
print(''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890', k=12)))

                             # randomly selects 5 characters from the uppercase alphabet with replacement

# Import Secrets
