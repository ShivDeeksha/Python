def add(x,y):
  
  while(y!=0):  
    carry = x & y 
    x = x ^ y
    y = carry << 1
  print("Sum:",x)

x=int(input("Enter Number: "))
y=int(input("Enter Number: "))
add(x,y)
