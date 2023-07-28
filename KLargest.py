'''
K largest element:
Given an array of N elements and a integer K, find K largest element from the array. The Output should be printed in descending order.
'''
# print("K largest element:\nGiven an array of N elements and a integer K, find K largest element from the array. \nThe Output should be printed in descending order.\n\n")
n=int(input("Enter Size of Array: "))
arr=[]
print("Enter elements: ")
for i in range(0,n):
  x=int(input())
  arr.append(x)
arr.sort(reverse=True)

k=int(input("Enter value of K: "))
for i in range(0,k):
  print(arr[i])
