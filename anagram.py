def anagram(str1,str2):
    l1=list(str1)
    l2=list(str2)
    l1.sort()
    l2.sort()
    flag=0
    for i in l1:
        for j in l1:
            if(i==j):
                flag+=1
    if flag==len(l1):
        print("Yes, these are anagram.")
    else:
        print("No, these are not anagram.")
            
            
    

str1=input("Enter first string: ")
str2=input("Enter second string: ")
anagram(str1,str2)
