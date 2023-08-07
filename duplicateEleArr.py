import numpy as np
n=int(input("Enter the size of array: "))
arr=np.array([])
dup=np.array([])
print("Enter Elements:")
for i in range(0,n):
  x=int(input())
  arr=np.append(arr,x)
dup=np.array([])
print("\nMultiple Occuring Elements are: ")
for i in range (n):
  flag=0
  if arr[i] not in dup:
    for j in range(n):
      if arr[i]==arr[j]:
        flag+=1
        dup=np.append(dup,arr[i])
    if flag>1:
      print(int(arr[i]),":-",flag,"times.")
    
