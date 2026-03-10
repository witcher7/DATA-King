import re  
my_string = "My name is Bodgan"
res = re.search("Bodgan$", my_string)
print(res) 
print(type(res))