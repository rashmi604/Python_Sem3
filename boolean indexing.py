arr = np.array([10,20,30,40,50])
print(arr[arr>25])

#WHERE 
arr = np.array([10,20,30,40,50])
print(np.where(arr>20)) 

#SORTING
arr = np.array([5,2,9,1])
print(np.sort(arr))

#UNIQUE VALUES
arr = np.array([1,2,2,3,3,4])
print(np.unique(arr))

#CONCATENATE
a=np.array([1,2])
b=np.array([3,4])
print(a)
prit(b)
print(np.vstack((a,b)))

print(np.hstack((a,b)))

#SPLIT
arr=np.arange(8) # no from 0 to 8
print(np.split(arr,4)) # make 4 array [0,1],[2,3],[4,5],[6,7]

#BROADCASTING
arr=np.array([1,2,3])
print(arr+10) #[11,12,13] adds 1+10 ,2+10,3+10

#2D
A=np.array([[1],[2],[3]])
B=np.array([10,20,30])
print(A+B)




