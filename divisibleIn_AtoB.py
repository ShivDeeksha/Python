print("Get total number of number divisible by a number in given rnage of numbers.\n\n")
a=int(input("Enter the start of the range: "))
b=int(input("Enter the end of the range: "))
num=int(input("Enter the number: "))
li=[]
for i in range(a,b+1):
  if i%3==0:
    li.append(i)
print("\n",len(li),"numbers are divisible by",num)
