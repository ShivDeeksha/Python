def wrap(string, max_width):
    new=""
    for i in range(0,len(string)+1,max_width):
        new=new+string[i:i+max_width]+"\n"
    return new
string=input("Enter a String: ")
max_width=int(input("Enter the Max width at each line: "))
print("Text Wraped:\n",wrap(string,max_width),sep='')
