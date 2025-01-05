s=input('enter a string')
d={}
for ch in s:
    if ch in d:
        d[ch]=d[ch]+1
    else:
        d[ch]=1

print(d)