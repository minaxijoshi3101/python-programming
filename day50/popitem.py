i=0
d={}
while i<26:
    d[chr(65+i)]=100+10*i
    i += 1
print(d.keys())
print(type(d.keys()))
print(d.values())
print(type(d.values()))
while len(d) != 0:
    print(d.popitem())
print(d)