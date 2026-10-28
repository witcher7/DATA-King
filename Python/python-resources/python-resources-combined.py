# ============================================================================
# Combined Python Resources File
# All Python files from python-resources folder combined in numerical order
# ============================================================================

# ============================================================================
# 01-main-types.py
# ============================================================================
print('Hello Python')
print("Hello Python")

print(100)
print(-20)

print(True)
print(False)

print([])
print([1, 2, 3])

print({})
print({'name': 'Bogdan'})
print({
    'name': 'Bogdan',
    'is_instructor': True
})

# ============================================================================
# 02-input.py
# ============================================================================
my_name = input("Please enter your name: ")

print(my_name)

my_favorite_num = input("Please enter your favorite number: ")

print(my_favorite_num)
print(type(my_favorite_num))

print(my_name.upper())

# ============================================================================
# 03-idents.py
# ============================================================================
def print_num(num):
    print(num)


print_num(5)

if 10 > 5:
    print(True)

# ============================================================================
# 04-functions.py
# ============================================================================
# 1. function declaration
def hello(name):
    print(name)
    print("Hello, there!")
    print("Hi there")


hello("Bogdan")
hello("Alice")


# 2. function parameters and arguments
def add_numbers(a, b):
    sum = a + b
    print(sum)


add_numbers(5, 2)
add_numbers(100, 50)
add_numbers(8, 10.5)


# 3. return statement
def multiply_numbers(a, b):
    result = a * b
    return result
    print("This line is not executed!")


result_of_multiplication = multiply_numbers(20, 5)
print(result_of_multiplication)

print(multiply_numbers(15, 2))

# ============================================================================
# 05-pep8.py
# ============================================================================
print(       'Bogdan'    ,    10




             )

def my_fn():
    print(True)
my_fn()

# ============================================================================
# 06-comments.py
# ============================================================================
# Single line comment

# Multi
# line
# comment

print(777)  # Printing 777 to the terminal
print('Bogdan')  # Printing my name to the terminal

# ============================================================================
# 07-id.py
# ============================================================================
my_name = 'Bogdan'
print(id(my_name))

my_num = 777

other_num = my_num
print(id(my_num) == id(other_num))

# ============================================================================
# 08-type.py
# ============================================================================
my_num = 777
print(type(my_num) == int)  # True

print(type(int))
print(type(str))
print(type(bool))
print(type(list))
print(type(dict))

# ============================================================================
# 09-isinstance.py
# ============================================================================
print(isinstance(777, int))
print(isinstance(777, object))
print(isinstance('Bogdan', str))
print(isinstance('Bogdan', object))
print(type(object))  # <class 'type'>

# ============================================================================
# 10-str.py
# ============================================================================
long_str = "This is a very long string"

long_str = 'It\'s a great day today'

long_str = "This is a " \
           "very long " \
           "string"

long_str = """This is a very, very,
 very, very, very, very,
 very, very, very, very, very, very,
 very, very, very, very, very, very long string"""

print(long_str)
print(type(long_str))
print(type(long_str) == str)
print(id(long_str))

# ============================================================================
# 11-str-methods.py
# ============================================================================
my_comment = "This is my short comment"
print(my_comment)
print(len(my_comment))
print(my_comment.count(' '))
print(my_comment.count('is'))
print(my_comment[4])
print(my_comment[2:-10])
print(my_comment[3:7])
print(my_comment.find('short'))
print(my_comment.find('long'))
print(my_comment.find('long') == -1)
print(my_comment.split(' '))
print(my_comment.upper())
print(my_comment.lower())
print(dir(my_comment))

my_comment = my_comment.replace('short', 'long')

print(my_comment)

# ============================================================================
# 12-str-concatenation.py
# ============================================================================
# 1. Plus operator
my_name = 'Bogdan'
my_hobby = 'running'
time = 8

info = my_name + ' likes ' + my_hobby + ' at ' + str(time) + " o'clock"
print(info)


# 2. f-string
my_name = 'Bogdan'
my_hobby = 'running'
time = 8

info = f"{my_name} likes {my_hobby} at {time} o'clock"
print(info)


# 3. format string method
my_name = 'Bogdan'
my_hobby = 'running'
time = 8

info = "{} likes {} at {} o'clock".format(my_name, my_hobby, time)
print(info)


# 4. string interpolation
info = "%s likes %s at %s o'clock" % (my_name, my_hobby, time)
print(info)

# ============================================================================
# 13-int.py
# ============================================================================
my_num = 1000
other_num = 100

res = my_num + other_num
print(res)


my_num = 1_000_000_000_000
other_num = 1_000

res = my_num / other_num
print(res)


input_str = input("Enter any number: ")
print(type(input_str))
try:
    input_num = int(input_str)
    print(type(input_num))
except ValueError:
    print("Not able to convert to int")

# ============================================================================
# 14-float.py
# ============================================================================
average_rating = 4.65

print(average_rating.is_integer())  # False
print(round(average_rating))  # 5
print(int(average_rating))  # 4
print(float(100))  # 100.0

# ============================================================================
# 15-bool.py
# ============================================================================
db_is_available = False

print(db_is_available)
print(type(db_is_available))
print(isinstance(db_is_available, bool))

db_is_available = True
print(db_is_available)


print(bool(10))  # True
print(bool(0))  # False
print(bool(0.0))  # False
print(bool('abc'))  # True
print(bool(''))  # False


print(100 > 50)
print(100 == 50)
print([1, 2, 3] == [1, 2, 3, 4])
print([1, 2, 3] == [1, 2, 3])

is_available = True
print(not is_available)

my_name = 'Bogdan'

print(is_available and my_name)

if is_available and my_name:
    print("Is available")

# ============================================================================
# 16-magic-methods.py
# ============================================================================
print(dir(str))


print(str.__doc__)
print(bool.__doc__)


my_num = 10
other_num = 20

print(my_num.__eq__(other_num))
print(my_num == other_num)

print(help(my_num.__add__))

# ============================================================================
# 17-lists.py
# ============================================================================
my_nums = [10, 3, 100, 35]

print(my_nums)
print(len(my_nums))
my_nums.pop(2)
print(my_nums)
print(len(my_nums))


my_nums = [10, 3, 100, 35]

my_nums.extend([34, 62])
print(my_nums)


my_nums = [10, 3, 100, 35, 100]
print(my_nums.index(100))


my_nums = [10, 3, 100, 35, 100]

my_nums.clear()
print(my_nums)
my_nums.append(50)
print(my_nums)


my_nums = [10, 3, 100, 35, 100]
other_nums = [351, 245, 425]

merged_nums = my_nums + other_nums
# merged_nums = my_nums.__add__(other_nums)
print(merged_nums)
print(my_nums)
print(other_nums)


my_nums = [10, 3, 100, 35, 100]

my_nums[2] = 0
print(my_nums)


my_list = [True, None, 'abc', 10, 10.5, [1, 2], {'name': 'Bogdan'}]
print(my_list)

# ============================================================================
# 18-copy-lists.py
# ============================================================================
my_list = [10, 'abc', True]

# OPTION 1
copy_of_my_list = my_list[:]

# # OPTION 2
# copy_of_my_list = my_list.copy()

# # OPTION 3
# copy_of_my_list = list(my_list)

copy_of_my_list.append(100)
print(my_list)
print(copy_of_my_list)
print(id(my_list) == id(copy_of_my_list))
print(id(my_list))
print(id(copy_of_my_list))

# ============================================================================
# 19-dict.py
# ============================================================================
# 1. Working with keys and values in the dictionary
my_bike = {'brand': 'Custom', 'price': 2000}

print(my_bike['brand'])
my_bike['color'] = 'red'
print(my_bike)


# 2. Changing value of specific key
my_bike = {'brand': 'Custom', 'price': 2000}

print(my_bike)
my_bike['price'] = 3000
print(my_bike)


# 3. Getting all keys from the dictionary
my_bike = {'brand': 'Custom', 'price': 2000}

keys = list(my_bike.keys())
print(type(keys))
print(keys)


# 4. Getting pairs of keys and values from the dictionary
my_bike = {'brand': 'Custom', 'price': 2000}

print(my_bike.items())


# 5. Copying the dictionary
my_bike = {'brand': 'Custom', 'price': 2000}

other_bike = my_bike.copy()

other_bike['color'] = 'red'
print(my_bike)
print(other_bike)


# 6. "get" method vs square brackets notation for accessing key values
my_bike = {'brand': 'Custom', 'price': 2000}

print(my_bike.get('color', 'black'))
print(my_bike['brand'])


my_list = [('a', 10), ('b', 20)]

print(dict(my_list))

# ============================================================================
# 20-tuple.py
# ============================================================================
screen_res = (1920, 1080)

print(screen_res)
print(type(screen_res))
print(isinstance(screen_res, tuple))
print(id(screen_res))

print(screen_res.count(1080))
print(screen_res.index(1080))

screen_res_list = list(screen_res)
screen_res_list[0] = 1444
print(screen_res_list)

screen_res = tuple(screen_res_list)
print(screen_res)
print(id(screen_res))


screen_res = (1920, 1080)
screen_info = (True, 'Samsung', 150)

screen_data = screen_res + screen_info
print(screen_data)
print(screen_res)
print(screen_info)

print(screen_data[0])
print(screen_data[-1])
print(len(screen_data))

# ============================================================================
# 21-set.py
# ============================================================================
my_set = {10, 5, 5, 100, 10, 20}

print(my_set)
print(type(my_set))
print(isinstance(my_set, set))
print(len(my_set))

# my_set[0]  # TypeError: 'set' object is not subscriptable

my_list = [10, 5, 5, 100, 10, 20]

print(my_list.__getitem__(3))

my_str = 'asdfasdfads'
print(my_str.__getitem__(6))


my_set = set()
print(my_set)
print(type(my_set))


my_set = {10, True, 'abc', [1, 2]}  # Error

# ============================================================================
# 22-set-methods.py
# ============================================================================
# 1. Add, Remove and Discard
my_set = {10, 2, 10, 5, 7}

print(my_set)
my_set.add(8)
print(my_set)
# my_set.remove(200)  # Error if element is absent
my_set.discard(200)  # No Error if element is absent
print(my_set)


