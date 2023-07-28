#Reverse in int
def int_rev(num):
  rev=0
  while num!=0:
    rev=rev*10+num%10
    num=num//10
  
  print("Reversed number: ",rev)
#Reverse in string
def str_rev(str):
  rev=''
  for i in str:
    rev=i+rev
  print("Reversed String: ",rev)
  
num=int(input("Enter any number: "))
int_rev(num)
str_rev(str(num))
