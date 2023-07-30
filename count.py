def countDisplay(str1):
  alpha=0
  digit=0
  sp=0
  nu=0
  al="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
  di='0123456789'
  for i in str1:
    if i==" ":
      nu+=1
    elif i in al:
      alpha+=1
    elif i in di:
      digit+=1
    else:
      sp+=1
  print("\n\nThe string contains: ")
  print("Alphabets:",alpha)
  print("Digits:",digit)
  print("Special Symbol:",sp)
  print("Blank Symbol:",nu)
str1=input("Enter a string: ")
countDisplay(str1)
