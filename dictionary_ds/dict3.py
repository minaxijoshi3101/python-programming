d={}
while True:
    name=input("enter student name")
    marks=input("enter marks of the student")
    d[name]=marks
    option=input("do you want to continue? enter [Yes|No]")
    while True:
        if option.lower() in ['yes','no']:
            break
        else:
            option=input("you have entered wrong option. please enter [yes|no]")
    if option.lower() == "no":
        break
print("Name\t\tMarks")
print("#"*30)
for k in d:
    print("{}\t\t{}".format(k,d[k]))
print("#"*30)