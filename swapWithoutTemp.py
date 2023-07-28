def swap(a, b):
  a = a + b
  b = a - b
  a = a - b
  print("a:", a)
  print("b:", b)


def swap_temp(a, b):
  temp = a
  a = b
  b = temp
  print("a:", a)
  print("b:", b)


a, b = input("Enter two numbers: ").split()
a = int(a)
b = int(b)
print("a:", a)
print("b:", b)
print("\nAfter Swap (Without using temp)")
swap(a, b)
print("\nAfter Swap (With using temp)")
swap_temp(a,b)