# 2. Intersection and Union
my_set = {10, 2, 10, 5, 7}
other_set = {34, 1, 10, 5}

print(my_set.intersection(other_set))
print(other_set.intersection(my_set))
print(my_set.intersection((2, 100, 200)))
print(my_set & other_set)

print(my_set.union(other_set))
print(other_set.union(my_set))
print(my_set.union(other_set) == other_set.union(my_set))
print(my_set | other_set)


# 3. Copy
my_set = {10, 2, 10, 5, 7}
other_set = {34, 1, 10, 5}

set_copy = other_set.copy()
set_copy.add(200)
print(set_copy)
print(other_set)


# 4. Issubset and Issuperset
my_set = {10, 5}
other_set = {34, 1, 10, 5}

print(my_set.issubset(other_set))
print(other_set.issuperset(my_set))


# 5. Symmetric Difference
a = {'a', 'c', 'd'}
b = {'l', 'm', 'c'}

print(a.symmetric_difference(b))

print((a | b) - (a & b))

# ============================================================================
# 23-range.py
# ============================================================================
# 1. Ranges with start, stop and step
odd_nums = range(1, 100, 2)
even_nums = range(0, 101, 2)

print(list(odd_nums))
print(list(even_nums))


# 2. Index and count methods of the ranges
odd_nums = range(1, 100, 2)

print(odd_nums.index(51))
print(odd_nums.count(50))
print(odd_nums.count(51))

print(odd_nums.start)
print(odd_nums.stop)
print(odd_nums.step)


# 3. Range with start and stop
my_range = range(5, 8)

print(my_range.start)
print(my_range.stop)
print(my_range.step)


# 4. Conversion of the range to list, tuple or set
odd_nums = range(1, 100, 2)

print(list(odd_nums))
print(tuple(odd_nums))
print(set(odd_nums))
print(dict(odd_nums))  # TypeError

# ============================================================================
# 24-zip.py
# ============================================================================
# 1. Zip object creation and its conversion to a list
products = ['phone', 'tablet', 'laptop']
quantities = [343, 13, 74]

products_qtys = zip(products, quantities)

print(products_qtys)
print(type(products_qtys))

products_qtys_list = list(products_qtys)
print(products_qtys_list)


# 2. Iteration over the zip object
products = ['phone', 'tablet', 'laptop']
quantities = (343, 13, 74)
tags = 'asd'

products_qtys = zip(products, quantities, tags)

for product in products_qtys:
    print(product)
    print(product[0])


# 3. Conversion of the zip object to a dictionary
products = ['phone', 'tablet', 'laptop']
quantities = (343, 13)

products_qtys = zip(products, quantities)

products_qtys_dict = dict(products_qtys)
print(products_qtys_dict)

# ============================================================================
# 25-deepcopy.py
# ============================================================================
from copy import deepcopy

info = {
    'name': 'Bogdan',
    'is_instructor': True,
    'reviews': []
}

info_deepcopy = deepcopy(info)
print(info_deepcopy)
print(id(info_deepcopy), id(info))

info_deepcopy['reviews'].append('Great course!')
info['reviews'].append('Thanks!')
print(id(info['reviews']), id(info_deepcopy['reviews']))

print(info)
print(info_deepcopy)

# ============================================================================
# 26-objects-in-functions.py
# ============================================================================
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

# ============================================================================
# 27-positional-args.py
# ============================================================================
# 1. Matching quantity of the arguments and parameters
def my_fn(first, second):
    print(first)
    print(second)


my_fn(None, 10)


# 2. Arguments and parameters quantities mismatch
def my_fn(first, second):
    print(first)
    print(second)


my_fn(None)  # Error


# 3. Default value for the parameter makes it optional
def my_fn(first, second=True):
    print(first)
    print(second)


my_fn(None)

# ============================================================================
# 28-args.py
# ============================================================================
# 1. Gathering all positional arguments into a tuple
def sort_nums(*args):
    print(args)
    print(type(args))


sort_nums(10, 3, 15, 246, 23)


# 2. Iteration of the tuple with all positional arguments
def sort_nums(*nums):
    for num in nums:
        print(num)


sort_nums(10, 3, 15, 246, 23)


# 3. Sorting all positional arguments in the function
def sort_nums(*args):
    return sorted(args)


sorted_nums = sort_nums(10, 3, 15, 246, 23)
print(sorted_nums)

sorted_nums = sort_nums(377, 23, 3)
print(sorted_nums)

# ============================================================================
# 29-keyword-arguments.py
# ============================================================================
# 1. Keyword arguments in the function call
def comments_info(comments_qty, day):
    print(f'{comments_qty} comments were posted on {day}')


comments_info(comments_qty=50, day='Monday')
comments_info(20, day='Sunday')
# comments_info(day='Sunday', 20)  # Error
comments_info(10, 'Friday')


# 2. Keyword arguments can't be gathered into the args tuple
def comments_info(*args):
    print(f'{args[0]} comments were posted on {args[1]}')


comments_info(50, day='Monday')  # Error

# ============================================================================
# 30-kwargs.py
# ============================================================================
# 1. Required parameters and keyword arguments
def product_price_info(product_title, product_price):
    print(f'{product_title} costs {product_price}$')


product_price_info(product_title="Bottle of water", product_price=2)


# 2. Gathering all keyword arguments into a dictionary
def product_price_info(**product):
    print(product)


product_price_info(product_title="Bottle of water",
                   product_price=2, product_availability=True)


# 3. Accessing values of the dictionary in the function
def product_price_info(**product):
    print(f"{product['product_title']} costs {product['product_price']}$")


product_price_info(product_title="Bottle of water", product_price=2)


# 4. Assigning values from the dictionary to the variables
def product_price_info(**product):
    title = product['product_title']
    price = product['product_price']
    print(f"{title} costs {price}$")


product_price_info(product_title="Bottle of water", product_price=2)

# ============================================================================
# 31-args-kwargs.py
# ============================================================================
def send_email(to, subject, *args, **kwargs):
    """
    Sends email to different recipients

    :param str to: Recipient address
    :param str subject: Email subject
    :param str args: Additional recipients
    :param str kwargs: Additional details
    :return None:
    """
    print(f"Sending an email to: {to}")
    print(f"Email subject: {subject}")

    if args:
        print("Additional recipients:")
        for recipient in args:
            print(recipient)

    if kwargs:
        print("Additional details for the email:")
        for key in list(kwargs):
            print(f"{key}: {kwargs[key]}")


send_email('test@test.com',
           'Hello there!')
print('_______')
send_email('test@test.com',
           'Hello there!',
           'other@test.com',
           'someone@gmail.com')
print('_______')
send_email('test@test.com',
           'Hello there!',
           bcc='bogdan@gmail.com',
           img='test.png')
print('_______')
send_email('test@test.com',
           'Hello there!',
           'other@test.com',
           'someone@gmail.com',
           bcc='bogdan@gmail.com',
           img='test.png')
print('_______')
send_email(True, 100, 1000)

# ============================================================================
# 32-default-parameters.py
# ============================================================================
from datetime import date


def get_weekday():
    return date.today().strftime('%A')


def create_new_post(post, weekday=get_weekday()):
    post_copy = post.copy()
    post_copy['created_on_weekday'] = weekday
    return post_copy


initial_post = {
    'id': 243,
    'author': 'Bogdan',
}

post_with_weekday = create_new_post(initial_post)

print(post_with_weekday)

# ============================================================================
# 33-docstring.py
# ============================================================================
def print_number_info(num):
    """
    Returns info regarding num, whether num is even or odd

    :param int num: Number to be evaluated
    :return str: Returns string which tells whether num is even or odd
    """
    if (num % 2) == 0:
        return "Num is even"
    else:
        return "Num is odd"


print(print_number_info(21))

# ============================================================================
# 34-scopes.py
# ============================================================================
c = True


def mult(a, b):
    c = a * b
    print(dir())
    return c


print(mult(100, 30))
print(dir())

# ============================================================================
# 35-global.py
# ============================================================================
counter = 0


def inc_counter(value=1):
    """
    Increments value

    :param int value: Increment counter by value
    """
    global counter
    counter += value


def dec_counter(value=1):
    """
    Decrements value

    :param int value: Decrement counter by value
    """
    global counter
    counter -= value


inc_counter(5)
print(counter)
inc_counter(2)
print(counter)
dec_counter()
print(counter)

# ============================================================================
# 36-prefix-operators.py
# ============================================================================
# 1. Prefix unary "-" operator
my_num = -10

print(my_num)
print(-my_num)


# 2. Prefix unary "+" operator
my_num = -10.3

print(my_num)
print(+my_num)


# 3. Prefix unary "+" operator with booleans
my_num = False

print(my_num)
print(+my_num)


# 4. Prefix unary "not" operator
my_name = 'Bogdan'

print(my_name)
print(not my_name)
print(not not my_name)
print(bool(my_name))


# 5. Prefix unary "not" operator with non-empty list
my_list = [1, 2]
print(not my_list)


# 6. Prefix unary "not" operator with empty list
my_list = []
print(not my_list)

# ============================================================================
# 37-comparison.py
# ============================================================================
# 1. Comparison operators for integers
a = 7
b = 10

print(a > b)
print(a >= b)
print(a < b)
print(a <= b)
print(a == b)
print(a != b)


# 2. Comparison operators for lists and corresponding magic methods
a = [1, 2]
b = [1, 2]

print(id(a))
print(id(b))

print(a > b)
# a.__gt__
print(a >= b)
# a.__ge__
print(a < b)
# a.__lt__
print(a <= b)
# a.__le__
print(a == b)
# a.__eq__
print(a != b)
# a.__ne__


# 3. Comparison operators in the conditional statements
name = 'Alice'

if len(name) > 4:
    print("Name is longer than 4 characters")

name = 'Bob'

if len(name) > 4:
    print("Name is longer than 4 characters")


# 4. Comparison operator and built-in sum function
my_nums = (10, 3, 20, 6)

print(sum(my_nums))

if sum(my_nums) > 20:
    print("Sum is greater than 20")


# 5. Checking if list is already sorted using equality operator and built-in sorted function
my_nums = [10, 3, 5, 20]

if my_nums == sorted(my_nums):
    print("List my_nums is already sorted!")

other_nums = [3.5, 5.10, 7.75, 10.05]

