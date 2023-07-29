def lcm_lst(lst):
  lst.sort()
  great=lst[-1]
  while True:
    flag=0
    for i in lst:
      if(great%i==0):
        flag+=1
    if(flag==len(lst)):
      lcm=great
      break
    great+=1  
  print("LCM: ",lcm) 

n=int(input("Enter the size of List: "))
lst=[]
print("Enter Elements: ")
for i in range(0,n):
  x=int(input())
  lst.append(x)
print("List: ",lst)

lcm_lst(lst)
