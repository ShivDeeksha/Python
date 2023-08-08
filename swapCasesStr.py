
def swapCase(s):
    res=''
    for i in s:
        if i.isupper():
            res=res+i.lower()
        elif i.islower():
            res=res+i.upper()
        else:
            res=res+i
    return res
print(swapCase("Hello tHerE!!"))
