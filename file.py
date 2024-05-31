f = open("myfile1.txt",'wt')
#content = f.read()
#print(content)
#Writing a file
f.write("Hi, this is a second file")
f.close()

#with option - no need to close the file explicitely
with open('myfile.txt','r') as f1:
    print(f1.read())