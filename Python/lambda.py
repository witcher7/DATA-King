# Lambda function 
#  lambda parameters: expression


## Lambda functions are always anonymous
## they dont have any name 
lambda a,b: a*b   


def greeting(greet):
    return lambda name: f"{greet},{name}!"

morning_greeting = greeting("Good Morning") # this is now a function
print(type(morning_greeting))