if other_nums == sorted(other_nums):
    print("List other_nums is already sorted")

print(id(other_nums) == id(sorted(other_nums)))

# ============================================================================
# 38-falsy-values.py
# ============================================================================
# 1. Falsy values
print(bool(0))
print(bool(0.0))
print(bool(0j))

print(bool(None))
print(bool(False))

print(bool(''))

print(bool([]))
print(bool({}))
print(bool(()))
print(bool(set()))
print(bool(range(0)))


# 2. Truthy values
print(bool(10))
print(bool(3.6))
print(bool(3j))

print(bool(True))

print(bool('abc'))

print(bool([1, 2]))
print(bool({'a': 'abc'}))
print(bool((3, 5)))
print(bool({10, 20}))
print(bool(range(100)))


# 3. No need to compare "len" of the sequence to 0
my_dict = {'a': 10, 'b': [1, 2]}

if len(my_dict) > 0:
    print("Dictionary is not empty")


# 4. No need to use "len" of the sequence
my_dict = {'a': 10, 'b': [1, 2]}

if len(my_dict):
    print("Dictionary is not empty")


# 5. No need to convert to "bool" explicitly
my_dict = {'a': 10, 'b': [1, 2]}

if bool(my_dict):
    print("Dictionary is not empty")


# 6. Implicit conversion to "bool"
my_dict = {'a': 10, 'b': [1, 2]}

if my_dict:
    print("Dictionary is not empty")

if not my_dict:
    print("Dictionary is empty")

if my_dict.get('b'):
    print("Key 'b' in the dictionary has value")

# ============================================================================
# 39-short-cirquit.py
# ============================================================================
# 1. Short-circuit "or" operator (looks for the first falsy value)
print('apple' or 'banana' or 'strawberry')
print('apple' or print('CALLED') or 'banana' or 'strawberry')
print('' or print('CALLED') or 'banana' or 'strawberry')
print('' or 0 or [] or {} or print('CALLED'))
print('apple' or 'banana')


# 2. Short-circuit "and" operator (looks for the first truthy value)
print('apple' and 'banana')
print('apple' and 'banana' and 'strawberry')
print('' and 'banana' and 'strawberry')
print(0 and 'banana' and 'strawberry')
print(0 and print('CALLED') and 'banana' and 'strawberry')
print(10 > 100 and print('CALLED') and 'banana' and 'strawberry')
print('apple' and print('CALLED') and 'banana' and 'strawberry')
print('apple' and 'banana' and 'strawberry')


# 3. Logical operators could be chained
print('apple' or 'banana' and 'strawberry')


# 4. Round brackets impact order of the operands evaluation
print(('apple' or 'banana') and 'strawberry')


# 5. Result of entire expression with "or" is truthy if any of the operands is truthy
my_list = [1, 2]
other_list = ['a', 'b']

print(my_list or other_list)


# 6. Round brackets impact order of the operands evaluation
my_list = []
other_list = [1]

print(not not (my_list or other_list))


# 7. "and" operator instead of the if statement
my_list = [1, 2]

if my_list:
    print("List is not empty")

my_list and print("List is not empty")

# ============================================================================
# 40-lambda.py
# ============================================================================
# 1. Regular function returns a lambda function
def multiply_by(multiplier):
    return lambda x: x * multiplier


multiply_by_3 = multiply_by(3)

print(multiply_by_3(10))
print(multiply_by_3(50))

multiply_by_5 = multiply_by(5)

print(multiply_by_5(10))
print(multiply_by_5(50))


# 2. Sorting list of dictionaries
students = [
    {'name': 'John', 'score': 50},
    {'name': 'Alice', 'score': 20},
    {'name': 'Bob', 'score': 90}
]

# def sort_by_score(student):
#     return student['score']

students.sort(key=lambda student: student['score'], reverse=True)
print(students)


# 3. Filtering a list
my_nums = [3, 4, 10, 15, 20, 21]

even_nums = list(filter(lambda num: num % 2 == 0, my_nums))
print('Even numbers', even_nums)

odd_nums = list(filter(lambda num: num % 2 == 1, my_nums))
print('Odd numbers', odd_nums)

# ============================================================================
# 41-try-except.py
# ============================================================================
# 1. Different except blocks
try:
    salary = int(input("Enter salary amount: "))
    days_qty = int(input("Enter days quantity: "))
    salary_per_day = round(salary / days_qty)
    print(salary_per_day)
except ValueError:
    print("Cannot convert value to integer")
except ZeroDivisionError:
    print("Cannot divide by zero!")


# 2. One except block with different error types
try:
    salary = int(input("Enter salary amount: "))
    days_qty = int(input("Enter days quantity: "))
    salary_per_day = round(salary / days_qty)
    print(salary_per_day)
except (ValueError, ZeroDivisionError) as e:
    if type(e) == ValueError:
        print(e)
        print("Cannot convert value to int")
    if type(e) == ZeroDivisionError:
        print(e)
        print("Cannot divide by zero")


# 3. General exception class and different actions depending on the error type
try:
    salary = int(input("Enter salary amount: "))
    days_qty = int(input("Enter days quantity: "))
    salary_per_day = round(salary / days_qty)
    print(salary_per_day)
except Exception as e:
    if type(e) == ValueError:
        print(e)
        print("Cannot convert value to int")
    if type(e) == ZeroDivisionError:
        print(e)
        print("Cannot divide by zero")


# 4. General exception class
try:
    salary = int(input("Enter salary amount: "))
    days_qty = int(input("Enter days quantity: "))
    salary_per_day = round(salary / days_qty)
    print(salary_per_day)
except Exception as e:
    print(type(e))
    print(e)
    print(isinstance(e, Exception))
    print(isinstance(e, ValueError))
    print(isinstance(e, ZeroDivisionError))


# 5. No error context (NOT RECOMMENDED)
try:
    salary = int(input("Enter salary amount: "))
    days_qty = int(input("Enter days quantity: "))
    salary_per_day = round(salary / days_qty)
    print(salary_per_day)
except:
    print("Some error happened")


# 6. else and finally blocks
try:
    salary = int(input("Enter salary amount: "))
    days_qty = int(input("Enter days quantity: "))
    salary_per_day = round(salary / days_qty)
except ValueError as e:
    print(e)
    print("Cannot convert value to integer")
except ZeroDivisionError as e:
    print(e)
    print("Cannot divide by zero!")
else:
    print("Result, salary per day: ", salary_per_day)
finally:
    print("Salary operation calculation complete")


# 7. Handling file not found error
try:
    file = open("file.txt", "r")
except FileNotFoundError as e:
    print(e)
else:
    print("File is ready for reading")
finally:
    if 'file' in globals() and file and not file.closed:
        file.close()
        print("File was closed.")
        print(file.closed)

# ============================================================================
# 42-raise.py
# ============================================================================
def contains_at_symbol(email):
    return '@' in email


def register_user(email: str, age: int):
    if not isinstance(email, str):
        raise TypeError("Email must be a string")

    if not isinstance(age, int):
        raise TypeError("Age must be an integer")

    if not contains_at_symbol(email):
        raise ValueError("Invalid email. Email must contain @ sign")

    # Register user...
    print("User was registered successfully")
    return {'email': email, 'age': age}


try:
    registered_user = register_user('abc@abc.com', 10)
    print(registered_user)
except (TypeError, ValueError) as e:
    print(e)

# ============================================================================
# 43-list-tuple-unpacking.py
# ============================================================================
# 1. Tuple unpacking
employee_info = ("Jane Doe", 32, "Junior Developer")

employee_name, employee_age, employee_position = employee_info

# employee_name = employee_info[0]
# employee_age = employee_info[1]
# employee_position = employee_info[2]

print(employee_name, employee_age, employee_position)


# 2. Creating a new tuple
color = (225, 128, 10)

red, green, blue = color
print(red)
print(green)
print(blue)

red = 100
blue = 20

color = (red, green, blue)
print(color)


# 3. List of tuples
user_credentials = [
    ("user1", "password_one"),
    ("user2", "password_two"),
    ("user3", "password_three")
]

user1, user2, user3 = user_credentials

print(user1)
print(user2)
print(user3)

user1_username, user1_password = user1
user2_username, user2_password = user2
user3_username, user3_password = user3

print(user1_username, user1_password)
print(user2_username, user2_password)
print(user3_username, user3_password)


# 4. Error - unpacking more elements
person = ('Bob', 25)

# ValueError: not enough values to unpack (expected 3, got 2)
name, age, city = person

print(name)
print(age)
print(city)


# 5. No error
person = ('Bob', 25)

name, age, *other = person

print(name)
print(age)
print(other)


# 6. Gathering middle elements
school_grades = (80, 75, 35, 20, 90)

first, *middle, last = school_grades

print(first)
print(middle)
print(last)


# 7. Gathering remaining elements
school_grades = (80, 75, 35, 20, 90)

first, second, *remaining = school_grades

print(first)
print(second)
print(remaining)


# 8. Placeholder variable
comment = ("This is a great course", 'bob_202', 120, 4.7)

_, username, _, course_rating = comment

print(username)
print(course_rating)

# ============================================================================
# 44-fn-pos-args-unpacking.py
# ============================================================================
def calculate_rectangle_area(length: int, width: int):
    return length * width


dimensions = [100, 20]

# area = calculate_rectangle_area(dimensions[0], dimensions[1])
# print(area)

area = calculate_rectangle_area(*dimensions)
print(area)

# ============================================================================
# 45-fn-keyword-args-unpacking.py
# ============================================================================
# 1. Unpacking dictionary
def setup_db_connection(hostname, port, username, password):
    print(hostname, port, username, password)
    return {'hostname': hostname, 'port': port, 'username': username, 'password': password}


data = {
    'hostname': 'localhost',
    'username': 'admin',
    'password': 'admin123',
    'port_value': 3674,
}

data['port'] = data['port_value']
del data['port_value']

setup_db_connection(**data)


# 2. Unpacking dictionary or list
def create_user(username, email, password):
    # Creating user...
    return {'username': username, 'email': email, 'password': password}


user_details = {
    'username': 'bogdan-123',
    'email': 'bogdan@gmail.com',
    'password': 'bogdan1341513'
}

created_user = create_user(**user_details)
print(created_user)

