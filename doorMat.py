print("Enter height and width of doormat: ",end='')
r,c=input().split()
r=int(r)
c=int(c)
s='.|.'
for i in range(1,r,2):
    print((i*s).center(c,"-"))
print("WELCOME".center(c,"-"))
for i in range(r-2,0,-2):
    print((i*s).center(c,"-"))
