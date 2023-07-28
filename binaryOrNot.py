def isBinary(num):
  n=str(num)
  yes=0
  for i in range(len(n)):
    if(n[i]=='1' or n[i]=='0'):
      yes=yes+1
      
  if yes==len(n):
    print("It is a Binary")
  else:
    print("It is not a Binary")

num=int(input())
isBinary(num)
