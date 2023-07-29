def toOctal(num):
  lst=[]
  while num>0:
    quo=num//8
    lst.append(num%8)
    num=quo
  binary=''
  for i in lst:
    binary=binary+str(i)
    
  print(x,"in Octal:",binary[::-1])

x=int(input("Enter a number: "))
toOctal(x)
