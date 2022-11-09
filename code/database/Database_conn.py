import pymysql


# Change the following to your own database connection info
host = 'localhost'
user = 'root'
password = ''


class my_sql():
    def __init__(self, database_name):
        self.database_name = database_name

    def Create_Database(self):
        conn = pymysql.connect(host=host, user=user,
                               password=password, charset='utf8')
        cursor = conn.cursor()
        cursor.execute("DROP DATABASE IF EXISTS %s" % self.database_name)
        cursor.execute("CREATE DATABASE %s" % self.database_name)
        cursor.close()
        conn.close()

    def Drop_Database(self):
        conn = pymysql.connect(host=host, user=user,
                               password=password, charset='utf8')
        cursor = conn.cursor()
        cursor.execute("DROP DATABASE IF EXISTS %s" % self.database_name)
        cursor.close()
        conn.close()

    def Drop_table(self, table_name):
        conn = pymysql.connect(host=host, user=user, password=password,
                               database=self.database_name, charset='utf8')
        cursor = conn.cursor()
        cursor.execute("DROP TABLE IF EXISTS %s" % table_name)
        cursor.close()
        conn.close()

    def Create_table(self, table_name, columns):
        self.Drop_table(table_name)
        conn=pymysql.connect(host=host, user=user, password=password, database=self.database_name, charset='utf8')
        cursor=conn.cursor()
        cursor.execute("CREATE TABLE %s (%s)" % (table_name,self.translate(columns)))
        cursor.close()
        conn.close()

    def translate(self,column_list):
        column = ''
        for i in column_list:
            column += i[0]+' '+i[1]+','
        return column[:-1]

    def Update_table(self,table_name,item):
        conn=pymysql.connect(host=host, user=user, password=password, database=self.database_name, charset='utf8')
        cursor=conn.cursor()
        values=""
        for i in item:
            values+=f'{i},'
        sql=f'insert into `{table_name}` values({values[:-1]});'
        try:
            cursor.execute(sql)
            conn.commit()
        except:
            conn.rollback()
        cursor.close()
        conn.close()

    def get_data(self,table_name):
        conn=pymysql.connect(host=host, user=user, password=password, database=self.database_name, charset='utf8')
        cursor=conn.cursor()
        cursor.execute(f'select * from {table_name}')
        data=cursor.fetchall()
        cursor.close()
        conn.close()
        return data
        
