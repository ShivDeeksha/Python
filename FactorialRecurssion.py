def fact(num):
  if num==1:
    return num
  else:
    return num*fact(num-1)

x=int(input("Enter a Number: "))
fact=fact(x)
print("Factorial of",x,"is",fact)
