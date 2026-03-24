import matplotlib.pyplot as plt
values = [0,1,2,3,4,5,6,7,8,9,10,11,12]
sqaures = [pow(x,2) for x in values]
plt.plot(sqaures, values)
plt.show()

plt.scatter(sqaures, values)
plt.show()

plt.scatter(values,squares,c=sqaures,cmap=plt.cm.Blues,edgecolors='none',s=10)

values = list(range(200))
squares= [pow(values,2)for value in values]
cubes= [pow(values,3)for value in values]
plt.subplots(2,1, sharex=True)