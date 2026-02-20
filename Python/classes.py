## CLASSES are templates for objects
## Instances are created based on the class
## Instances can have thier own attributes 

## Instances inherit class attributes 

# class Car():
#     def move(self):
#         print("Car is moving")
#     def stop(self):
#         print("Car stopped")


# mycar = Car()
# print(mycar.move())
# mycar.stop() # to call methods of class 



# class User: 
#     def info(self,username,email):
#         print(f"User {username} has email {email}")
    
# first_user = User() 
# first_user.info("rg7","gulati.r7121@gmail.com")
# first_user.username= "Rishabh"
# first_user.email= "gulati.r7121@gmail.com"
# print(first_user.__dict__)


# ## COnstrutor __init__ method for creating own objects
# class Comment:    # self variable references a specific instance of the class 
#      def __init__(self,username,text): # helps to create new instance 
#          self.text = text 
#          self.name = "Gali"
#          self.qty = 0

#      def upvote(self): 
#          self.qty += 1

# first_comment = Comment("First Customer")
# print(first_comment.qty)
# print(first_comment.name)


## Static method
# instance method operates on a specific object instance and has access to its data
# while static method is a utility function that does not access any instance or class-level data  
# - Has no this / self
# - Can only access static data

class Comment: 
    def __init__(self,txt):
        self.txt = txt
    
    def normal(self):
        print(self.txt)
        self.txt = "Raja"

    @staticmethod
    def get_text(txt):
        return f"{txt}"
    
mycomment = Comment("my")
mycomment.normal()
m1 = mycomment.get_text("Thanks!")
print(m1)
mycomment.normal()


## Class attributes 
class Comment: 
    total_comments = 0 

    def __init__(self,text): 
        self.text = text 
        self.votes_qty = 0
        Comment.total_comments +=1 
   


first_comment  = Comment("Balley")
print(first_comment.votes_qty)
print(first_comment.total_comments)
second_comment = Comment("Yoyo")
print(second_comment.votes_qty)
print(second_comment.total_comments)


## MAGIC METHOD 
class Comment: 
    total_comments = 0 

    def __init__(self,text): 
        self.text = text 
        self.votes_qty = 0
        Comment.total_comments +=1 
    def upvote(self):
        self.votes_qty += 1
    def __add__(self, other):  # Magic methods in classes
        return (f"{self.text} {other.text}")



## Inheritence from the other classes 
class ExtendedList(list): # WE ARE EXTENDING our list 
    def print_list_info(self): 
        print(f"List has {len(self)} elements")

custom_list = ExtendedList([3,5,2])
custom_list.print_list_info()



class User: 
    def __init__(self,username,email): 
        self.username = username 
        self.email = email 

class AdminUser(User):
    def __init__(self, username, email,role):
        super().__init__(username, email) # super is to call parent class objects
        self.role = role



## ENCAPSULATION 
# Its purpose is to hide internal data and protect it from accidental modification, while exposing only what is necessary.


class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner          # public attribute
        self._balance = balance     # protected attribute
        self.__pin = 1234           # private attribute

    def deposit(self, amount):
        self._balance += amount
        print(f"Deposited {amount}. New balance: {self._balance}")

    def withdraw(self, amount, pin):
        if pin == self.__pin:
            if amount <= self._balance:
                self._balance -= amount
                print(f"Withdrawn {amount}. Remaining balance: {self._balance}")
            else:
                print("Insufficient funds")
        else:
            print("Incorrect PIN")

    def get_balance(self):
        return self._balance
    

## POLYMORPHISM through method overriding (RUNTIME POLYMORPHISM)
# different classes implement the same method in their own way 
class Bird:
    def make_sound(self):
        return "Some generic bird sound"

class Sparrow(Bird):
    def make_sound(self):
        return "Chirp chirp"

class Eagle(Bird):
    def make_sound(self):
        return "Screech!"
    
birds = [Sparrow(), Eagle(), Bird()]

for b in birds:
    print(b.make_sound())

# Polymorphism Through Duck Typing
# Any object with the required method works — no need for inheritance
class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

class Human:
    def speak(self):
        return "Hello!"
    
for obj in [Dog(), Cat(), Human()]:
    print(obj.speak())



### A REAL BACKEND

class Payment:
    def pay(self, amount):
        raise NotImplementedError

class CreditCard(Payment):
    def pay(self, amount):
        print(f"Paid {amount} using Credit Card")

class UPI(Payment):
    def pay(self, amount):
        print(f"Paid {amount} using UPI")

class BankTransfer(Payment):
    def pay(self, amount):
        print(f"Paid {amount} using Bank Transfer")


def process_payment(payment_method, amount):
    payment_method.pay(amount)

process_payment(UPI(), 500)
process_payment(CreditCard(), 1000)
process_payment(BankTransfer(), 2000)
# Same function → different payment flows.
# This is exactly how real systems (banking, fintech, APIs) are designed
