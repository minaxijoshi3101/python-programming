#Important functions related to dictionary:
print("1. dict() function to create an empty dictionary:")
d=dict()
print(d)
d=dict({100:'minaxi',200:'amita'})
print(d)
print("{} ==> represents dictionary and set")
print("[] ==> represents List")
print("() ==> represents tuple")
d=dict([(100,"minaxi"),(200,"amita"),(300,"sumit")])
print("dictionary to store list of tuple objects is possible")
print(d)
print("\n")
print("dictionary to store tuple of tuple objects is possible")
d=dict(((100,"minaxi"),(200,"amita"),(300,"sumit")))
print(d)
print("\n")
print("dictionary to store list of list objects is possible")
d=dict([["min",100],["amita",200],["sumit",300]])
print(d)
print("\n")
print("dict to store tuples of list objects is possible")
d=dict((["amita",200],["minaxi",300],["sumit",400]))
print(d)
print("dict to store set of list obejcts is not possible as inside set every object should be hashable.")
print("\n")
print("dict to store set of tuple objects is possible")
d=dict({("amita",100),("minaxi",200),("sumit",300)})
print(d)
print(d.get('minai'))
#print(d['min'])
print(d.get("min",200))