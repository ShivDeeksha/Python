def sumDigit(str1):
  sum=0
  num='0123456789'
  for i in str1:
    if i in num:
      sum+=int(i)
  print("Sum of Integers in string:",sum)
str1=input("Enter a string: ")
sumDigit(str1)
