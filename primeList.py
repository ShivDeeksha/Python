def prime(num):
  flag=0
  for i in range(1,num+1):
    if num%i==0:
      flag=flag+1
  if flag==2:
    print(i)

x=int(input("Enter the start of range: "))
y=int(input("Enter the end of range: "))
print("Prime  number form",x,"to",y,"are: ")
for i in range(x,y+1):
  prime(i)