user_other_details = ['alice-462', 'alice@alice.com', 'alice235423']
other_created_user = create_user(*user_other_details)
print(other_created_user)

# ============================================================================
# 46-dict-unpacking.py
# ============================================================================
# 1. Adding keys or modifying values of the keys
person = {'name': 'John', 'age': 23}

# other_person = person.copy()
# other_person['age'] = 30

other_person = {
    **person,
    'age': 30,
    'occupation': 'teacher'
}

print(person)
print(other_person)
print(id(person) == id(other_person))


# 2. Merging two dictionaries
default_settings = {'theme': 'light', 'font_size': 16}
user_settings = {'font_size': 20, 'show_avatar': True}

# merged_settings = {
#     **default_settings,
#     **user_settings
# }

merged_settings = default_settings | user_settings

print(merged_settings)

# ============================================================================
# 47-if.py
# ============================================================================
# 1. if
def check_shipping_fee(weight):
    if weight <= 0:
        print("Invalid weight. Weight must be greater than zero")

    if 0 < weight <= 5:
        print("The shipping fee is 5$")

    if 5 < weight <= 15:
        print("The shipping fee is 10$")

    if weight > 15:
        print("The shipping fee is 20$")


check_shipping_fee(11.5)


# 2. if else
def check_shipping_fee(weight):
    if weight <= 0:
        print("Invalid weight. Weight must be greater than zero")
    else:
        print("Shipping fee is 5$")


check_shipping_fee(-100)


# 3. if elif else
def check_shipping_fee(weight):
    if weight <= 0:
        print("Invalid weight. Weight must be greater than zero")
    elif weight <= 5:
        print("The shipping fee is 5$")
    elif weight <= 15:
        print("The shipping fee is 10$")
    else:
        print("The shipping fee is 20$")


check_shipping_fee(100)


# 4. Hardcoded dividers (if elif else)
def check_divisibility(num):
    if num % 3 == 0 and num % 5 == 0:
        print("Number is divisible by 3 and 5")
    elif num % 3 == 0:
        print("Number is divisible only by 3")
    elif num % 5 == 0:
        print("Number is divisible only by 5")
    else:
        print("Number is not divisible by 3 or by 5")


check_divisibility(15)


# 5. Dividers as parameters (if elif else)
def check_divisibility(num: int, divider1: int, divider2: int):
    if num % divider1 == 0 and num % divider2 == 0:
        print(f"Number is divisible by {divider1} and {divider2}")
    elif num % divider1 == 0:
        print(f"Number is divisible only by {divider1}")
    elif num % divider2 == 0:
        print(f"Number is divisible only by {divider2}")
    else:
        print(f"Number is not divisible by {divider1} or by {divider2}")


check_divisibility(20, 4, 5)

# ============================================================================
# 48-if-functions.py
# ============================================================================
# 1. "if else" in the function and single return
def calc_discounted_price(price: float, is_member: bool):
    if is_member:
        discount = price * 0.1  # 10% discount
    else:
        discount = price * 0.05  # 5% discount
    return price - discount


res_price = calc_discounted_price(price=1000, is_member=True)
print(res_price)


# 2. "if" in the function and multiple returns
def calc_discounted_price(price: float, is_member: bool):
    if is_member:
        return price - price * 0.1  # 10% discount

    return price - price * 0.05  # 5% discount


res_price = calc_discounted_price(price=1000, is_member=True)
print(res_price)


# 3. "if elif else" in the function and single return
def get_letter_grade(grade):
    if grade >= 90:
        letter_grade = 'A'
    elif grade >= 80:
        letter_grade = 'B'
    elif grade >= 70:
        letter_grade = 'C'
    elif grade >= 60:
        letter_grade = 'D'
    else:
        letter_grade = 'F'
    return letter_grade


print(get_letter_grade(70))


# 4. "if" in the function and multiple returns
def get_letter_grade(grade):
    if grade >= 90:
        return 'A'
    if grade >= 80:
        return 'B'
    if grade >= 70:
        return 'C'
    if grade >= 60:
        return 'D'

    return 'F'


print(get_letter_grade(30))

# ============================================================================
# 49-ternary.py
# ============================================================================
# 1. Assigning result of the ternary expression to a variable
user_is_active = True

user_status_string = "Active" if user_is_active else "Inactive"
print(user_status_string)


# 2. Returning result of the ternary expression from the function
def convert_status_to_str(is_active):
    return "Active" if is_active else "Inactive"


user_is_active = True

user_status = convert_status_to_str(user_is_active)
print(user_status)


# 3. Checking discount eligibility in the function using ternary operator
def check_discount_eligibility(is_member):
    discount = 0.1 if is_member else 0.05
    return discount


customer_membership = False
discount_percentage = check_discount_eligibility(customer_membership)
print(discount_percentage)


# 4. Process data in the function if needed using ternary operator
def process_data(data):
    processed_data = data if data is not None else []
    # Process data...
    return processed_data


received_data = None
data = process_data(received_data)
print(data)


# 5. Calculate grades in the function using ternary operator
def get_letter_grade(score):
    letter_grade = 'A' if score >= 90 else 'B' if score >= 80 else 'C' if score >= 70 else 'D' if score >= 60 else 'F'
    return letter_grade


print(get_letter_grade(95))
print(get_letter_grade(75))
print(get_letter_grade(60))
print(get_letter_grade(50))

# ============================================================================
# 50-for-in-list-tuple.py
# ============================================================================
# 1. Iteration of the list using "for in" loop
countries = ['USA', 'Canada', 'UK', 'Australia']

for country in countries:
    print(f"Welcome to the {country}")


# 2. Iteration of the tuple using "for in" loop
countries = ['USA', 'Canada', 'UK', 'Australia']

for country in countries:
    print(f"Welcome to the {country}")

# ============================================================================
# 51-for-in-dict.py
# ============================================================================
product_prices = {
    'PC': 1000,
    'Mobile Phone': 200,
    'Tablet': 350,
    'Camera': 700
}

for k, v in product_prices.items():
    print(k, v)

# ============================================================================
# 52-for-in-str-range-set.py
# ============================================================================
# 1. Iteration of the string using "for in" loop
name = 'Jennifer'

for char in name:
    print(char)


# 2. Iteration of the range using "for in" loop
for i in range(7):
    print(i)


# 3. Iteration of the range with step using "for in" loop
for i in range(10, -1, -1):
    print(i)
print("Rocket launch!")


# 4. Iteration of the set using "for in" loop
genres = {'Romance', 'Fantasy', 'Mystery', 'Science Fiction'}

for genre in genres:
    print(f"My favorite genre is {genre}")

# ============================================================================
# 53-while.py
# ============================================================================
# 1. Creating a timer using "while" loop
import time

seconds_qty = 5

while seconds_qty > 0:
    print(f"Timer: {seconds_qty} seconds remaining...")
    seconds_qty -= 1
    time.sleep(1)

print("Timer is up!")


# 2. Asking user for the username in the "while" loop
username = ''

while not username:
    entered_username = input("Please enter your username: ")
    if len(entered_username) > 3:
        username = entered_username
    else:
        print("Username is too short. Must be more than 3 characters!")

print(f"Welcome, {username}")


# 3. Asking for user input to start or load the game in the "while" loop
selected_option = 0

while selected_option not in range(1, 4):
    print("Menu:")
    print("1. Start the game")
    print("2. Load saved game")
    print("3. Quit")
    try:
        selected_option = int(input("Please enter your choice (1-3): "))
    except ValueError as e:
        print(e)
        print("Try to select option once again")

if selected_option == 1:
    print("Starting the game...")
if selected_option == 2:
    print("Loading the game...")
if selected_option == 3:
    print("Quitting...")

# ============================================================================
# 54-break-continue.py
# ============================================================================
# 1. Breaking the "while" loop
user_password = 'admin123'
password = ''

while password != user_password:
    print("Enter 'quit' in order to exit from login")
    password = input("Please enter your password: ")
    if password == 'quit':
        print("Quitting...")
        break

if password == user_password:
    print("Login successful!")
else:
    print("Login failed")


# 2. Breaking the "for in" loop
my_list = [10, 5, 2, 100, 35]

for num in my_list:
    if num == 2:
        break
    print(num)


# 3. "break" and "continue" in the loop
current_usernames = ['bogdan123', 'bob1', 'alice75']

while True:
    username = input("Please enter desired username: ")

    if username in current_usernames:
        print("Username is already taken. Try again")
        continue

    current_usernames.append(username)
    break

print("User registration complete.")
print(current_usernames)

# ============================================================================
# 55-comprehensions.py
# ============================================================================
# 1. List comprehension
nums = [10, 2, 5, 100]

squared_nums = [num * num for num in nums]

print(nums)
print(squared_nums)


# 2. Dictionary comprehension
fruits = ['banana', 'mandarin', 'orange', 'apple']

fruits_length = {fruit: len(fruit) for fruit in fruits}
print(fruits_length)

# {
#     'banana': 6,
#     'mandarin': 8,
#     ...
# }


# 3. Tuple comprehension
names = ['Bogdan', 'Alice', 'Bob']

names_lengths = tuple(len(name) for name in names)
print(names_lengths)


# 4. Tuple to list using comprehension
coordinates = (120, 240, 500)

coordinates_list = [coordinate * 2 for coordinate in coordinates]
print(coordinates_list)


# 5. zip object to a dictionary using comprehension
grades = (80, 95, 65)
subjects = ['Science', 'Math', 'Physics']

grade_dict = {subject: grade - 10 for subject, grade in zip(subjects, grades)}
print(grade_dict)


# 6. Dictionary to a list using comprehension
person = {
    'name': 'Bogdan',
    'favorite_num': 777,
    'is_instructor': True
}

person_str_values = [value for value in person.values() if type(value) == str]
print(person_str_values)


# 7. Dictionary to a dictionary using comprehension
stocks = {
    'GOOGL': 1500,
    'AMZN': 3000,
    'AAPL': 300
}

doubled_stocks = {k: v * 2 for k, v in stocks.items() if v >= 500}
print(doubled_stocks)


# 8. Chaining "for in" expressions
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_list = [num for sublist in nested_list for num in sublist]
print(flattened_list)

# ============================================================================
# 56-generators.py
# ============================================================================
# 1. Generator size is small
from sys import getsizeof

