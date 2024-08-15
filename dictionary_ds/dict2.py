d={}
while True:
    name=input("enter name of the student ")
    marks=input("enyer marks of the student ")
    d[name]=marks
    option=input("Do you wanna continue? enter [yes|no]")
    if(option.lower()=="no"):
        break
    elif(option.lower()!="yes" | option.loweer()!="no"):
        print("wrong entry. enter [yes|no]")
print(d)