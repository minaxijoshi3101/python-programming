d={}
while True:
    name=input("enter name of the student ")
    marks=input("enyer marks of the student ")
    d[name]=marks
    print("student record inserted successfully!!")
    option=input("Do you wanna continue? enter [yes|no]")
    while option.lower() not in ['yes','no']:
        #print("You have entered wrong option. Please enter [yes|no]")
        #option=input()
        option=input("You have entered wrong option. Please enter [yes|no]")
    if(option.lower()=="no"):
        break
print(d)