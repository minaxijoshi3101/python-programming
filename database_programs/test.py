import pymysql
l=[]
con=pymysql.connect(host='192.168.18.2',port=3306,database='employeedb',user='root',password='root')
if con is not None:
    print('Connected successfully.')
crsr=con.cursor()
#crsr.execute("create table employees(enum int(20) primary key,ename varchar(20),esal double(20,2),eaddr varchar(20))")
#print("Table created successfully")
#query="insert into employees(enum,ename,esal,eaddr) values(%s,%s,%s,%s)"
""" records = [
    (100,'Minaxi',10500,'SGP'),
    (200,'Amita',11000,'noida'),
    (300,'Sumit',12000,'haldwani')
] """
#crsr.executemany(query,records)
crsr.execute("select * from employees")
data=crsr.fetchall()
print(data)

for row in data:
    print("Employee ID: ",row[0])
    print("Employee Name: ",row[1])
    print("Employee Slaray: ",row[2])
    print("Employee Address: ",row[3])
    print()
#con.commit()
#print("Records inserted successfully")
crsr.close()
con.close()