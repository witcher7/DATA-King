my_nums = [10, 3, 100, 35]

print(my_nums)
print(len(my_nums))
my_nums.pop(2)
print(my_nums)
print(len(my_nums))


my_nums = [10, 3, 100, 35]

my_nums.extend([34, 62])
print(my_nums)


my_nums = [10, 3, 100, 35, 100]
print(my_nums.index(100))


my_nums = [10, 3, 100, 35, 100]

my_nums.clear()
print(my_nums)
my_nums.append(50)
print(my_nums)


my_nums = [10, 3, 100, 35, 100]
other_nums = [351, 245, 425]

merged_nums = my_nums + other_nums
# merged_nums = my_nums.__add__(other_nums)
print(merged_nums)
print(my_nums)
print(other_nums)


my_nums = [10, 3, 100, 35, 100]

my_nums[2] = 0
print(my_nums)


my_list = [True, None, 'abc', 10, 10.5, [1, 2], {'name': 'Bogdan'}]
print(my_list)
