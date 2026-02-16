# Lambda function 
#  lambda parameters: expression


## Lambda functions are always anonymous
## they dont have any name 
lambda a,b: a*b   


def greeting(greet):
    return lambda name: f"{greet},{name}!"

morning_greeting = greeting("Good Morning") # this is now a function
print(type(morning_greeting))



## 
my_nums = [3,4,10,200,-10,-3]
print(list(filter(lambda num: num%2==0, my_nums)))
