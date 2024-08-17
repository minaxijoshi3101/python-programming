#delete elements from the dictionary
d={} #or d=dict()
d[100]="minaxi"
d[200]="sumit"
d[300]="amita"
#invalid --> d2={1,2,3 : 'a','b','c'}
print("delete elements from the dictionary")
del_key=int(input("enter key which you want to delete"))
del d[del_key]
print(d)
print("Name\t\tMarks")
print("#"*25)
for k in d:
    print("{}\t\t{}".format(k,d[k]))
print("#"*25)
