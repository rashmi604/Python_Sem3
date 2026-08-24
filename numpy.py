imprt numpy as np # to import numpy
arr = np.array([10,20,30,40]) #to create a 1D array in numpy or using numpy
print(arr)

#2D Arrray
arr = np.array([
    [1,2,3],
    [4,5,6]
])
print(arr)

#3D Array
arr = np.array([
    [
        [1,2],
        [3,4]
    ],
    [
    [5,6],
    [7,8]
    ]
])
print(arr)

print(arr.ndim)

print(arr.shape) #to check shape of array

print(arr.size) #to check size of an array

print(arr.dtype) #tells the data type of elements

print(arr.)

#Zeros
print(np.zeros((5,6))) #make all elements of an array zero

#Ones
print(np.ones((2,5)))

#Identity Matrix
print(np.eye(5)) #Matrix size 5 and all diagonal elements 1

#Full
print(np.full((3,3),100)) #all elements of array are 100

