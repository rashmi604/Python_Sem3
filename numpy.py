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

#Random Integer
print(np.random.randint(1,100,(4,4))) #4cross4matrix have values between 1 and 100

print(np.arange(1,20)) #print no from 1 to 20 excluding 20and 1 is included

print(np.arange(0,20,3)) #print no from 0 to 20 with a gap of 3

#Flatten 
print(arr.reshape(3,4))

arr.flatten()

#Indexing
arr=np.array([1,2,3,4])
print(arr(-1))

#2D array
arr=np.array([[1,,2,3],[4,5,6]])              0 1 2 #index
print(arr[0,1]) # 0isrow and 1 is indexing 0 [1,2,3],
                                          # 1 [4,5,6]
## so 2 is prinnted

arr= np.arange(10) # array([0,1,2,3,4,5,6,7,8,9])
print(arr[2:7])
print(arr[:5])
print(arr[5:])

a=np.array([1,2,3])
b=np.array([4,5,6])
print(a+b)
print(a-b)
print(a*b)
print(a/b)

import numpy as np
arr=np.array([10,20,30,40])
print(np.sum(arr))
print(np.mean(arr))
print(np.max(arr))
print(np.min(arr))
print(np.std(arr))
print(np.var(arr))

