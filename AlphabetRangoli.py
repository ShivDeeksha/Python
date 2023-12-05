def print_rangoli(size):
    li="abcdefghijklmnopqrstuvwxyz"
   
    
    for i in range(size - 1, 0, -1):
        st = '-'.join(li[size - 1:i:-1] + li[i:size])
        print(st.center(size * 4 - 3, "-"))

    for i in range(size):
        st = '-'.join(li[size - 1:i:-1] + li[i:size])
        print(st.center(size * 4 - 3, "-"))
print_rangoli(17)

