def isPrime(num):
  flag=0
  for i in range(1,num+1):
    if num%i==0:
      flag+=1
  if flag==2:
    print(num,"is a Prime Number")
  else:
    print(num,"is not a prime Number")

num=int(input("Enter a number: "))
isPrime(num)
