# 1. Required parameters and keyword arguments
def product_price_info(product_title, product_price):
    print(f'{product_title} costs {product_price}$')


product_price_info(product_title="Bottle of water", product_price=2)


# 2. Gathering all keyword arguments into a dictionary
def product_price_info(**product):
    print(product)


product_price_info(product_title="Bottle of water",
                   product_price=2, product_availability=True)


# 3. Accessing values of the dictionary in the function
def product_price_info(**product):
    print(f"{product['product_title']} costs {product['product_price']}$")


product_price_info(product_title="Bottle of water", product_price=2)


# 4. Assigning values from the dictionary to the variables
def product_price_info(**product):
    title = product['product_title']
    price = product['product_price']
    print(f"{title} costs {price}$")


product_price_info(product_title="Bottle of water", product_price=2)
