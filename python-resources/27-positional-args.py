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
