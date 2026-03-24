import matplotlib.pyplot as plt
values = [0,1,2,3,4,5,6,7,8,9,10,11,12]
sqaures = [pow(x,2) for x in values]
plt.plot(sqaures, values)
plt.show()
