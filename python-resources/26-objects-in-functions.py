# 1. Mutation of the external list in the function
def print_fruits_info(person_name, fruits):
    print(id(fruits))
    fruits.pop()
    for fruit in fruits:
        print(f'{person_name} likes {fruit}')


my_name = 'Bogdan'
favorite_fruits = ['oranges', 'apples', 'bananas']

print_fruits_info(my_name, favorite_fruits)
print(id(favorite_fruits))
print(favorite_fruits)


# 2. Immutable objects as function arguments
def print_fruits_info(person_name, fruits):
    person_name = 'Alice'
    print(id(person_name))
    fruits.pop()
    for fruit in fruits:
        print(f'{person_name} likes {fruit}')


my_name = 'Bogdan'
favorite_fruits = ['oranges', 'apples', 'bananas']

print_fruits_info(my_name, favorite_fruits)
print(id(my_name))
print(my_name)


# 3. Making a copy of them mutable object in the function
def print_fruits_info(person_name, fruits):
    fruits_copy = fruits.copy()
    fruits_copy.pop()
    for fruit in fruits_copy:
        print(f'{person_name} likes {fruit}')


my_name = 'Bogdan'
favorite_fruits = ['oranges', 'apples', 'bananas']

print_fruits_info(my_name, favorite_fruits)
print(favorite_fruits)
