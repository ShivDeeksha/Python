def swap(a,b):
  a=a+b
  b=a-b
  a=a-b
  print("a:",a)
  print("b:",b)

a,b=input("Enter two numbers: ").split()
a=int(a)
b=int(b)
print("a:",a)
print("b:",b)
print("\nAfter Swap:")
swap(a,b)
