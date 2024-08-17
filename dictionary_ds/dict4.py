d={}
while len(d) < 4:
    name=input("enter name of the student ")
    marks=input("enter marks of the student ")
    d[name]=marks

print("Name\t\tMarks")
print("#"*(30-5))
for k in d:
    print("{}\t\t{}".format(k,d[k]))
print("#"*25)