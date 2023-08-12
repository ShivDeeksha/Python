s1=input("Enter a String of len(n): ")
k=int(input("Enter K factor of n: "))
li=[]
for i in range (0,len(s1),k):
  s=s1[i:i+k]
  li.append(s)
u=[]
for i in li:
  n=''
  for j in i:
    if j not in n:
      n=n+j
  u.append(n)
for i in u:
  print(i)
      
