def int_rev(num):
  rev=0
  while num!=0:
    rev=rev*10+num%10
    num=num//10
  return rev
num=int(input("Enter a number: "))
if num==int_rev(num):
  print("The number is a Palindrome")
else:
  print("The number is not a Palindrome")
