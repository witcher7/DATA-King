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
