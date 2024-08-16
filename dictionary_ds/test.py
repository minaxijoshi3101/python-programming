#check if given key already in dictionary:
d={100:"minaxi",200:"amita"}
key=int(input("enter a key you want to check"))
for k in d:
    print(type(k))
    if k==key:
        print("matched")
