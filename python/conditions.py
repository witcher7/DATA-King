# conditions are if-else statements
age = 10
if age > 10:
    print("You are not allowed")
else:
    print("You are allowed")

# if else helps in decision making for the program
# also if else has nested if else statements
# elif is used to check multiple conditions
price = 100
if price > 100:
    print("Price is greater than 100")
elif price == 100:
    print("Price is equal to 100")
else:
    print("Price is less than 100")

# taking input from the user
name = input("Enter your name: ")
print("Hello " + name)  
if name == "John":
    print("You are John")
else:
    print("You are not John")

# taking input as integer
age = int(input("Enter your age: "))
if age > 18:
    print("You are an adult")
else:
    print("You are a minor")
# if we dont write int before input, it will be string
# and string cannot be compared with integer

# round function is used to round off the decimal numbers
# round(number, digits)
# digits is optional, if not specified it will round off to nearest integer
# if digits is specified, it will round off to specified number of digits

round(3.14159, 2)  # 3.14
round(3.14159)  # 3

# import math helps you to use mathematical functions
import math

print(math.ceil(3.14159))  # 4
print(math.floor(3.14159))  # 3
print(math.pow(2, 3))  # 8.0
print(math.sqrt(16))  # 4.0

# A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years
# ask user for their salary and year of service and print the net bonus amount
salary = float(input("Enter your salary: "))
years = int(input("Enter your years of service: "))
if years > 5:
    print("Your net bonus is: ", salary * 0.05)
else:
    print("You are not eligible for bonus")
