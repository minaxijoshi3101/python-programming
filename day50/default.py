d1={65:'A',66:'B',67:'C'}
d1.setdefault(68,'D')
print(d1)

d2={97:'a',98:'b',99:'c'}
d1.update(d2)
print(d1)
print(d2)
print(id(d2))

d3=d2.copy()
print(d3==d2)

print(id(d2)==id(d3))

d4=d2
print(d4)
print(id(d4))

print(d4==d2)
print(id(d4)==id(d2))