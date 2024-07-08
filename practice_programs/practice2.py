from random import *
i=0
while i<6:
    print(randint(0,9),end='')
    i+=1
print("\n")
for i in range(10):
    for i in range(6):
        print(randint(0,9),end='')
    print("\n")