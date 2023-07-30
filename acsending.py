def acsending(str1):
  lst = list(str1)
  lst.sort()
  new = ''
  for i in range(len(lst)):
    new += lst[i]
  print("Acsending Order:", new)
str1 = input("Enter a String: ")
acsending(str1)
