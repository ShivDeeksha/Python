def toHex(num):
  hx = ''
  while num != 0:
    rem = num % 16
    if rem == 10:
      hx = 'A' + hx
    elif rem == 11:
      hx = 'B' + hx
    elif rem == 12:
      hx = 'C' + hx
    elif rem == 13:
      hx = 'D' + hx
    elif rem == 14:
      hx = 'E' + hx
    elif rem == 15:
      hx = 'F' + hx
    else:
      hx = str(rem) + hx
    num = num//16
  return hx

num=int(input("Enter a number:"))
print("Hexadecimal value of",num,"is",toHex(num))
