# Numpy is a fundamental package for scientific computing in Python.
import numpy as np

# Creating a numpy array from a list
arr = np.array([1, 2, 3, 4, 5])
# All numpy methods are called using the np prefix
print("Numpy Array:", arr)
# Output: Numpy Array: [1 2 3 4 5]

## Below are all methods and functions of numpy with examples
# Array creation
zeros_array = np.zeros((2, 3))  # 2x3 array of zeros
ones_array = np.ones((3, 2))    # 3x2 array of ones
random_array = np.random.rand(2, 2)  # 2x2 array of random numbers
print("Zeros Array:\n", zeros_array)    
print("Ones Array:\n", ones_array)
print("Random Array:\n", random_array)
# Output:
# Zeros Array:      
# [[0. 0. 0.]
#  [0. 0. 0.]]

# Ones Array:
# [[1. 1.]  
#  [1. 1.]
#  [1. 1.]]
# Random Array:
# [[0.5488135  0.71518937]
#  [0.60276338 0.54488318]]
# Array operations
arr1 = np.array([1, 2, 3])
arr2 = np.array([1, 4, 5])
sum_array = arr1 + arr2  # Element-wise addition    
print("", sum_array)
# Output: [2 6 8]
diff_array = arr2 - arr1  # Element-wise subtraction    
print("", diff_array)
# Output: [0 2 2]
prod_array = arr1 * arr2  # Element-wise multiplication
print("Product Array:", prod_array)
# Output: Product Array: [ 1  8 15]
div_array = arr2 / arr1  # Element-wise division
print("Division Array:", div_array)
# Output: Division Array: [1. 2. 1.66666667]
# Statistical functions
mean_value = np.mean(arr)  # Mean of the array
median_value = np.median(arr)  # Median of the array
std_dev = np.std(arr)  # Standard deviation of the array
print("Mean:", mean_value)
print("Median:", median_value)
print("Standard Deviation:", std_dev)
# Output:
# Mean: 3.0 
# Median: 3.0
# Standard Deviation: 1.4142135623730951
# Reshaping arrays
reshaped_array = arr.reshape((5, 1))  # Reshape to 5x1 array
print("Reshaped Array:\n", reshaped_array)  
# Output:
# Reshaped Array:   
# [[1]
#  [2]  
#  [3]
#  [4]
#  [5]]
# Indexing and slicing
print("First element:", arr[0])  # First element
print("Elements from index 1 to 3:", arr[1:4])  #
# Output:
# First element: 1  
# Elements from index 1 to 3: [2 3 4]
# Boolean indexing
bool_idx = arr > 2  # Boolean array
filtered_array = arr[bool_idx]  # Filtered array
print("Filtered Array (elements > 2):", filtered_array)
# Output: Filtered Array (elements > 2): [3 4 5]
# Output:
# This will raise an error because x is not defined outside the function
print(" Please enter a positive number.")    