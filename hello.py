from math import factorial
from unittest import result


""" def fact(num):
    print('finding factorail of ',num)
    if num==0:
        result=1
    else:
        result=num*fact(num-1)
    print("factorial of {} is {} ".format(num, result))
    return result

print(fact(5)) """

global fact
def factorial(num,fact=1):
    while(num>0):
        fact=fact*(num)
        num=num-1
    return fact

print(factorial(5))

