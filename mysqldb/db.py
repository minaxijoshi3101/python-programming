import pymysql

con=pymysql.connect(host='192.168.18.7',database='sehdb',user='remoteuser',password='remoteuser')
crsr=con.cursor()
con.commit()
#crsr.execute("create table employees(eno int(5) primary key,ename varchar(20),esal double(10,2), eaddr varchar(40))")
#if con is not None:

#WAP to fetch data from employees
query="select * from employees"
crsr.execute(query)
data=crsr.fetchall()
#data is in the form of tuple of tuples
print(data)
#To print each row:
for row in data:
    print("Employee ID   ",row[0])
    print("Employee Name   ",row[1])
    print("Employee salary   ",row[2])
#print("Table created successfully!!!")
crsr.close()
con.close()

