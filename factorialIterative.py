def factorial(num):
  fact=1
  for i in range(1,num+1):
    fact=fact*i
  print("Factorial of",num,"is",fact)

x=int(input("Enter a Number: "))
factorial(x)
    
