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
  return hcf

def hcf_lst(lst):
  hf=hcf(lst[0],lst[1])
  if len(lst)==2:
    print("HCF:",hf)
  for i in range(0,len(lst)-1):
    hf=hcf(hf,lst[i+1])
    if hf==1:
      print("HCF:",hf)
  print("HCF:",hf)

n=int(input("Enter the size of List: "))
lst=[]
print("Enter Elements: ")
for i in range(0,n):
  x=int(input())
  lst.append(x)
print("List: ",lst)

hcf_lst(lst)
