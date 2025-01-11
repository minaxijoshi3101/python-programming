n=int(input('Enter no of students:'))
d={}
for i in range(n):
    name=input('Enamr student name:')
    marks=int(input('Enter marks of student:'))
    d[name]=marks
print(d)
#student marks as per student name as input
while True:
    s_name=input('Student Name whose masrks you want to see:')
    if s_name.casefold() in d:
        print('Marks of student {} are {} '.format(s_name,d[s_name]))
    else:
        print('Student name not found')
    option=input('Do you want to continue? Y|n')
   
    while option.lower() not in ['y','n']:
        option=input("Please enter a valid option 'y' or 'n'")
    if option.lower() == 'n':
        break
print('Thank you for using the program')