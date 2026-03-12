# numpy is a library for numerical computing in Python. It provides support for large, multi-dimensional arrays and matrices, along with a collection of mathematical functions to operate on these arrays efficiently.
import numpy as np

# ONE DIMENSIONAL ARRAY
nums_array = np.array([1, 2,])
print(nums_array)
# Output: [1 2]
num_array.shape
# Output: (2,)
num_array.ndim 
# Output: 1 # number of dimensions
num_array.size
# Output: 2 # number of elements in the array
num_array.dtype
# Output: dtype('int32') # data type of the elements in the array
num_array.itemsize 
# Output: 4 # size of each element in bytes
num_array.dtype.name 
# Output: 'int32' # name of the data type of the elements in the array

# TWO DIMENSIONAL ARRAY
two_dim_array = np.array([[1, 2], [3, 4]])
print(two_dim_array)
# Output: [[1 2]
#          [3 4]]
two_dim_array.shape
# Output: (2, 2) # shape of the array (number of rows,
two_dim_array.ndim 
# Output: 2 # number of dimensions 
two_dim_array.size
# Output: 4 # number of elements in the array
two_dim_array.dtype
# Output: dtype('int32') # data type of the elements in the array
two_dim_array.itemsize
# Output: 4 # size of each element in bytes
two_dim_array[0][1]
# Output: 2 # access the element at row 0, column 1

first = np.array([[1, 2, 3], [4, 5, 6]])
second = np.array([[7, 8, 9], [10, 11, 12]])
print(first, second)
result = first + second
print(result)
# Output: [[ 8 10 12]
#          [14 16 18]]

# concatenate two arrays
concatenated = np.concatenate((first, second), axis=0)  
print(concatenated)
# Output: [[ 1  2  3]
#          [ 4  5  6]
#          [ 7  8  9]
#          [10 11 12]]
concatenated = np.concatenate((first, second), axis=1)
print(concatenated)
# Output: [[ 1  2  3  7  8  9]
#          [ 4  5  6 10 11 12]]
concatenated = np.concatenate((first, second), axis=2)  
print(concatenated)
# Output: ValueError: all the input arrays must have same number of dimensions, but the array at index 0 has 2 dimension(s) and the array at index 1 has 2 dimension(s)


np.zeros((3,4),dtype = int) 
# array ([0,0,0,])
np.ones((3,4),dtype = bool)
# array [1,[1,[1]]]
np.random.random((3,4))

np.random.randint(10,20,size = (4,5))

np.arrange(8)
np.arrange(20).reshape([2,10])
np.arrange(20).reshape([2,2,5])

## CALCULATING TOTAL REVENUE
prices = np.array([19.99,29.99,14.99,9.99,24.99])
quantities = np.array([10,5,8,12,3])
prices * quantities
total_revenue = np.sum(prices*quantities,axis=0)

## ANALYSING Blog post stats 
views = np.array([100,500,800,1200,300,600])
max_views = np.max(views)
min_views = np.min(views)
average_views = np.round(np.mean(views),2)
total_views = np.sum(views)


## SPLITTING order into Batches 
order_id = np.array([1001,1002,1003,1004,1005,1006])
batches = np.split(order_id,3)
for batch in batches:
    print(batch)

### CATEGORIZING PRODUCT ratings 
ratings = np.array([4.5,3.2,1.5,2.5,4.7])
positive_ratings = ratings[ratings>=4.0]
negative_ratings = ratings[ratings<4.0]

## Calculate total and average quantities sold 
order_quantities = np.array([[5,3,2,7],[10,6,3,9]])
total_quantities = np.sum(order_quantities,axis = 0)
average_views_quantities = np.mean(order_quantities,axis = 0)
  