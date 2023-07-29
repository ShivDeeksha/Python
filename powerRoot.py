def square(num):
  print("Square: ",num**2)
def cube(num):
  print("Cube: ",num**3)
def sqRoot(num):
  rt=num**(1/2)
  print("Square Root: ",round(rt,3))
def cuRoot(num):
  rt=num**(1/3)
  print("Cube Root: ",round(rt,3))

n=int(input("Enter number: "))
square(n)
sqRoot(n)
cube(n)
cuRoot(n)
