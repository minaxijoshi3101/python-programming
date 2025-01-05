d={
}
d[100]="min"
d[200]="an"
d[300]="sum"
print(d)
key=int(input("inter key to find the value: "))
if key in d:
    print(d[key])
else:
    print("specified key not available")