my_number = 10 
print(id(my_number))

new_number = 10
print(id(new_number))


## TO avoid mutation 
## User .copy() shallow copy
info = {
    'name': 'Bodgan',
    'age': 30 ,
    'reviews': []
}
info_copy = info.copy()
info_copy['reviews'].append('Great Product!')
print(info)
print(info_copy)


#  
## or user deepcopy 
from copy import deepcopy 
info = {
    'name': 'Bodgan', 
    "age": 30 ,
    'reviews': []
}
info_deepcopy = deepcopy(info)
info_deepcopy['reviews'].append('Great Product!')
print(info) 
print(info_deepcopy)
