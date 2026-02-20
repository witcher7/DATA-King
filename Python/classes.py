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