my_motorbike = {
    'brand': 'Ducati', # value 
   # key 
    'price' : 25000,
    'engine_vol' : 1.2
}
other_motorbike = {
    'price' : 25000,
    'engine_vol' : 1.2,
    'brand' : 'Ducati'
}
## ORDER Does not matter in dictionaries
# Technically identical dictionaries

print(my_motorbike == other_motorbike) # true 
print(id(my_motorbike) == id(other_motorbike)) # false  

print(my_motorbike['brand']) # Accessing value using key
print(my_motorbike.get('price')) # Accessing value using get() method

## Change values 
my_motorbike['brand'] = 'Suzuki'
 
# Adding new key-value pair
print(my_motorbike.get()) # prints all key-value pairs in the dictionary
my_motorbike['color'] = 'red' # Adding new key-value pair
print(my_motorbike.get()) 
  
# Deleting a key-value pair
del my_motorbike['engine_vol'] # Deleting key-value pair using del keyword
print(my_motorbike.get()) # 

key_name = 'brand'
my_motorbike[key_name] # Accessing value using variable as key


# dictionary methods
print(my_motorbike.keys()) # Returns a view object that displays a list of all the keys in the dictionary
print(my_motorbike.values()) # Returns a view object that displays a list of all the values in the dictionary
print(my_motorbike.items()) # Returns a view object that displays a list of dictionary's key-value tuple pairs
print(len(my_motorbike)) # Returns the number of key-value pairs in the dictionary
print('brand' in my_motorbike) # Checks if 'brand' is a key in the dictionary
print(my_motorbike.get('brand', 'Key not found')) # Returns the value for 'brand' key, or 'Key not found' if the key does not exist

# NEsted dictionaries
my_motorbike ={
    'brand': 'Ducati',
    'engine_vol' : 1.2,
    'specs': {
        'color': 'red',
        'weight': 200
    }
}
print(my_motorbike['specs']['color']) # Accessing nested dictionary value using keys

# magic methods
my_dict = {}
print(my_dict.__doc__) # Returns the docstring of the dictionary class
print(my_dict.__class__) # Returns the class of the dictionary object
print(my_dict.__dict__) # Returns the dictionary of the dictionary object (which is empty in this case)
