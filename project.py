# a basic numpy and panda project

import numpy as np 
import pandas as pd  

#a = np.array([1, 2, 3, 4, 5])
#b = np.array([1, 3, 4, 5,  6])
#print(a*b)
#print(a.dtype) # for checking the size
#print(b.dtype)
#print(a.nbytes)
#x = np.zeros((2,3, 2,3))
#print(x)
#y = np.ones((4,2,2))
#print(y)

a = np.rand.randint(10, 35, size = 30)
mean_temp= np.mean(a)
median_temp = np.median(a)
standard_deviation = np.std(a)

hottest_temp = np.max(a)
coldest_temp = np.min(a)

number_of_day_above = np.sum(a > 30)
print(f"Mean temp : {mean_temp:.2f}c")
print(f"the median temp is : {median_temp:.2f}c")
print(f"the standard deviation is : {standard_deviation:.2f}")
print(f"the hottest temp is : {hottest_temp:.2f}c")
print(f"the coldest temp is : {coldest_temp:.2f}c")
print(f"the number of days above 30 are : {number_of_day_above}")


a = np.random.randint(1, 10, (3, 3))
b = np.random.randint(1, 10, (3, 3))
sum = a + b
subtract = a - b
multiply = a * b
matrix_mult = a @ b
multiply_vector = np.matmul(a, b)
det_a = np.linalg.det(a)
inv_a = np.linalg.inv(a)
print(f"the  sum is :\n ",sum)
print("subtraction value :\n", subtract)
print(f"the multiplication is :\n", multiply)
print(f"the multiplication of the vector is :\n", multiply_vector)
print(f"the matrix multiplication is :\n", det_a)
print(f"the inverse is : \n", inv_a)


data = {"Name" : ["john", "alice", "victor", "bob", "emily"], "age" : [25, 12, 40, 42, 50], "salary" :[7000, 5000, 2450, 1980, 6000], "department" : ["IT", "HR", "IT", "Finance", "Marketing"]}
df = pd.DataFrame(data)
print(df)










