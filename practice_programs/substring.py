""" main_str=input("Enter a string ")
sub_str=input("Enter a substring")
begin=0
end=len(main_str)
#flag=str.find(sub_str)
#print(flag)
flag=False
pos=-1
n=len(main_str)
count=0
while True:
    pos=main_str.find(sub_str,pos+1,n)
    if pos==-1 :
        break
    print("found at index ",pos)
    flag=True
    count=count+1
if flag == False :
    print("Not found")
print("The number of occurances ",count)

#Method 2
print(main_str.count(sub_str,begin,end+1))
"""
s="learning java"
rs=s.replace("java","python")
print(s,"address of rs is ",id(s))
print(rs,"address of rs is ",id(rs))