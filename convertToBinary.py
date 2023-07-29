def toBinary(num):
  lst=[]
  while num>0:
    quo=num//2
    lst.append(num%2)
    num=quo
  binary=''
  for i in lst:
    binary=binary+str(i)
    
  print(x,"in binary:",binary[::-1])

x=int(input("Enter a number: "))
toBinary(x)
