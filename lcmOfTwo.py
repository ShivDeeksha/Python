def lcm(a,b):
  if a>b:
    great=a
  else:
    great=b
  while(True):
    if((great%a==0) and (great%b==0)):
      lcm=great
      break
    great+=1
  print("LCM:",lcm)

x,y=input("Enter two Numbers: ").split()
x=int(x)
y=int(y)
lcm(x,y)
