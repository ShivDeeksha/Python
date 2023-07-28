num=int(input("Enter Elements in Sequence: "))
first=0
second=1
next=0
print("The first",num,'elements of the fibbonacci series are: \n')
print(first)
print(second)
for i in range(2,num):
  next=first+second
  first=second
  second=next
  print(next)
