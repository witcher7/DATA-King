# 1. Plus operator
my_name = 'Bogdan'
my_hobby = 'running'
time = 8

info = my_name + ' likes ' + my_hobby + ' at ' + str(time) + " o'clock"
print(info)


# 2. f-string
my_name = 'Bogdan'
my_hobby = 'running'
time = 8

info = f"{my_name} likes {my_hobby} at {time} o'clock"
print(info)


# 3. format string method
my_name = 'Bogdan'
my_hobby = 'running'
time = 8

info = "{} likes {} at {} o'clock".format(my_name, my_hobby, time)
print(info)


# 4. string interpolation
info = "%s likes %s at %s o'clock" % (my_name, my_hobby, time)
print(info)
