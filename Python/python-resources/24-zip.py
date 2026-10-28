# 1. Zip object creation and its conversion to a list
products = ['phone', 'tablet', 'laptop']
quantities = [343, 13, 74]

products_qtys = zip(products, quantities)

print(products_qtys)
print(type(products_qtys))

products_qtys_list = list(products_qtys)
print(products_qtys_list)


# 2. Iteration over the zip object
products = ['phone', 'tablet', 'laptop']
quantities = (343, 13, 74)
tags = 'asd'

products_qtys = zip(products, quantities, tags)

for product in products_qtys:
    print(product)
    print(product[0])


# 3. Conversion of the zip object to a dictionary
products = ['phone', 'tablet', 'laptop']
quantities = (343, 13)

products_qtys = zip(products, quantities)

products_qtys_dict = dict(products_qtys)
print(products_qtys_dict)
