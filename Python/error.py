# # Try and except
# try: 
#       # execution of a code block 
#      pass 
# except ErrorType:
#      # This block will executed in case of errors in the try block 
#      pass 

try:
    print(10/0)
except ZeroDivisionError as e:
    print(e)
    print("Error in division by zero!")
except TypeError as e:
    print(e)


try:
    print(10/10)
except (TypeError, ValueError) as e:
    print(e)
else:
    print("There was no error!")
finally: 
    print("Continue") # This block will be executed in any case 


# Catching any error in the except block
try: 
    print(10/0)
except Exception as e: 
    print(e)



## error generation 
def divide_nums(a,b): 
    if b == 0:
        raise TypeError("Second argument cant be 0")
    return a / b 