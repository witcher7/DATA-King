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
fig, (ax1,ax2) = plt.subplots(2,1, sharex=True)
ax1.scatter(values,squares)
ax1.set_title('Square numbers')
ax2.scatter(values,cubes)
ax2.set_title("Cube numbers")
plt.show()


      
plt.scatter()
Now if we want to plot individual points rather than connecting them using a line, we can use another function called scatter which takes the same input format.
#Plotting 4 Graphs in one plane
plt.plot([1,2,3,4],[1,4,2,3], c="lightblue") # c parameter is for defining color
plt.plot([1,2,3,4],[4,1,3,2], c="lightgreen")
plt.scatter([1,2,3,4],[1,4,2,3], c="darkblue")
plt.scatter([1,2,3,4],[4,1,3,2], c="darkgreen")
plt.show()
plt.scatter([1,2,3,4],[1,4,2,3])
plt.show()


plt.scatter([5,3,4,1,2],[2,3,4,3,5], c =["red","blue","green","red","black"])
plt.show()


Similarly, we have some other data visualisation functions like : BarGraphs, PieCharts, etc. So let’s try and plot each of them and we can use another function called subplot to plot multiple graphs in a single plot.

There are tons of other parameters too in these plots, that can make the representation more representative and useful. For eg:

plt.xlabel("X - Axis") –> Used to represent X-Axis label

plt.ylabel("Y - Axis") –> Used to represent Y-Axis label

plt.title("Graph Title") –> Used to give graphs a Title

plt.legends() –> Used to define a legend for graph.

import numpy as np
plt.figure(figsize=(15,5))

# ---Bar Graph at 1st index of subplot---
plt.subplot(1,2,1)

Products = np.array(["P1","P2","P3","P4","P5"])
Sale2020 = np.array([200,100,400,100,400])
Sale2021 = np.array([300,200,300,400,300])

plt.title("Product Sales in 2020 v/s 2021")
plt.xlabel("Product Names")
plt.ylabel("Sale Quantity")

plt.bar(Products,Sale2020, align = 'edge' ,width = 0.5, label="2020 Sales")
plt.bar(Products,Sale2021, align = 'center',width = -0.5, label="2021 Sales")
plt.legend()



# --- Pie Chart at 2nd index of subplot ---
plt.subplot(1,2,2)
plt.title("Market Share of the Investors")
Investors = ["A","B","C","D","E"]
Share = [40,25,20,10,5]
plt.pie(Share, labels = Investors,explode=[0,0,0,0,0.2], normalize=True)


plt.show()


data = {
    'Year': [2001,2002,2003,2004,2005],
    'Sales': [100,150,130,180,200,210]
}
df= pd.DataFrame(data)
df.plot(x="Year",y = "Sales",Kind = 'line')
df.title('Yearly Sales')

df= pd.DataFrame(data)
df.plot(x="Year",y = "Sales",Kind = 'Bar')
df.title('Yearly Sales')

df= pd.DataFrame(data)
df.plot(y = "Sales",Kind = 'pie',labels=df['Year'])
df.title('Yearly Sales')

data = {
    'Age': [10,20,30,40]
}
df = pd.DataFrame(data) 
df.plt(y="age",kind = 'hist')
plt.title('Age Distribution')


data = {
    'Category': ['First','First','Second','Third','Third'],
    'Value': [10,20,30,25,45,50]
}
df = pd.DataFrame(data) 
df.boxplot(by='Category',column='Value')
plt.title('Values Distribution by category')


# import pandas as pd
import matplotlib.pyplot as plt  
df = pd.read_csv('csv',index_col=0)
df.plot(y='YearTotalmm')

df.drop(columns=['YearTotalmm'].plot())
plt.show()

df.T.plot(y=[1901,1902],kind ='area')