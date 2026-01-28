### FUNCTIONS are predefined pieces of code that perform specific tasks.


# def greet(name):
#     """This function greets the person passed as a parameter."""
#     return f"Hello, {name}!"

# # we have to call the function to see the result
# print(greet("Alice"))  # Output: Hello, Alice!
# print(greet("Rishabh")) # Output: Hello, Rishabh!


# def addNumbers(a, b):
#     """This function returns the sum of two numbers."""
#     x = 100 # local variable inside the function
#     ## or 
#     ## print(a + b)
#     return a + b # return keyword sends back the result to the caller
# print(addNumbers(5, 3)) # 
# print(x) # This will raise an error because x is not defined outside the function

# Default Parameters
from profile import Profile


shop = ["apples", "bananas", "cherries", "dates", "elderberries", "figs", "grapes"]
def orders():
    items = []
    while True:
        item = input("Enter an item to add to your order (or 'done' to finish): ")
        if item =="done":
            break
        elif item not in shop:
            print("Item not available in the shop.")
        elif item in items:  
            print(f"{item} already added to your order.")
        else:
            items.append(item)
    return items

# Keyword Arguments
def describe_pet(pet_name, animal_type="dog"):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
describe_pet(pet_name="willie")  # uses default animal_type
describe_pet(pet_name="harry", animal_type="hamster")  # overrides default animal_type
describe_pet("crocodile", "gecko")  # positional arguments so output will be gecko and crocodile


# Variable-length arguments: These are used when a function needs to accept an arbitrary or unknown number of arguments.
# Arbitrary Positional Arguments (*args): A parameter prefixed with a single asterisk (*) in the function definition 
#collects all extra positional arguments into a tuple.
def add_numbers(*args):
    total = sum(args)
    print(f"Sum: {total}")

add_numbers(1, 2, 3, 4) # Output: Sum: 10
add_numbers(10, 20)    # Output: Sum: 30
add_numbers()          # Output: Sum: 0


# Arbitrary Keyword Arguments (**kwargs): A parameter prefixed with a double asterisk (**) collects all extra keyword arguments into a dictionary
def build_profile(**kwargs):
    profile = {}
    for key, value in kwargs.items():
        profile[key] = value
    return profile
def get_profile(profile_name,) -> Profile:
    profile = build_profile(name=profile_name, age=30, city="New York")
    print(profile)
get_profile("Alice")  # Output: {'name': 'Alice', 'age': 30, 'city': 'New York'}    