squares_gen = (num * num for num in range(10_000_000))

print(getsizeof(squares_gen))  # 208

print(type(squares_gen))  # <class 'generator'>

squares_list = [num * num for num in range(10_000_000)]

print(getsizeof(squares_list))  # 89095160

print(type(squares_list))  # <class 'list'>


# 2. Iteration over the generator continues where it was stopped
squares_gen = (num * num for num in range(100_000_000))

for num in squares_gen:
    print(num)
    if num == 100:
        break

print("START SECOND ITERATION")

for num in squares_gen:
    print(num)
    if num == 225:
        break

# ============================================================================
# 57-decorators.py
# ============================================================================
# 1. Syntax of the decorator function
def decorator_function(original_fn):
    def wrapper_function(*args, **kwargs):
        print(args)
        print(kwargs)
        # Some actions before execution of the original_fn function
        print("Executed before function")

        result = original_fn(*args, **kwargs)

        # Some actions after execution of the original_fn function
        print("Executed after function")

        return result

    return wrapper_function


@decorator_function
def my_function(*args, **kwargs):
    print("This is my function")


my_function(10, name='Bogdan')


# 2. Checking if user is authenticated in the decorator function
def is_user_authenticated():
    return True


def check_user_auth(fn):
    def wrapper(*args, **kwargs):
        if is_user_authenticated():
            print("User is authenticated!")
            return fn(*args, **kwargs)
        else:
            raise Exception("User is not authenticated")

    return wrapper


@check_user_auth
def do_sensitive_job():
    # Perform action only if user is authenticated
    print("Some sensitive job results")


do_sensitive_job()


# 3. Logging in the decorator function
def log_function_call(fn):
    def wrapper(*args, **kwargs):
        print(f"Calling function {fn.__name__}")
        print(f"Function arguments: {args}, {kwargs}")
        res = fn(*args, **kwargs)
        print(f"Result of the function is {res}")
        return res

    return wrapper


@log_function_call
def mult_numbers(a, b):
    return a * b


print(mult_numbers(10, 2))
print('')


@log_function_call
def sum_numbers(a, b):
    return a + b


print(sum_numbers(10, 2))
print('')
print(sum_numbers(a=50, b=5))


# 4. Arguments validation in the decorator function
def validate_args(fn):
    def wrapper(*args, **kwargs):
        for arg in args:
            if not isinstance(arg, int):
                raise ValueError("Arguments must be integers!",
                                 f"{arg} is of type {type(arg)}")
        return fn(*args, **kwargs)

    return wrapper


@validate_args
def sum_nums(a, b):
    return a + b


try:
    print(sum_nums(5, 2))
    print(sum_nums('5', 2))
except ValueError as e:
    print(e)

# ============================================================================
# 58-classes.py
# ============================================================================
# 1. Methods are inherited by the instances of the class
class Car:
    def move(self):
        print("Car is moving")

    def stop(self):
        print("Car stopped")


my_car = Car()
print(type(my_car))
print(isinstance(my_car, Car))
print(isinstance(my_car, object))
print(dir(my_car))
print(my_car.__dict__)

my_car.move()
my_car.stop()


# 2. Magic __init__ method
class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

    def info(self):
        print(f"User {self.username} has email {self.email}")


first_user = User('bogdan123', 'bogdan@bogdan.com')
first_user.info()
print(first_user.username)
print(first_user.email)

other_user = User('alice3245', 'alice@alice.com')
other_user.info()
print(other_user.username)
print(other_user.email)
print(other_user.__dict__)

other_user.username = 'a6363'
print(other_user.username)


# 3. Methods
class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author
        self.likes_qty = 0

    def like(self):
        self.likes_qty += 1


my_post = Post("My first post", "Some post content", "Bogdan")
print(my_post)
print(my_post.title)
print(my_post.likes_qty)

my_post.like()  # recommended
my_post.like()
print(my_post.likes_qty)

Post.like(my_post)  # not recommended
print(my_post.likes_qty)


# Post class doesn't have such attributes!
# Post.likes_qty
# Post.title


# 4. Static methods
class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author
        self.likes_qty = 0

    def like(self):
        self.likes_qty += 1

    @staticmethod
    def format_post(title, content):
        return (
            f"Post title: {title}\n"
            f"Post content: {content}"
        )


formatted_post = Post.format_post("Some post title", "Post contents")
print(formatted_post)


# 5. Class with just static methods
class Calculator:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def subtract(a, b):
        return a - b

    @staticmethod
    def mult(a, b):
        return a * b

    @staticmethod
    def divide(a, b):
        if b != 0:
            return a / b
        raise ValueError("Can't divide by zero")


print(Calculator.add(20, 10))
print(Calculator.subtract(20, 10))
print(Calculator.mult(20, 10))
print(Calculator.divide(20, 10))


# 6. Class attributes
class User:
    users_qty = 0

    def __init__(self, username, email):
        self.username = username
        self.email = email
        User.users_qty += 1


first_user = User('bob234', 'bob@bob.com')
second_user = User('alice356', 'alice@alice.com')
third_user = User('john324', 'john@john.com')

print(second_user.__dict__)
print(User.__dict__)

print(User.users_qty)
print(third_user.users_qty)

third_user.users_qty = 10
print(User.users_qty)  # 3
print(third_user.users_qty)  # 10
print(third_user.__dict__)


# {'username': 'john324', 'email': 'john@john.com', 'users_qty': 10}


# 7. Magic methods
class Post:
    def __init__(self, title):
        self.title = title

    def __add__(self, other):
        return f"{self.title} {other.title}"

    def __eq__(self, other):
        return self.title == other.title


first_post = Post("This is first post")
second_post = Post("This is second post")
same_post_as_first = Post("This is first post")

print(first_post + second_post)

print(first_post == same_post_as_first)  # True
print(first_post == second_post)  # False


# 8. Class extension
class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email


class AdminUser(User):
    def __init__(self, username, email, role):
        super().__init__(username, email)
        self.role = role
        self.is_admin = True


my_admin = AdminUser('admin123', 'admin@admin.com', 'Administrator')
print(my_admin)
print(type(my_admin))
print(isinstance(my_admin, AdminUser))
print(isinstance(my_admin, User))
print(isinstance(my_admin, object))

print(my_admin.__dict__)

my_user = User('bob234', 'bob@bob.com')

print(my_user.__dict__)

print(User.__subclasses__())  # [<class '__main__.AdminUser'>]
print(object.__subclasses__())

# ============================================================================
# 59-several-classes.py
# ============================================================================
class User:
    def __init__(self, username: str, email: str):
        self.username = username
        self.email = email


class Post:
    def __init__(self, title: str, content: str, author: User):
        self.title = title
        self.content = content
        self.author = author


class Forum:
    def __init__(self):
        self.users = []
        self.posts = []

    def register_user(self, username: str, email: str):
        user = User(username, email)
        self.users.append(user)
        return user

    def create_post(self, title: str, content: str, author: User):
        post = Post(title, content, author)
        self.posts.append(post)
        return post

    def find_user_by_username(self, username: str):
        for user in self.users:
            if user.username == username:
                return user

    def find_user_by_email(self, email: str):
        for user in self.users:
            if user.email == email:
                return user

    def find_posts_by_author(self, author: User):
        found_posts = []
        for post in self.posts:
            if post.author == author:
                found_posts.append(post)
        return found_posts


forum = Forum()

bogdan = forum.register_user('bogdan123', 'b@gmail.com')
alice = forum.register_user('alice643', 'a@a.com')

print(forum.users)

forum.create_post("My first post", "Post content", bogdan)

print(forum.posts)
# Now you should NOT search for posts like that. Use find_posts_by_author!
# print(forum.posts[0].title)
# print(forum.posts[0].content)
# print(forum.posts[0].author.username)
# print(forum.posts[0].author.email)

print(forum.find_user_by_username('admin12'))  # None
print(forum.find_user_by_username('bogdan123').email)  # b@gmail.com

forum.create_post("Second great post", "Post content", bogdan)

# Find posts of the user
found_posts = forum.find_posts_by_author(bogdan)
found_posts_titles = [post.title for post in found_posts]
print(found_posts_titles)


# Find user by email and find all posts by that user
user_email = 'b@gmail.com'
found_user = forum.find_user_by_email(user_email)
if found_user:
    print(forum.find_posts_by_author(found_user))
else:
    print(f"User with email {user_email} doesn't exist!")

# ============================================================================
# 60-encapsulation.py
# ============================================================================
# Encapsulation
class Email:
    def __init__(self, sender, recipient, subject, body):
        self.sender = sender
        self.recipient = recipient
        self.subject = subject
        self.body = body

    def send_email(self):
        # Logic related to sending email
        pass

    def read_email(self):
        # Logic related to reading email
        pass

# ============================================================================
# 61-inheritance.py
# ============================================================================
# Inheritance
class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def start(self):
        # Code to start the vehicle
        pass

    def stop(self):
        # Code to stop the vehicle
        pass


class Car(Vehicle):
    def __init__(self, make, model, doors_qty):
        super().__init__(make, model)
        self.doors_qty = doors_qty

    def lock_doors(self):
        # Logic to lock the doors
        pass

    def unlock_doors(self):
        # Logic to unlock the doors
        pass

# ============================================================================
# 62-polymorphism.py
# ============================================================================
# Polymorphism
import math


class Shape:
    def calc_area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calc_area(self):
        return math.pi * pow(self.radius, 2)


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calc_area(self):
        return self.width * self.height


shapes = [Circle(5), Rectangle(10, 2), Circle(7), Rectangle(25, 15)]

for shape in shapes:
    print(shape.calc_area())

# ============================================================================
# 63-abstraction.py
# ============================================================================
# Abstraction
from abc import ABC, abstractmethod


class Payment(ABC):
    @abstractmethod
    def process_payment(self):
        pass


class CreditCardPayment(Payment):
    def process_payment(self):
        # Code to process Credit Card payment
        pass


class StripePayment(Payment):
    def process_payment(self):
        # Code to process Stripe payment
        pass


class PayPalPayment(Payment):
    def process_payment(self):
        # Code to process PayPal payment
        pass

# ============================================================================
# 64-modules.py
# ============================================================================
# Check folder 63-modules

