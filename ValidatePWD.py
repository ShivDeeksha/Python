print("Your password must contain atleast one lowercase letter, uppercase letter, one number and one special symbol(@$_)\n\n")
def validate():
  pwd=input("Enter Password: ")
  l,u,n,s=0,0,0,0
  small='abcdefghijklmnopqrstuvwxyz'
  upper='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
  number='0123456789'
  special='@$_'
  if len(pwd)>=8:
    for i in pwd:
      if (i in small):
        l=l+1
      if (i in upper):
        u=u+1
      if (i in number):
        n=n+1
      if(i in special):
        s=s+1
  
  if(l>=1 and u>=1 and n>=1 and s>=1 and (l+u+n+s==len(pwd))):
    print("Valid")
  else:
    print("Invalid try again!!\n\n")
    validate()

validate()
