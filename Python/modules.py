# module_one.py 
def print__name():
    print(name) 

# module_two.py
import module_one as n 
print(module_one.__name__)
print(type(module_one))
print(dir(module_one))
module_one.print__name("Rishabh")
n.print__name("Rishabh") # if module is imported with as alias 
