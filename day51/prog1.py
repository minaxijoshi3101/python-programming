d=eval(input('Enter Studetname{} and marks{} in dictionary format:'.format('\'','\'')))
print(d)
#student marks as per student name as input
s_name=input('Enter student name:')
if s_name in d:
    print('Marks of {}:{}'.format(s_name,d[s_name]))
