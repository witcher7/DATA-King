person_info = {
    'age': 20
}
if not person_info.get('name'):
    print("Name is absent")


# TERNARY OPERATOR

# Expression_1 if condition else Expression_2
mynumber = 100
print("is int") if type(mynumber) is int else print("not int")

