my_num = 1000
other_num = 100

res = my_num + other_num
print(res)


my_num = 1_000_000_000_000
other_num = 1_000

res = my_num / other_num
print(res)


input_str = input("Enter any number: ")
print(type(input_str))
try:
    input_num = int(input_str)
    print(type(input_num))
except ValueError:
    print("Not able to convert to int")
