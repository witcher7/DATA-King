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


