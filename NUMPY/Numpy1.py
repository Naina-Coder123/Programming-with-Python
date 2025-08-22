#creating the numpy 1 d array
import numpy as np; # pyright: ignore[reportMissingImports]
n1=np.array([1,2,3,4])
print(n1)
#2 D array
n2=np.array([[1,2,3,4],[3,4,5,6]])
print(n2)
#Attributes of N dimensional array
#shape
#size
#dimension
#datatype
print(n2.shape) #no of rows and no of columns
print(n2.size) #no of elements
print(n2.ndim) # no of dimension
print(n2.dtype) # dataype of the N dimensional array
# create 2 1D array of elements and apply vector operations like addition and subtractions
n3=np.array([6,7,8,9])
n4=np.array([9,8,7,6])
n5=(n3+n4)#addition
n6=(n3-n4)#subtraction
n7=(n3*n4)#multiplication
n8=(n3//n4)#division
print(n5)
print(n6)
print(n7)
print(n8)

# to create the array of zeros
c1=np.zeros((2,3))
print(c1)

# to create the array of ones

c2=np.ones((3,2))
print(c2)

#to create 3 d array
c3=np.zeros((4,3,2))
print(c3)
# 4 heights of 2 d object
# 3 rows
# 2 columns

# create an identity matrix using eye method

c4=np.eye(3)# gives identity matrix in which Aij i=j
print(c4)

# 
print(n1>15) # work on single element

# apply logical not operation on an input array

n2=np.logical_not(c1.astype(int))
print(n2)

#numpy array supports shallow copy and deep copy
# create an aray of 3 elements 5 ,7,9 create deep copy and shallow copy of this array

a1=np.array([5,7,9])
print(a1.view())#shallow copy
print(a1.copy())# deep copy

# broadcasting

a2=np.array([3,4,5]);
a3=a2+5
print(a3)

# array reshape and flatten operation

#create a 2 d array (4,2) and reshape (2,4)
a4 = np.array([[1,2],[4,5],[6,7],[8,9]])
reshaped = a4.reshape((2,4))  # Reshape to 2 rows, 4 columns
print(reshaped)

flattened = a4.flatten()      # Flatten to 1D array
print(flattened)

# indexing and slicing
# consider a 2D array of shape (4,2) and 
print(a4[1:])
print(a4[1,1:3])






