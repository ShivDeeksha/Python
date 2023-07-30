def delVowel(str1):
  vowel="aeiou"
  for i in str1:
    if i in vowel:
      str1=str1.replace(i,'')
  print("String without Vowel:",str1)

str1=input("Enter a string: ")
delVowel(str1)
 
