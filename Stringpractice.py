message = "Hi, \"These are apples\""
print (message)

message2 = 'Hi, "These are apples" '
print (message2)

#multi-line string using triple single quotes ir double quotes
chat = """ Hi,
          My name is Minaxi.
          I am from INDIA
        """
for character in chat : 
    print (character)

name="minaxi, joshi"
print(name[0:6])

print(len(name))
print(name[:])

print(name[0:-5])

name2="minaxi"
print(name2[-4:-2])

print(name2.upper()) #a new string will be created. It wont change the existing string

print(name2) #Strings are immutable

str1="Hello !!!!"
print(str1.rstrip("!"))

str2= "Silver Spoon"
print(str2.replace("sp","M"))

print(str2.split(" "))
str3=str2.split(" ")
print(str3[0])

blogHeading = "hi, this is sEH"
print(blogHeading.capitalize())

print(blogHeading.capitalize().center(50))

print(str1.endswith("!!"))

str4="welcome to SEH!!!"
print(str4.endswith("to",4,10))

str5="He's name is Aadu. He's a cute boy."
print(str5.find("is"))
print(str5.index("is"))
str6="We wish you a merry christmas \n"
print(str6.isprintable())

print(str6.istitle())

f = open("hello.py",'r')
print(f)