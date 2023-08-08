def count_substring(string, sub_string):
    count=0
    nstring=string
    for i in range(len(string)+1):
        if nstring.startswith(sub_string):
            count+=1
            nstring=string[i+1:]
        else:
            nstring=string[i+1:]
    return count
string=input("Enter a string: ")
sub_string=input("Enter a substring: ")
print(sub_string,"occured",count_substring(string,sub_string),"times")
