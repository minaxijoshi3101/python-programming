#######################################################################################
#Program to reverse each word of a string
#Hi This is Minaxi 
#o/p - iH sihT si ixaniM
str = "Hi This is Minaxi"
new_str_list = []
list_str = str.split()
for lst in list_str:
    i=len(lst)-1
    rev=""
    while i >= 0 :
        rev=rev+lst[i]
        i = i-1
    new_str_list.append(rev)
print(new_str_list)
