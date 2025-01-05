d={1:'a',2:'b',3:'c'}
print(d.items())
print(type(d.items()))
for x in d.items():
    print(x)
    print(x[0])
print("keys")
for k,v in d.items():
    print(k)
    print('{}:{}'.format(k,v))

print(d.get(5,'Nahi hai'))