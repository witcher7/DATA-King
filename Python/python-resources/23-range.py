# 1. Ranges with start, stop and step
odd_nums = range(1, 100, 2)
even_nums = range(0, 101, 2)

print(list(odd_nums))
print(list(even_nums))


# 2. Index and count methods of the ranges
odd_nums = range(1, 100, 2)

print(odd_nums.index(51))
print(odd_nums.count(50))
print(odd_nums.count(51))

print(odd_nums.start)
print(odd_nums.stop)
print(odd_nums.step)


# 3. Range with start and stop
my_range = range(5, 8)

print(my_range.start)
print(my_range.stop)
print(my_range.step)


# 4. Conversion of the range to list, tuple or set
odd_nums = range(1, 100, 2)

print(list(odd_nums))
print(tuple(odd_nums))
print(set(odd_nums))
print(dict(odd_nums))  # TypeError
