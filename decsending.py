def descending(str1):
  lst = list(str1)
  lst.sort()
  lst.reverse()
  new = ''
  for i in range(len(lst)):
    new += lst[i]
  print("Descending Order:", new)
str1 = input("Enter a String: ")
descending(str1)
