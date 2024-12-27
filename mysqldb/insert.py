import pymysql

con=pymysql.connect(host="192.168.18.7",database='studentDB',user='remoteuser',password='remoteuser')
crsr=con.cursor()
con.commit()
query = "INSERT INTO student (student_name, student_password, student_mobile, student_email) VALUES ('minaxi', 'minaxi', 9999020508, 'minaxijoshi3101@yahoo.com')"
crsr.execute(query)
qury2="select * from student"
crsr.execute(qury2)
data=crsr.fetchall()
con.commit()
print(data)