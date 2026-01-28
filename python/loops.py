# Loops are used to execute a block of code repeatedly until a certain condition is met.
# In Python, there are two main types of loops: for loops and while loops.
# for loop - iterates over a sequence (like a list, tuple, or string) or other iterable objects
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
# Output:
# apple
# banana        
for i in range(5):  # range(5) generates numbers from 0 to 4
    print(i)
# Output:
for i in range(2, 6):  # range(2, 6) generates numbers from 2 to 5
    print(i)
                # 1 is starting point, 10 is ending point, 2 is step
for i  in range(1, 10, 2):  # range(1, 10, 2) generates odd numbers from 1 to 9
    print(i)    

# courses = ["Math", "Science", "History"]
# for course in courses:
# print(f" I am studying {course}")

# for student in students:
# if student.startswith("A"):
# print(f" Student name is {student}")
# elif students!='Saif':
# print(" Not found")
# else:
# print(" End of the list")

## List comprehension with for loop
squares = [x**2 for x in range(10)]  # creates a list of squares of numbers from 0 to 9
print(squares)  # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
newlist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squares_even = [x**2 for x in newlist if x % 2 == 0]  # squares of even numbers only


### WHILE LOOP
## We dont need to know the number of iterations in advance > no need of collection to iterate over
count = 0
while count < 5:
    print(count)
    count += 1  # increment count by 1
# Output:
# 0
# 1     
# 2
# 3
# 4
# Infinite loop example (commented out to prevent execution)
# while True:
#     print("This will run forever")
# Output:
# This will run forever
# This will run forever
# This will run forever
# This will run forever

count = 0
while count <= 10:
      guess = int(input(" Enter a number: "))
      if guess == 0:
          break  # exit the loop if guess is 0
      elif guess < 0:
          print(" Negative number, try again.")
          continue  # skip the rest of the loop and start from the beginning
      else:
            print(f" You entered: {guess}")
