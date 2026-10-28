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
