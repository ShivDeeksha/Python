def removeCh(strng,x):
  new=''
  for i in strng:
    if(i!=x):
      new=new+i
  print("String Without",x,":",new)

strng=input("Enter a string: ")
x=input("Enter char to be removed: ")
removeCh(strng,x)
