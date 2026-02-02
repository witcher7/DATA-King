user_input = input("Enter a number: ")
any_number = int(user_input)
print("You entered the number:", any_number)    
print(type(user_input)) # by default input() function takes input as string
print(type(any_number)) # after conversion it is int

base = 3
power = 4
result = base ** power
print(f"{base} raised to the power of {power} is {result}")
## we can also user pow() function
print(pow(base, power))

## ROunding numbers
average_price = 17.25 
print(round(average_price)) # rounds to nearest integer
print(round(average_price, 1)) # rounds to 1 decimal place