# ============================================================================
# 65-json.py
# ============================================================================
import json

# 1. list -> JSON array
my_nums = [10, 100, 5, 20]
my_nums_json = json.dumps(my_nums)
print(my_nums_json)
print(type(my_nums_json))


# 2. tuple -> JSON array
my_nums = (10, 100, 5, 20)
my_nums_json = json.dumps(my_nums)
print(my_nums_json)
print(type(my_nums_json))


# # 3. set -> JSON (not possible)
# my_nums = {10, 100, 5, 20}
# my_nums_json = json.dumps(my_nums)
# # TypeError: Object of type set is not JSON serializable


# 4. dict -> JSON object
my_post = {
    'title': "My post",
    'content': "Post content",
    'likes_qty': 25,
    'author': {
        'username': 'bogdan123',
        'email': 'b@gmail.com'
    },
    'metadata': (5, 7, 20)
}
my_post_json = json.dumps(my_post)
print(my_post_json)
print(type(my_post_json))


# 5. JSON object -> dict
my_post_dict = json.loads(my_post_json)
print(my_post_dict)
print(type(my_post_dict))
print(my_post_dict['likes_qty'])


# 6. JSON array -> list
my_list = json.loads('[10, "abc", null, [1, 2], {"name": "Bogdan"}]')
print(my_list)


# # 7. dict with function (not possible)
# def sum_fn(a, b):
#     return a + b
#
#
# my_math = {
#     'title': "Math dict",
#     'sum': sum_fn
# }
#
# my_math_json = json.dumps(my_math)
# # TypeError: Object of type function is not JSON serializable


# 8. Format dictionary using JSON
my_dict = {
    'name': 'Bogdan',
    'is_instructor': True
}

print(my_dict)

my_dict_json = json.dumps(my_dict, indent=2)

file = open('test.txt', 'w')
file.write(my_dict_json)

# ============================================================================
# 66-files-dirs-os.py
# ============================================================================
# NOTE: CREATE FEW FILES IN THE my_test_directory AFTER FIRST CODE RUN
import os

# Directory path
directory_path = 'my_test_directory'


# Check if directory exists
if not os.path.exists(directory_path):
    # Create directory
    os.mkdir(directory_path)
    print("Directory was created: ", directory_path)
else:
    print("Directory exists: ", directory_path)


# Creating path to the file
file_path = os.path.join(directory_path, 'my_file.txt')
print("File path: ", file_path)


# Getting parent directory
parent_dir = os.path.dirname(file_path)
print("Parent directory: ", parent_dir)


# Checking if the file is file path or dir path
is_file = os.path.isfile(file_path)
is_dir = os.path.isdir(directory_path)
print(f"{file_path} is file: ", is_file)
print(f"{directory_path} is directory: ", is_dir)


# Listing files in the directory
dir_files = os.listdir(directory_path)
print(f"Files in the directory {directory_path}: ")
print(dir_files)
for file in dir_files:
    print(file)


# Removing directory
if os.path.exists(directory_path):
    dir_files = os.listdir(directory_path)
    for file in dir_files:
        os.remove(os.path.join(directory_path, file))
    os.rmdir(directory_path)
    print(f"Directory {directory_path} was removed")

# ============================================================================
# 67-files-dirs-Path.py
# ============================================================================
# NOTE: CREATE FEW FILES IN THE my_test_directory AFTER FIRST CODE RUN
from pathlib import Path


# Directory path
directory_path = Path('my_test_directory')
# print(type(directory_path))
# print(Path.__subclasses__())


# Check if directory exists
if not directory_path.exists():
    # Create directory
    directory_path.mkdir()
    print("Directory was created: ", directory_path)
else:
    print("Directory already exists: ", directory_path)


# Creating path to the file
file_path = directory_path / 'my_file.txt'
# file_path = directory_path.joinpath('my_file.txt')
print("File path is: ", file_path)


# Getting parent directory
parent_dir = file_path.parent
print("Parent directory: ", parent_dir)


# Checking if the file is file path or dir path
is_file = file_path.is_file()
is_dir = directory_path.is_dir()
print(f"File {file_path} is file: ", is_file)
print(f"Directory {directory_path} is directory: ", is_dir)


# Listing files in the directory
files = [file.name for file in directory_path.iterdir() if file.is_file()]
print("Files in the directory: ", files)


# Removing directory
if directory_path.exists():
    files = [file for file in directory_path.iterdir()]
    for file in files:
        file.unlink()
    directory_path.rmdir()
    print(f"Directory {directory_path} was removed")

# ============================================================================
# 68-read-write-files.py
# ============================================================================
from pathlib import Path

# 1. File must be closed after each operation
file_path = 'my_file.txt'

file = open(file_path, 'w')

print(file)
print(type(file))

file.write("First line\n")
file.write("Second line\n")

file.close()

file = open(file_path)

print(file.read())


# 2. "with" statement closes the file automatically
file_path = 'my_file.txt'

with open(file_path, 'w') as file:
    file.write("First line\n")
    file.write("Second line\n")

with open(file_path) as file:
    print(file.read())


# 3. "readlines" reads the file into the list of strings
file_path = 'my_file.txt'

with open(file_path, 'w') as file:
    file.write("First line\n")
    file.write("Second line\n")

with open(file_path) as file:
    for line in file.readlines():
        print(line.strip())


# 4. "readline" is good for big files as it reads the file line by line
file_path = 'my_file.txt'

with open(file_path, 'w') as file:
    file.write("First line\n")
    file.write("Second line\n")

with open(file_path) as file:
    while True:
        line = file.readline()
        if not line:
            break
        print(line.strip())


# 5. Append to the file and delete file at the end
file_path = Path('my_file.txt')

with open(file_path, 'w') as file:
    file.write("First line\n")
    file.write("Second line\n")

with open(file_path) as file:
    print(file.read())

with open(file_path, 'a') as file:
    file.write("Third line\n")

with open(file_path) as file:
    print(file.read())

if file_path.exists():
    file_path.unlink()

# ============================================================================
# 69-zip.py
# ============================================================================
from zipfile import ZipFile
from pathlib import Path

files_dir = Path('my-files')
if not files_dir.exists():
    files_dir.mkdir()

zip_archive = Path('my-files.zip')
if zip_archive.exists():
    zip_archive.unlink()

with open('my-files/first.txt', 'w') as file:
    file.write("This is first file\n")

with open('my-files/second.txt', 'w') as file:
    file.write("This is second file\n")

with ZipFile('my-files.zip', mode='w') as zip_file:
    for file in files_dir.iterdir():
        print(file)
        zip_file.write(file)

with ZipFile('my-files.zip') as zip_file:
    # print(zip_file)
    # print(type(zip_file))
    # print(zip_file.infolist())
    zip_file.extractall('unzipped-my-files')
    # zip_file.extract('my-files/first.txt', 'individual-files')

# ============================================================================
# 70-csv.py
# ============================================================================
import csv

with open('test.csv', 'w') as csv_file:
    writer = csv.writer(csv_file, delimiter=';')
    writer.writerow(['user_id', 'user_name', 'comments_qty'])
    writer.writerow([5423, 'bogdan', 1300])
    writer.writerow([5425, 'alice', 830])
    writer.writerow([7245, 'bob', 970])

with open('test.csv') as csv_file:
    reader = csv.reader(csv_file, delimiter=';')
    for index, line in enumerate(reader):
        print(index, line)
        if index == 0:
            header = line
        else:
            for idx, val in enumerate(line):
                print(f"{header[idx]}: {val}")

# ============================================================================
# 71-datetime.py
# ============================================================================
# 1. date
from datetime import datetime, timedelta

future_date = datetime.date(2222, 9, 20)
print("Future date:", future_date)

print(future_date.year)
print(future_date.month)
print(future_date.day)


# 2. time
some_time = datetime.time(15, 30, 10)
print("Some time:", some_time)

print(some_time.hour)
print(some_time.minute)
print(some_time.second)


# 3. datetime
future_datetime = datetime(2100, 10, 12, 20, 50, 15)
print("Future date and time:", future_datetime)

print(dir(future_datetime))

print(future_datetime.hour)


# 4. strftime
future_datetime = datetime(2100, 10, 12, 20, 50, 15)
print("Future date and time:", future_datetime)

print("Formatted date:", future_datetime.strftime(
    "%B %d, %Y"))  # October 12, 2100
print("Formatted time:", future_datetime.strftime("%I:%M %p"))  # 08:50 PM
print("Formatted date and time:",
      future_datetime.strftime("%A, %B %d, %Y %I:%M %p"))  # Tuesday, October 12, 2100 08:50 PM
print("Formatted month:", future_datetime.strftime("%B"))  # October
print("Formatted year:", future_datetime.strftime("%Y"))  # 2100


# 5. strptime
formatted_datetime_str = "3000-11-20 14:25:45"

parsed_datetime = datetime.strptime(
    formatted_datetime_str, "%Y-%m-%d %H:%M:%S")
print(parsed_datetime)
print(parsed_datetime.year)

parsed_data = datetime.strptime("June 03, 2050", "%B %d, %Y")
print(parsed_data)
parsed_time = datetime.strptime("10:12 AM", "%I:%M %p")
print(parsed_time)
parsed_month = datetime.strptime("June", "%B")
print(parsed_month)
parsed_year = datetime.strptime("2222", "%Y")
print(parsed_year)


# 6. timedelta
future_datetime = datetime(2100, 12, 10, 18, 10, 45)

print("Original date:", future_datetime)

print(future_datetime + timedelta(days=100))
print(future_datetime + timedelta(hours=3))
print(future_datetime + timedelta(days=3, hours=5, minutes=15))

print(future_datetime - timedelta(days=5))
print(future_datetime - timedelta(days=365, hours=24))

# ============================================================================
# 72-time.py
# ============================================================================
import time

# 1. time and ctime
current_time_in_seconds = time.time()
# print(time.ctime(current_time_in_seconds))

print(time.ctime(23423423423))


# 2. sleep
start_time = time.time()
print('Start:', start_time)

time.sleep(3)

end_time = time.time()
print('Continue:', end_time)

print('Time spent:', end_time - start_time)


# 3. Measure time
start_time = time.time()

my_list = list(range(100_000_000))
print(my_list[1000000])

end_time = time.time()

