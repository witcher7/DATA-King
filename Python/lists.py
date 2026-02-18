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

## List methods
myfruits.append("orange") # adds element at the end
print(myfruits) # ['apple', 'mango', 'cherry', 'orange']

myfruits.insert(1, "grape") # adds element at specific index
print(myfruits) # ['apple', 'grape', 'mango', 'cherry', 'orange']

myfruits.remove("mango") # removes specific element
print(myfruits) # ['apple', 'grape', 'cherry', 'orange']

popped_fruit = myfruits.pop() # removes and returns last element
print(popped_fruit) # orange    
print(myfruits) # ['apple', 'grape', 'cherry']

myfruits.sort() # sorts the list in ascending order
print(myfruits) # ['apple', 'cherry', 'grape']

myfruits.reverse() # reverses the list
print(myfruits) # ['grape', 'cherry', 'apple']
count = myfruits.count("apple") # counts occurrences of an element
print(count) # 1

myfruits.index("cherry") # returns index of first occurrence of an element
print(myfruits.index("cherry")) # 1

myfruits.copy() # returns a shallow copy of the list
new_fruits = myfruits.copy()
print(myfruits)

myfruits.extend(["kiwi", "melon"]) # extends list by appending elements from another list
print(myfruits) # ['grape', 'cherry', 'apple', 'kiwi', 'melon']

# append vs extend 
# append adds its argument as a single element to the end of a list
# extend iterates over its argument adding each element to the list, extending the list.

myfruits.sort(reverse=True) # sorts the list in descending order
print(myfruits) # ['kiwi', 'grape', 'cherry', 'apple', 'melon']
print(min(myfruits))
print(max(myfruits))
print(sum(mylist)) # sums up all elements in the list


## dunder methods for list
print(dir(myfruits))
num1 = [1, 2, 3, 4,]
num2 = [1, 2,]
merged_nums = num1.__add__(num2) # merges two lists

## when we copy list using = operator it creates reference
list_a = [1, 2, 3]
list_b = list_a 
list_b.append(4)
print(list_a) # [1, 2, 3, 4]     # list_a is also changed

## we can use copy() method to create a shallow copy of the list
# deep copy vs shallow copy 
# shallow copy creates a new object but inserts references into it to the objects found in the original.
# deep copy creates a new object and recursively adds copies of nested objects found in the original.
my_cars = ["BMW", "Audi", "Tesla"]
copied_cars = my_cars.copy()
copied_cars.sort(reverse=True)
print(copied_cars) # ['Tesla', 'BMW', 'Audi']
print(my_cars) # ['BMW', 'Audi', 'Tesla'] 
# to create deep copy we can use copy module


## Unpacking Lists 

myfruits = ["Apple","Banana","Lime"]
myapple , mybanana , mylime = myfruits
print(myapple)


user_credentials = [
   ("user1","password_one"),
   ("user2","password_two"),
   ("user3","password_three")
]
user1,user2, user3 = user_credentials
user1_username, user1_password = user1 
print(user1_username,user1_password)


## 
school_grades = (80,75,35,20,90)
first, *middle , last = school_grades
print(first)
print(middle)
print(last)



## List comprehension

all_nums = [1,2,3,4,20]
absolute_nums = [abs(num) for num in all_nums]

print(absolute_nums)
print(all_nums)


all_nums = [1,2,3,10,-3,-20,30,-100]
positive_nums = [num for num in all_nums if num >0]
print(positive_nums)
print(all_nums)


## SET comprehension 
myset = {1,2,3,4,20,0,15}
new_set = set()
for i in myset:
    new_set.add(i**i)
print(new_set)
print(myset)

my_set = {1,10,15}
new_set = {val*val for val in myset}

## Dictionary Comprehension 
my_scores = {
    'a': 10,
    'b': 7,
    "c": 8,
}
scores = {k: v*10 for k, v in my_scores.items()}
print(scores)
print(my_scores) 