import pymysql

db_ip="192.168.38.148"

def Create_D(name):
    conn=pymysql.connect(host=db_ip,port=3306,user='root',password='',charset='utf8')
    cursor=conn.cursor()
    sql=f"DROP database IF EXISTS `{name}`;"
    cursor.execute(sql)
    sql=f"create database `{name}`;"
    cursor.execute(sql) 
    cursor.close()
    conn.close()


Create_D("test")