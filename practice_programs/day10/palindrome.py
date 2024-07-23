def palindrome(num):
    result=""
    if(len(num)==1):
        result=num
    else:
        i=0
        print(len(num)//2)
        while i < len(num):
            if num[i] == num[len(num)-1-i]:
                result=result+num[len(num)-1-i]
            i = i+1
        print(result)
    if result == num:
        return num+" is a fibonnaci"
    else:
        return num+" is NOT a fibonnaci"

print(palindrome("minnimmmm"))

