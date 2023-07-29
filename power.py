def power_loop(num,raised):
  pow=1
  for i in range (1,raised+1):
    pow=pow*num
  print("Answer:",pow)

x=int(input("Enter Base: "))
y=int(input("Enter Exponent: "))
power_loop(x,y)
