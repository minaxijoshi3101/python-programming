#Write a program to reverse a given string
str1=input("enter a string: ")
print("*************reverse using slice operator*********")
print(str1[::-1])
print("**************using reversed function***************")
rs = reversed(str1) #type of output will be reversed object
print(type(rs))
output=''.join(rs)
print(output)
""" for ch in output :
    print (ch) """
print("**************reverse using for loop*************")
def reverse_string(input_string):
    reversed_string = ''
    for char in input_string:
        reversed_string = char + reversed_string #h+"", e+h, l+eh,l+leh,o+lleh =olleh
    return reversed_string

original_string = "hello"
reversed_string = reverse_string(original_string)
print(reversed_string)
print("***********using while loop*****************")
i=0 #for indexing
rs1=""
while i<len(str1) : #len(str) - to perform reverse
    rs1 = rs1+str1[(len(str1)-1-i)]
    i=i+1
print(rs1)

#or
j = len(str1)-1
rs2=""
while j>=0 :
    rs2=rs2+str1[j]
    j=j-1
print(rs2)
