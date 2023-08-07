import numpy as np
n=int(input("Enter the size of array: "))
arr=np.array([])
print("Enter Elements:")
for i in range(0,n):
  x=int(input())
  arr=np.append(arr,x)
  arr=np.asarray(arr,dtype='int')
arr=set(arr)
arr=list(arr)
x=int(input("Enter a Value:"))
print("\nPair (a,b) such that a+b=",x,"are:")
for i in range (len(arr)):
  for j in range(len(arr)):
    if arr[i]+arr[j]==x:
      print("(",arr[i],",",arr[j],")")
