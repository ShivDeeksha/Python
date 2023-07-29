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
  return lcm
def hcf(a,b):
  hcf=(a*b)//lcm(a,b)
  print("HCF:",hcf)

x,y=input("Enter two Numbers: ").split()
x=int(x)
y=int(y)
hcf(x,y)
