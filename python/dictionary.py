# it is a collection of data or data structure
# mutable means the data can be changed whenever we want to update
# iterable through loops
# it stores data as key value pair 
student = {
    'id': 425,
    'name': 'Rishabh',
    'course': 'python'
}   
print(student) # {'id': 425, 'name': 'Rishabh', 'course': 'python'}

# TO ACCESS  SPECIFIC VALUE
student['name']
student['course']

# To print only keys
student.keys() # dict_keys(['id', 'name', 'course'])

# To print only values
student.items()

## Adding more key value pair to existing dict
student['email'] = 'gulati7@gmail.com'
print(student) # {'id': 425, 'name': 'Rishabh', 'course': 'python', 'email': 'gulati7@gmail.com'}

## All dictionaries methods 
my_dict = {'1': 'Geeks', '2': 'For', '3': 'Geeks'}
my_dict.clear()
print(my_dict) # {}
    
d = {'Name': 'Ram', 'Age': '19', 'Country': 'India'}
print(d.get('Name')) # Ram
print(d.get('Gender')) # None


#d = {'Name': 'Ram', 'Age': '19', 'Country': 'India'}
print(list(d.items())[1][0]) # Age
print(list(d.items())[1][1]) # 19

d = {'Name': 'Ram', 'Age': '19', 'Country': 'India'}
print(list(d.keys())) # ['Name', 'Age', 'Country']

d1 = {'Name': 'Ram', 'Age': '19', 'Country': 'India'}
d2 = {'Name': 'Neha', 'Age': '22'}

d1.update(d2) # updates d1 with d2 values
print(d1) # {'Name': 'Neha', 'Age': '22', 'Country': 'India'}

d = {'Name': 'Ram', 'Age': '19', 'Country': 'India'}
d.pop('Age')
print(d) # {'Name': 'Ram', 'Country': 'India'}

d = {'Name': 'Ram', 'Age': '19', 'Country': 'India'}
val = d.popitem()
print(val) # ('Country', 'India')

val = d.popitem()
print(val) # ('Age', '19')