d={}
i=0
while i<10:
    d[i]=i*2
    i += 1
print(d.keys())
print(type(d.keys()))
print(d.values())
print(type(d.values()))
for k in d.keys():
    print(k)
print("Print Values one by one")
for v in d.values():
    print(v)