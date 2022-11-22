import pymysql


# Change the following to your own database connection info
host = 'localhost'
# local
user = 'root'
password = ''
# server
# user = 'debian-sys-maint'
# password = 'P9l61rDpABnQXBq3'
# password = 'wgAkYmSE'

class my_sql():
    def __init__(self, database_name):
        self.database_name = database_name

    def execute_sql(self, sql):
        conn = pymysql.connect(host=host, user=user, password=password,
                               database=self.database_name, charset='utf8')
        cursor = conn.cursor()
        cursor.execute(sql)
        cursor.close()
        conn.commit()
        conn.close()

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
        conn = pymysql.connect(host=host, user=user, password=password,
                               database=self.database_name, charset='utf8')
        cursor = conn.cursor()
        self.Drop_table(table_name)
        cursor.execute("CREATE TABLE %s (%s)" %
                       (table_name, self.translate(columns)))
        cursor.close()
        conn.close()

    def translate(self, column_list):
        column = ''
        for i in column_list:
            column += i[0]+' '+i[1]+','
        return column[:-1]

    def Update_table(self, table_name, item):
        conn = pymysql.connect(host=host, user=user, password=password,
                               database=self.database_name, charset='utf8')
        cursor = conn.cursor()
        values = ""
        for i in item:
            values += f'{i},'
        sql = f'insert into `{table_name}` values({values[:-1]});'
        try:
            cursor.execute(sql)
            conn.commit()
        except:
            conn.rollback()
            with open("err.txt", "a", encoding="utf-8")as f:
                f.write(sql+"\n")
            print("error")
        cursor.close()
        conn.close()

    def get_data(self, table_name):
        conn = pymysql.connect(host=host, user=user, password=password,
                               database=self.database_name, charset='utf8')
        cursor = conn.cursor()
        cursor.execute(f'select * from {table_name}')
        data = cursor.fetchall()
        cursor.close()
        conn.close()
        return data

    def get_data_by_attr(self, table_name, attr_name, attr_value):
        conn = pymysql.connect(host=host, user=user, password=password,
                               database=self.database_name, charset='utf8')
        cursor = conn.cursor()
        cursor.execute(
            f'select * from {table_name} where {attr_name}="{attr_value}"')
        data = cursor.fetchall()
        cursor.close()
        conn.close()
        return data

    def get_specific_data(self, table_name, item):
        conn = pymysql.connect(host=host, user=user, password=password,
                               database=self.database_name, charset='utf8')
        cursor = conn.cursor()
        values = ""
        for i in item:
            values += f'{i},'
        cursor.execute(f'select {values[:-1]} from {table_name}')
        data = cursor.fetchall()
        cursor.close()
        conn.close()
        return list(data)

    def get_sepcific_data_by_attr(self, table_name, item, attr_name, attr_value):
        conn = pymysql.connect(host=host, user=user, password=password,
                               database=self.database_name, charset='utf8')
        cursor = conn.cursor()
        values = ""
        for i in item:
            values += f'{i},'
        cursor.execute(
            f'select {values[:-1]} from {table_name} where {attr_name}="{attr_value}"')
        data = cursor.fetchall()
        cursor.close()
        conn.close()
        return list(data)
        
    def Update_user(self, id, name, gender, telephone, password, brief):
        item = []
        item.append(id)
        item.append(f'"{name}"')
        item.append(f'"{gender}"')
        item.append(f'"{telephone}"')
        item.append(f'"{password}"')
        item.append(f'"{brief}"')
        self.Update_table("user", item)
    
    def Update_statistics(self,userid,score,start,end,duration,a1,a2,a3,a4,a5,b1,b2,b3,b4,b5,questionnum,rightnum,wrongnum,emptynum):
        item = []
        item.append(userid)
        item.append(score)
        item.append(start)
        item.append(end)
        item.append(duration)
        item.append(a1)
        item.append(a2)
        item.append(a3)
        item.append(a4)
        item.append(a5)
        item.append(b1)
        item.append(b2)
        item.append(b3)
        item.append(b4)
        item.append(b5)
        item.append(questionnum)
        item.append(rightnum)
        item.append(wrongnum)
        item.append(emptynum)
        self.Update_table("statistics", item)


