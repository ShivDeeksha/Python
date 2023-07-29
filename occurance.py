def occur(str1,x):
  count=0
  for i in str1:
    if i==x:
      count+=1
  print(x,"occured",count,"times")

str1=input("Enter a String: ")
x=input("Enter a char: ")
occur(str1,x)
