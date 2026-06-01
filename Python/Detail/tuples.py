## Same as list 
## immutable 
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple[0]) # Accessing first element of the tuple using indexing
print(my_tuple[1]) # Accessing second element of the tuple using indexing

# Order does matter in tuples
print(len(my_tuple)) # len() function returns the length of the tuple
my_tuple[2] = 100 # This will raise a TypeError as tuples are immutable
# Items also cannot be added or removed from a tuple after it is created
# However, we can concatenate tuples to create a new tuple

users = (
    {
        "User_id": 1,
        "username": "Rishabh",
    },
    {
        "User_id": 2,
        "username": "Monalisa",
    }
)
users[1]["username"] = "Mona" # Modifying the username of the second user in the tuple

# Tuple methods
print(my_tuple.count(2)) # Returns the number of occurrences of the value 2 in the tuple
print(my_tuple.index(3)) # Returns the index of the first occurrence of the value 3 in the tuple