def reset_book():
    tabname = "book"
    column = []
    column.append(['id', 'int'])
    column.append(['name', 'varchar(50)'])
    column.append(['author', 'varchar(50)'])
    column.append(['country', 'varchar(50)'])
    column.append(['publisher', 'varchar(50)'])
    column.append(['year', 'varchar(50)'])
    column.append(['page', 'varchar(50)'])
    column.append(['price', 'varchar(50)'])
    column.append(['frame', 'varchar(50)'])
    column.append(['category', 'varchar(50)'])
    column.append(['isbn', 'varchar(50)'])
    column.append(['star', 'float'])
    column.append(['comment_num', 'int'])
    column.append(['brief', 'varchar(9999)'])
    column.append(['douban_bookid', 'varchar(50)'])
    column.append(['link', 'varchar(50)'])
    column.append(['name_o', 'varchar(50)'])
    column.append(['trans', 'varchar(50)'])

    sql = my_sql("readbook")
    sql.Create_table(tabname, column)


def reset_user():
    tabname = "user"
    column = []
    column.append(['id', 'int'])
    column.append(['name', 'varchar(50)'])
    column.append(['gender', 'char'])
    column.append(['telephone', 'varchar(50)'])
    column.append(['password', 'varchar(50)'])
    column.append(['brief', 'varchar(1000)'])

    user1 = [1, '"castamere"', '"M"',
             '"13834230484"', '"aaa6953217"', '"xxxx"']
    user2 = [2, '"today_red"', '"F"',
             '"13686521434"', '"ZzZ123456"', '"xxxx"']

    sql = my_sql("readbook")
    sql.Create_table(tabname, column)
    sql.Update_table(tabname, user1)
    sql.Update_table(tabname, user2)


def reset_question():
    tabname = "question"
    column = []
    column.append(['Bookid', 'int'])
    column.append(['Question', 'varchar(2000)'])
    column.append(['Tpye', 'int'])
    column.append(['Option_num', 'int'])
    column.append(['Option1', 'varchar(2000)'])
    column.append(['Option2', 'varchar(2000)'])
    column.append(['Option3', 'varchar(2000)'])
    column.append(['Option4', 'varchar(2000)'])
    column.append(['Answer', 'varchar(2000)'])
    column.append(['Category', 'varchar(2000)'])

    sql = my_sql("readbook")
    sql.Create_table(tabname, column)


def reset_statistics():
    tabname= "statistics"
    column = []
    column.append(['userid', 'int'])
    column.append(['score','float'])
    column.append(['start','int'])
    column.append(['end','int'])
    column.append(['duration','int'])
    column.append(['a1','int'])
    column.append(['a2','int'])
    column.append(['a3','int'])
    column.append(['a4','int'])
    column.append(['a5','int']) 
    column.append(['b1','int'])
    column.append(['b2','int'])
    column.append(['b3','int'])
    column.append(['b4','int'])
    column.append(['b5','int'])

    column.append(['questionnum','int'])
    column.append(['rightnum','int'])
    column.append(['wrongnum','int'])
    column.append(['emptynum','int'])

    test1=[1,96,1668926839,1668927099,260,5,5,5,5,4,5,5,5,5,5,25,24,1,0]
    test2=[1,48,1668927000,1668927365,365,1,2,3,4,2,5,5,5,5,5,25,12,13,0]
    test3=[1,60,1668927566,1668927826,260,5,1,3,2,4,5,4,7,3,6,25,15,7,0]

    sql = my_sql("readbook")
    sql.Create_table(tabname, column)
    sql.Update_table(tabname, test1)
    sql.Update_table(tabname, test2)
    sql.Update_table(tabname, test3)
