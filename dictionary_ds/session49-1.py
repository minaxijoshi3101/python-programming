student_dict={}
i=0
while True:
    key=input("Enter name of the student: ")
    value=int(input("enter marks: "))
    student_dict[key]=value
    option=input("Do you want to continue: 'Yes or No ': ")
    while True:
        if option.lower() == 'no':
            break
        elif option.lower() == 'yes' :
            break
        else:
            option=input("Please enter a valid option either 'yes or no'")
    if option.lower() == 'no':
        break
print(student_dict)