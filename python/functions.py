### FUNCTIONS are predefined pieces of code that perform specific tasks.


def greet(name):
    """This function greets the person passed as a parameter."""
    return f"Hello, {name}!"

# we have to call the function to see the result
print(greet("Alice"))  # Output: Hello, Alice!
print(greet("Rishabh")) # Output: Hello, Rishabh!


def addNumbers(a, b):
    """This function returns the sum of two numbers."""
    x = 100 # local variable inside the function
    ## or 
    ## print(a + b)
    return a + b # return keyword sends back the result to the caller
print(addNumbers(5, 3)) # 
print(x) # This will raise an error because x is not defined outside the function