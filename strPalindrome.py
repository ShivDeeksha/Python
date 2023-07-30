def palindrome(str1):
    rev=''
    l=len(str1)
    for i in range(0,l):
        rev=rev+str1[i]
    if rev==str1:
        print("It is a Palindrome")
    else:
        print("It is not a Palindrome")

str1=input("Enter a string: ")
palindrome(str1)
        
