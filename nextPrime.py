def isPrime(n):
  num=n
  flag=0
  for i in range(1,num+1):
    if num%i==0:
      flag+=1
  if flag==2:
    print(num,"is a Prime Number")
    return
  else:
    print(num,"is not Prime Number")
    notPrime(num+1)

def notPrime(n):
  num=n
  flag=0
  for i in range(1,num+1):
    if num%i==0:
      flag+=1
  if flag==2:
    print(num,"is next Prime Number")
    return
  else:
    notPrime(num+1)

num=int(input("Enter a number: "))
isPrime(num)
