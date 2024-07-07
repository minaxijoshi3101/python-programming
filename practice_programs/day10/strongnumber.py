#!/bin/bash
num=int(input("enter a number to check"))#145
sum=0
fact=1
tmp=num
while tmp>0 :
   remainer = tmp%10 #5
   while remainer>0:
        fact=remainer*fact #5 #20 #60 #120
        remainer -= 1 #4 3 2 1
        new_num=fact
   fact=1
   sum=sum+new_num #120
   tmp=tmp//10
"strong " if sum==num else "not"
print(str(num)+"is a strong numner" if sum==num else str(num)+" is a not strong numner")
#print(sum)
#print(type(sum))
""" if(sum==num):
    print(str(num)+"is a strong numner") """
