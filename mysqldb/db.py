import pymysql
con=pymysql.connect(host='192.168.18.7',database='sehdb',user='remoteuser',password='remoteuser')
if con is not None:
    print("connected")
