# # Function a block of code that can be executed multiple times 
# def sum(a,b):  # a and b are parameters 
#     c = a+b   
#     print(c) 
#     d = a*b 
#     return c  # return is used to return from function area to the caller 

# a = 5 
# b = 3 
# sum(a,b)
# print()


# ## if function body does not have anything to return 
# def my_funct():
#     pass # just to avoid syntax error when function body is empty

# my_funct()

# ## mutable objects as arguments will be modified in place

# def increase(person):
#     person['age'] +=1 
#     # person_copy = person.copy() # to avoid mutation of the original object
#     return person 
# person_one = {
#     'name': 'Bob',
#     'age': 21 
# }
# increase(person_one)
# print(person_one['age']) # Output: 22

# ## immutable objects as arguments will not be modified in place
# ## better to create copy of the object before modifying it


# ## Positional arguments
# def greet(name, greeting="Hola"): # default value for greeting is "Hola"
#     print(f"{greeting}, {name}!")

# greet("Alice", "Hello") # Output: Hello, Alice!
# greet("Rish") # output: Hola, Rish!



# # Function can also take multiple arguments using *args and **kwargs

# def Sum_nums (*args):
#     print(args) # args is a tuple of all the positional arguments passed to the function
#     # we cant add in args as it is a tuple but we can convert it to a list and then add it 
#     total = sum(args) # sum is a built-in function that takes an iterable and
#     for arg in args:
#         print(arg)
#     return sorted(args)  # it will return a sorted list 

# Sum_nums(2,3,4,5,6,77,80)  



# ## kwargs is a dictionary of all the keyword arguments passed to the function
# def get_posts_info(**person):
#     print(person)
#     print(type(person))
#     info = (
#         f"{person['name']} is {person['age']} years old and has {person['posts']} posts."
#     )
#     return info 
# info = get_posts_info(name='Bod',posts_qty=25) # sending arguments as dictionary
# print(info) 
def my_function(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

my_function(1, 2, 3, name="Alice", age=30)


def update_car_info(**car):
   car['is_available'] = True
   return car  
result = update_car_info(brand="Toyota",price=20000)
print(result)



from datetime import date 

def get_weekday():
    return date.today().strftime("%A") # it will return the current day of the week as a string

def create_new_port(post,weekday=get_weekday()):
    post_copy = post.copy()
    post_copy['created_at'] = weekday
    print(f"Creating new post on {weekday}: {post}")
    return post_copy 
initial_post = {
    'title': 'My First Post',
    'id': 243
}
post_with_weekday = create_new_port(initial_post)
print(post_with_weekday) # 



## Callback function is a function that is passed as an argument to another function and is called inside that function

def print_number_info(num):
    if (num % 2 == 0):
        print(f"{num} is even")
    else:
        print("Entered number is odd ")

def process_numbers(numbers, callback):
    callback(numbers) # calling the callback function with the numbers as argument

entered_num = int(input("Enter any number: "))
process_numbers(entered_num, print_number_info)


a = 10 
def myfunc():
    a = True 
    global b  # global keyword is used to declare that a variable is global and can be accessed and modified inside the function.
    b = 15 
    print(a) 
    print(b) 

myfunc ()
print(a) # 10 # because a is defined in the global scope and is not modified by the function, it retains its value of 10 outside the function.
print(b) # 15 # because b is declared as global inside the function, it can be accessed and modified outside the function, and retains its value of 15.


## to import from other file
from main import my_function # importing the function my_function from the file main.py
import main # just to show that we can import the whole file and then use the function from it