print('Time spent:', round(end_time - start_time, 2))

# ============================================================================
# 73-random.py
# ============================================================================
import random

# float
print(random.random())
print(random.uniform(10.5, 11.6))


# int
print(random.randint(100, 1000))
print(random.randint(0, 1000))


# shuffle
my_list = [1, 2, 3, 4, 5, 6, 7]
print(my_list)
random.shuffle(my_list)
print(my_list)
random.shuffle(my_list)
print(my_list)


# choice
print(random.choice('Bogdan'))
print(random.choice((1, 3, 10)))
# print(random.choice({'a': 10, 'b': True}))
print(random.choice(['a', True, None]))


# choices (elements might be repeated)
print(random.choices([1, 2, 3, 4, 5], k=5))
print(random.choices('abcdef', k=10))


# create password (not recommended)
print(''.join(random.choices('ABCDEF0123456789', k=12)))


# sample (unique elements)
print(random.sample([1, 2, 3, 4, 5], k=5))
print(random.sample([1, 2, 3, 4, 5], k=3))
# print(random.sample([1, 2, 3, 4, 5], k=10))  # ValueError: Sample larger than population or is negative
print(''.join(random.sample('ABCDEF0123456789', k=12)))
print(random.sample([1, 1, 1, 1], k=3))
print(random.sample(range(1_000_000), k=10))

# ============================================================================
# 74-secrets.py
# ============================================================================
import secrets
import string


# 1. Generating password of specific length
def generate_password(length: int):
    all_chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(all_chars) for _ in range(length))
    return password


print(generate_password(5))
print(generate_password(10))
print(generate_password(20))

# print(string.digits)
# print(string.ascii_letters)
# print(string.ascii_lowercase)
# print(string.ascii_uppercase)
# print(string.punctuation)
#
# all_chars = string.ascii_letters + string.digits + string.punctuation
# print(all_chars)


# 2. Generating a CSRF token for user session
print(secrets.token_hex(8))
print(secrets.token_hex(16))
print(secrets.token_hex(24))


# 3. Generating URL safe token
print(secrets.token_urlsafe())
print(secrets.token_urlsafe(16))
# https://mywebsite.com/reset-password?token=Kny70ou4ijpyuJOOUrQSWjhY9nQ8hlewc_1PtVegY7Y


# 4. Generating OTP password
def generate_otp_password(length):
    digits = string.digits
    password = ''.join(secrets.choice(digits) for _ in range(length))
    return password


print(generate_otp_password(6))
print(generate_otp_password(4))
print(generate_otp_password(10))


# 5. Generate random password with requirements
# print(any(char.islower() for char in 'asdf2342'))
# print(any(char.isupper() for char in 'as2342'))
# print(any(char.isdigit() for char in 'asdf2342'))
# print(any(char in string.punctuation for char in 'asdf2342!?'))

counter = 0  # counts how many times we try to generate password


def generate_password(length: int):
    global counter
    counter += 1
    all_chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(all_chars) for _ in range(length))
    return password


# password must have at least one lowercase letter, one uppercase letter, one digit and one special symbolß


def generate_special_password(length: int):
    while True:
        p = generate_password(length)
        if any(c.islower() for c in p) and any(c.isupper() for c in p) and any(c.isdigit() for c in p) and any(
                c in string.punctuation for c in p):
            break
    return p


print(generate_special_password(4))
print(counter)

# ============================================================================
# 75-math.py
# ============================================================================
import math

print(math.e)
print(math.pi)

print(math.sqrt(225))
print(math.sqrt(230.5))

print(math.factorial(10))  # 1 * 2 * 3 * ... * 10

print(math.log10(100))
print(math.log10(1000))
print(math.log2(8))

print(math.floor(10.7))
print(round(10.7))

# ============================================================================
# 76-recursive-functions.py
# ============================================================================
import math


def calc_factorial(num: int):
    if type(num) is not int:
        raise TypeError("Number must be integer")
    if num <= 0:
        raise ValueError("Number must be positive")
    if num == 1:
        return 1
    return num * calc_factorial(num - 1)


print(calc_factorial(10))
# print(calc_factorial('abc'))  # TypeError: Number must be integer

print(math.factorial(10))  # 10 * 9 * 8 ... 2 * 1

# ============================================================================
# 77-re.py
# ============================================================================
import re

# 1. Searching using re "search"
my_string = "My name is Bogdan."

res = re.search(r'^M.*Bogdan\.$', my_string)
print(res.span())
print(res.start())
print(res.end())
print(res)


# 2. Creating patterns using re "compile"
my_string = "My name is Bogdan."

my_pattern = re.compile(r'B....n')
print(my_pattern)
print(type(my_pattern))

print(my_pattern.search(my_string))
print(my_pattern.search("Hello, this is Boooon"))

print(my_pattern.match(my_string))
print(my_pattern.match('Boooon'))
print(my_pattern.match('Bogdan!!!'))

print(my_pattern.findall("My name is Bogdan. Hello Bogdan"))


# 3. Validating an email using re
def validate_email(email):
    email_regexp = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    email_pattern = re.compile(email_regexp)
    is_valid = bool(email_pattern.match(email))
    return email, is_valid


print(validate_email('bogdan@gmail.com'))  # Valid
print(validate_email('bogdangmail.com'))  # Invalid
print(validate_email('bogdan@gmailcom'))  # Invalid


# 4. Substitution using re "sub"
regexp = r'bad'

my_text = "Something bad is here. bad situation. bad words"

changed_text = re.sub(regexp, '*', my_text)
print(changed_text)


# 5. Splitting the string using re "split"
my_text = "This is    a very    long    not formatted    sentence"
print(my_text)

regexp = r'\s+'

words = re.split(regexp, my_text)
print(words)
print(' '.join(words))

print(my_text.split(' '))

# ============================================================================
# 78-smtplib.py
# ============================================================================
# GUIDELINES
# 1. Install Docker
# 2. Create container
# docker run --rm --it -p 3000:80 -p 2525:25 rnwood/smt4dev

from email.message import EmailMessage
import smtplib

my_email = EmailMessage()

my_email['from'] = 'Bogdan'
my_email['to'] = 'test@test.com'
my_email['subject'] = "Hello from Python"
my_email.set_content("Hey! How are you doing?!")

with smtplib.SMTP(host='127.0.0.1', port=2525) as smtp_server:
    smtp_server.ehlo()
    # smtp_server.starttls()
    # smtp_server.login('username', 'password')
    smtp_server.send_message(my_email)
    print("Email was sent!")

# ============================================================================
# 79-smtp-html-template.py
# ============================================================================
# GUIDELINES
# 1. Install Docker
# 2. Create container
# docker run --rm --it -p 3000:80 -p 2525:25 rnwood/smt4dev
# 3. Create HTML template in the templates folder
# <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <title>Email</title>
# </head>
# <body>
#     <h1>Greetings email</h1>
#     <h2>Hello $name, how are you?</h2>
#     <h3>Let's go out $date</h3>
# </body>
# </html>

from email.message import EmailMessage
import smtplib
from string import Template
from pathlib import Path

html_template = Template(Path('templates/template.html').read_text())

html_content = html_template.substitute({'name': 'Bogdan', 'date': 'Sunday'})

my_email = EmailMessage()

my_email['from'] = 'Bogdan'
my_email['to'] = 'test@test.com'
my_email['subject'] = "Hello from Python"
my_email.set_content(html_content, 'html')

with smtplib.SMTP(host='127.0.0.1', port=2525) as smtp_server:
    smtp_server.ehlo()
    # smtp_server.starttls()
    # smtp_server.login('username', 'password')
    smtp_server.send_message(my_email)
    print("Email was sent!")

# ============================================================================
# 80-sqlite3.py
# ============================================================================
import sqlite3

DB_NAME = 'sqlite_db.db'

# 1. Create DB if it is absent
with sqlite3.connect(DB_NAME) as sqlite_conn:
    print(sqlite_conn)
    print(type(sqlite_conn))


# 2. Create DB table
with sqlite3.connect(DB_NAME) as sqlite_conn:
    sql_request = """CREATE TABLE IF NOT EXISTS courses (
        id integer PRIMARY KEY,
        title text NOT NULL,
        students_qty integer,
        reviews_qty integer
    );"""
    sqlite_conn.execute(sql_request)


# 3. Insert one record to the table
with sqlite3.connect(DB_NAME) as sqlite_conn:
    sql_request = "INSERT INTO courses VALUES(?, ?, ?, ?)"
    sqlite_conn.execute(sql_request, (251, "Python course", 100, 30))
    sqlite_conn.commit()


# 4. Write multiple records
courses = [
    (456, "JS course", 235, 50),
    (234, "Java course", 452, 20),
    (567, "Node.js course", 753, 70)
]

with sqlite3.connect(DB_NAME) as sqlite_conn:
    sql_request = "INSERT INTO courses VALUES(?, ?, ?, ?)"
    for course in courses:
        sqlite_conn.execute(sql_request, course)
    sqlite_conn.commit()


# 5. Read records
with sqlite3.connect(DB_NAME) as sqlite_conn:
    sql_request = "SELECT * FROM courses WHERE reviews_qty>=30"
    sql_cursor = sqlite_conn.execute(sql_request)
    # for course in sql_cursor:
    #     print(course)
    courses = sql_cursor.fetchall()
    print(courses)

# ============================================================================
# 81-array.py
# ============================================================================
from array import array

# 1. Create array, add and remove elements
my_int_array = array('i', [10, 4, 3, 7, 9, 15])

print(my_int_array)
print(type(my_int_array))
print(dir(my_int_array))
print(my_int_array[2])
my_int_array.append(20)
print(my_int_array)
# my_int_array.append(10.5)
my_int_array.append(True)
print(my_int_array)
my_int_array.pop(0)
print(my_int_array)


# 2. Save array to the file and load from the file
my_int_array = array('i', [10, 4, 3, 7, 9, 15])

with open('my_array.bin', 'wb') as file:
    my_int_array.tofile(file)

imported_array = array('i')
with open('my_array.bin', 'rb') as file:
    imported_array.fromfile(file, 3)
    print(imported_array)

# ============================================================================
# 82-sys.py
# ============================================================================
import sys

print(sys.argv)
print(sys.version_info)
print(sys.version)

