def fibonicci(num):
    list=[0,1]
    for i in range(num) :
        list.append(list[-1]+list[-2])
        i=i+1
    print(list)
    return list

fibonicci(4)

