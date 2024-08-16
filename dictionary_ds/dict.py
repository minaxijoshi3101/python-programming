d={} #or
d1=dict()
print(type(d))
d[100]="minaxi"
d[200]="sumit"
d[300]="amita"
print(d)
print(type(d[100]))
print(type(d1))
print(d[100])
key=300
if(key in d):
    print(d[key])
else:
    print("key is not available")
#invalid --> d2={1,2,3 : 'a','b','c'}

"""  if option.lower() == "yes":
            option="yes"
            break
        if option.lower() == "no":
            option="no"
            break """
