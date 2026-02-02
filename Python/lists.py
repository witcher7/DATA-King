## Orderd sequence of items in Python
mylist = [1,2,3,4,5]
myfruits = ["apple", "banana", "cherry"]
user_inputs = [True,'hi', 10.5, 20 ]

# to find length of list
print(len(mylist))
print(len(myfruits))
print(len(user_inputs))

## Indexing and Slicing
print(len(myfruits)) # length of list
print(myfruits[0])   # Accessing first element
print(myfruits[-1])  # Accessing last element   
print(myfruits[0])
print(myfruits[1:3]) # Slicing from index 1 to 2

# changing elements in list
myfruits[1] = "mango"
print(myfruits) # ['apple', 'mango', 'cherry']

# deleting elements from list
del user_inputs[0]
print(user_inputs) # [ 'hi', 10.5, 20 ] # it removes first element

users = [
    {
        "user": "Alice",
        "age": 30,
    }
    ,{
        "user": "Rish",
        "age": 25,
    }
]