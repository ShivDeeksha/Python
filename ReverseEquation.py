'''
Given a mathematical equation using numbers/variables and +, -, *, /. Print the equation in reverse.
'''
def rev(eq):
  x=eq.split()
  li=[]
  for i in x:
    if i.isnumeric():
      li.append(int(i))
    else:
      li.append(i)
  li.reverse()
  print("Your Reversed equation: ", end='')
  for i in range(0, len(li)):
    print(li[i],end='')
  return 0

print("Enter a equation with space before and after a operator:\n\n Example: 20 + 12 * 2 + 9\n\n")
eq=input("Your Equation: ")
rev(eq)
