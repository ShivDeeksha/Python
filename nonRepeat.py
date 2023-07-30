def notRepeat(str1):
  new=''
  for i in str1:
    if i not in new:
      new+=i
  print("\nString with non-repeating characters:",new)

str1=input("Enter a String: ")
notRepeat(str1)
