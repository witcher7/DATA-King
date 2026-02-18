# # Decorators are helpful to increase function usage 

# def my_decorator(func):
#     def wrapper(*args, **kwargs):   
#         print(args) 
#         print(kwargs)
#         print("Happening before the function")
#         result = func(*args, **kwargs)
#         print("After the function")
#         return result
#     return wrapper

# @my_decorator
# def test_decorator(*args, **kwargs):
#     print("Hello")

# test_decorator(10,name="Rishabh")

def is_user_authenticated():
   return False 


def check_user_auth(fn):
   def wrapper(*args, **kwargs):
      if is_user_authenticated():
         print("User is authenticated!")
         return fn(*args, **kwargs)
      else: 
         raise Exception("User is not authenticated")
   return wrapper  
   

@check_user_auth
def do_sensitive_job():
   print("do_sensitive job results")

do_sensitive_job()