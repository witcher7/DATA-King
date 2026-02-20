## CLASSES are templates for objects
## Instances are created based on the class
## Instances can have thier own attributes 

## Instances inherit class attributes 

class Car():
    def move(self):
        print("Car is moving")
    def stop(self):
        print("Car stopped")


mycar = Car()
print(mycar.move())
mycar.stop() # to call methods of class 



class User: 
    def info(self,username,email):
        print(f"User {username} has email {email}")
    
first_user = User() 
first_user.info("rg7","gulati.r7121@gmail.com")
first_user.username= "Rishabh"
first_user.email= "gulati.r7121@gmail.com"
print(first_user.__dict__)


## COnstrutor __init__ method 
class Comment:    # self variable references a specific instance of the class 
     def __init__(self,username,text): # helps to create new instance 
         self.text = text 
         self.name = "Gali"
         self.qty = 0
     def 