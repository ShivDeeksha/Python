num=int(input("Enter a number: "))
s=str(num)
li=[]
for i in range(len(s)):
  li.append(int(s[i]))
sum=0
for i in range(len(li)):
  sum=sum+(li[i]**len(li))
if sum==num:
  print("The number is Armstrong Number")
else:
  print("The number is not a Armstrong Number")