if len(sys.argv) < 3:
    raise IOError("You must provide username and password!")

# username = sys.argv[1]
# password = sys.argv[2]
# print(username, password)

_, username, password = sys.argv
print(username, password)

# ============================================================================
# 83-webbrowser.py
# ============================================================================
import webbrowser


def search_on_search_engine(query: str, search_engine: str):
    search_engines = {
        'google': 'https://www.google.com/search?q={}',
        'yahoo': 'https://search.yahoo.com/search?p={}',
        'bing': 'https://www.bing.com/search?q={}'
    }

    if search_engine not in search_engines:
        print("Unsupported search engine:", search_engine)
        return

    search_url = search_engines[search_engine].format(query)

    webbrowser.open(search_url)


search_on_search_engine("Python programming", 'google')
search_on_search_engine("Java programming", 'bing')

# ============================================================================
# 84-django.py
# ============================================================================
# Check folder 83-django

# ============================================================================
# 85-pygame-rectangle.py
# ============================================================================
import pygame
import sys

STEP = 10

pygame.init()

screen_width, screen_height = 800, 600

screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("My first Pygame")

rect_width, rect_height = 100, 200
rect_x = screen_width / 2 - rect_width / 2
rect_y = screen_height / 2 - rect_height / 2
rect_color = pygame.Color('lightyellow')

while True:
    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and rect_y >= STEP:
                rect_y -= STEP
            if event.key == pygame.K_DOWN and rect_y <= screen_height - rect_height - STEP:
                rect_y += STEP
            if event.key == pygame.K_LEFT and rect_x >= STEP:
                rect_x -= STEP
            if event.key == pygame.K_RIGHT and rect_x <= screen_width - rect_width - STEP:
                rect_x += STEP

    screen.fill((32, 52, 71))
    pygame.draw.rect(screen, rect_color,
                     (rect_x, rect_y, rect_width, rect_height))
    pygame.display.update()

# ============================================================================
# 86-pygame-shooter.py
# ============================================================================
import pygame
import sys
from random import randint

pygame.init()

game_font = pygame.font.Font(None, 30)

screen_width, screen_height = 800, 600
screen_fill_color = (32, 52, 71)
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Awesome Shooter Game")

FIGHTER_STEP = 2
fighter_image = pygame.image.load('images/fighter.png')
fighter_width, fighter_height = fighter_image.get_size()
fighter_x = screen_width / 2 - fighter_width / 2
fighter_y = screen_height - fighter_height
fighter_is_moving_left, fighter_is_moving_right = False, False

BALL_STEP = 0.5
ball_image = pygame.image.load('images/ball.png')
ball_width, ball_height = ball_image.get_size()
ball_x, ball_y = 0, 0
ball_was_fired = False

ALIEN_STEP = 0.1
alien_speed = ALIEN_STEP
alien_image = pygame.image.load('images/alien.png')
alien_width, alien_height = alien_image.get_size()
alien_x = randint(0, screen_width - alien_width)
alien_y = 0

game_score = 0
game_is_running = True

while game_is_running:
    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                fighter_is_moving_left = True
            if event.key == pygame.K_RIGHT:
                fighter_is_moving_right = True
            if event.key == pygame.K_SPACE:
                ball_was_fired = True
                ball_x = fighter_x + fighter_width / 2 - ball_width / 2
                ball_y = fighter_y - ball_height
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                fighter_is_moving_left = False
            if event.key == pygame.K_RIGHT:
                fighter_is_moving_right = False

    if fighter_is_moving_left and fighter_x >= FIGHTER_STEP:
        fighter_x -= FIGHTER_STEP
    if fighter_is_moving_right and fighter_x <= screen_width - fighter_width - FIGHTER_STEP:
        fighter_x += FIGHTER_STEP

    if ball_was_fired and ball_y + ball_height < 0:
        ball_was_fired = False

    if ball_was_fired:
        ball_y -= BALL_STEP

    alien_y += alien_speed

    screen.fill(screen_fill_color)
    screen.blit(fighter_image, (fighter_x, fighter_y))
    screen.blit(alien_image, (alien_x, alien_y))

    if ball_was_fired:
        screen.blit(ball_image, (ball_x, ball_y))

    game_score_text = game_font.render(
        f"Your Score is: {game_score}", True, 'white')
    screen.blit(game_score_text, (20, 20))

    pygame.display.update()

    if alien_y + alien_height > fighter_y:
        game_is_running = False

    if ball_was_fired and \
            alien_x < ball_x < alien_x + alien_width - ball_width and \
            alien_y < ball_y < alien_y + alien_height - ball_height:
        ball_was_fired = False
        alien_x = randint(0, screen_width - alien_width)
        alien_y = 0
        alien_speed += ALIEN_STEP / 2
        game_score += 1

game_over_text = game_font.render("Game Over", True, 'white')
game_over_rectangle = game_over_text.get_rect()
game_over_rectangle.center = (screen_width / 2, screen_height / 2)
screen.blit(game_over_text, game_over_rectangle)
pygame.display.update()
pygame.time.wait(5000)
pygame.quit()

# ============================================================================
# 87-pygame-shooter-oop.py
# ============================================================================
# Check folder 87-pygame-shooter-oop

# ============================================================================
# 63-modules/01-entire-module/main.py
# ============================================================================
# import utils
#
# print(utils)
# print(type(utils))
# print(dir(utils))
#
# print(utils.my_name)
# print(utils.hello(utils.my_name))

# ============================================================================
# 63-modules/01-entire-module/utils.py
# ============================================================================
# def hello(name):
#     return f"Hello {name}"
#
#
# my_name = 'Bogdan'

# ============================================================================
# 63-modules/02-rename-module/main.py
# ============================================================================
# import utils as u
#
# print(u)
# print(type(u))
# print(dir(u))
#
# print(u.my_name)
# print(u.hello(u.my_name))

# ============================================================================
# 63-modules/02-rename-module/utils.py
# ============================================================================
# def hello(name):
#     return f"Hello {name}"
#
#
# my_name = 'Bogdan'

# ============================================================================
# 63-modules/03-variables/main.py
# ============================================================================
# from utils import hello, my_name as name
#
# print(hello('Bogdan'))
# print(name)
#
# print(dir())

# ============================================================================
# 63-modules/03-variables/utils.py
# ============================================================================
# def hello(name):
#     return f"Hello {name}"
#
#
# my_name = 'Bogdan'

# ============================================================================
# 63-modules/04-everything/main.py
# ============================================================================
# from utils import *
#
# my_name = 'Alice'
#
# print(dir())
# print(hello('Bogdan'))
# print(my_name)

# ============================================================================
# 63-modules/04-everything/utils.py
# ============================================================================
# def hello(name):
#     return f"Hello {name}"
#
#
# my_name = 'Bogdan'

# ============================================================================
# 63-modules/05-different-modules/main.py
# ============================================================================
# from other import sum_fn
# import utils as my_utils
#
# print(sum_fn(10, 2))
#
# print(my_utils.hello('Bogdan'))
# print(my_utils.my_name)
#
#
# def main():
#     print("Running main block of code")

# ============================================================================
# 63-modules/05-different-modules/other.py
# ============================================================================
# import utils
#
# print(utils.hello('Bogdan'))
#
#
# def sum_fn(a, b):
#     return a + b

# ============================================================================
# 63-modules/05-different-modules/utils.py
# ============================================================================
# def hello(name):
#     return f"Hello {name}"
#
#
# print('UTILS')
#
# my_name = 'Bogdan'

# ============================================================================
# 63-modules/06-subfolders/main.py
# ============================================================================
# from src.other import sum_fn
# from src import utils as my_utils
#
# print(sum_fn(10, 2))
#
# print(my_utils.hello('Bogdan'))
# print(my_utils.my_name)
#
#
# def main():
#     print("Running main block of code")

# ============================================================================
# 63-modules/06-subfolders/src/other.py
# ============================================================================
# import utils
#
# print(utils.hello('Bogdan'))
#
#
# def sum_fn(a, b):
#     return a + b

# ============================================================================
# 63-modules/06-subfolders/src/utils.py
# ============================================================================
# def hello(name):
#     return f"Hello {name}"
#
#
# print('UTILS')
#
# my_name = 'Bogdan'

# ============================================================================
# 63-modules/07-built-in-modules/main.py
# ============================================================================
# from math import pi
#
# print(pi)

# ============================================================================
# 63-modules/08-what-is-__name__/main.py
# ============================================================================
# import other
#
# print("MODULE NAME: MAIN")
#
# # print(dir())
# # print(__name__)
# # print(type(__name__))
#
# print('MAIN', __name__)
# print('MAIN', __name__ == '__main__')
#
# if __name__ == '__main__':
#     print('MAIN:', 'ONLY IF RUN DIRECTLY')

# ============================================================================
# 63-modules/08-what-is-__name__/other.py
# ============================================================================
# print("MODULE NAME: OTHER")
#
# print('OTHER', __name__)
# print('OTHER', __name__ == '__main__')
#
# if __name__ == '__main__':
#     print('OTHER:', 'ONLY IF RUN DIRECTLY')

# ============================================================================
# 63-modules/09-if-__name__/main.py
# ============================================================================
# def initialize():
#     # Code to initialize application and perform setup
#     print("Initializing...")
#
#
# def main():
#     # Code for main app functionality
#     print("Running main functionality...")
#
#
# if __name__ == '__main__':
#     initialize()
#     main()

# ============================================================================
# 63-modules/09-if-__name__/other.py
# ============================================================================
# from main import initialize
#
# initialize()

# ============================================================================
# 63-modules/10-packages/main.py
# ============================================================================
# from my_package.module_one import my_num
# from my_package.module_two import my_name
#
# print(my_num)
# print(my_name)
#
# # from my_package import module_one, module_two
# #
# # print(module_one.my_num)
# # print(module_two.my_name)

# ============================================================================
# 63-modules/10-packages/my_package/__init__.py
# ============================================================================
# (empty file)

# ============================================================================
# 63-modules/10-packages/my_package/module_one.py
# ============================================================================
# my_num = 10

# ============================================================================
# 63-modules/10-packages/my_package/module_two.py
# ============================================================================
# my_name = 'Bogdan'

# ============================================================================
# END OF COMBINED FILE
# ============================================================================
