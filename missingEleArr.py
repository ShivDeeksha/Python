import numpy as np

def allSum(n):
  sum=0
  for i in range (1,n+1):
    sum+=i
  return sum
  
arr=np.array([])
print("Find one missing number from entered array: \nNote: Please don't include duplicate Elements\n")
n=int(input("Enter the size of array (1-100): "))
print("Enter elements(1-",n,"): ")
sum=allSum(n)
for i in range(1,n):
  x=int(input())
  arr=np.append(arr,x)
arsum=0
for i in range(0,n-1):
  arsum+=arr[i]
if sum==arsum:
  print("No value is missing!")
else:
  print(int(sum-arsum),"is missing!")
