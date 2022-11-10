import pymysql


# Change the following to your own database connection info
host = 'localhost'
user = 'root'
# password = ''
password = '123456'


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
            print(sql)
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

    def Update_user(self,id,name,gender,telephone,password,brief):
        item=[]
        item.append(id)
        item.append(f'"{name}"')
        item.append(f'"{gender}"')
        item.append(f'"{telephone}"')
        item.append(f'"{password}"')
        item.append(f'"{brief}"')
        self.Update_table("user",item)

def preload():
    tabname_book = "book"
    column_book = []
    column_book.append(['id', 'int'])
    column_book.append(['name', 'varchar(50)'])
    column_book.append(['author', 'varchar(50)'])
    column_book.append(['country', 'varchar(50)'])
    column_book.append(['publisher', 'varchar(50)'])
    column_book.append(['year', 'varchar(50)'])
    column_book.append(['page', 'int'])
    column_book.append(['price', 'varchar(50)'])
    column_book.append(['frame', 'varchar(50)'])
    column_book.append(['category', 'varchar(50)'])
    column_book.append(['isbn', 'varchar(50)'])
    column_book.append(['star', 'float'])
    column_book.append(['comment_num', 'int'])
    column_book.append(['brief', 'varchar(1000)'])
    column_book.append(['douban_bookid', 'varchar(50)'])
    column_book.append(['link', 'varchar(50)'])
    column_book.append(['name_o', 'varchar(50)'])
    column_book.append(['trans', 'varchar(50)'])

    tabname_user = "user"
    column_user = []
    column_user.append(['id', 'int'])
    column_user.append(['name', 'varchar(50)'])
    column_user.append(['gender', 'char'])
    column_user.append(['telephone', 'varchar(50)'])
    column_user.append(['password', 'varchar(50)'])
    column_user.append(['brief', 'varchar(1000)'])

    sql = my_sql("readbook")
    sql.Create_Database()
    sql.Create_table(tabname_book, column_book)
    sql.Create_table(tabname_user, column_user)

    book1 = [1, '"冰与火之歌"', '"Geoge RR Martin"', '"US"', '"xxx"', '"1996"', 3000, '"300"', '"精装版"', '"魔幻"',
             '"1234-5678-910"', 9.9, 100, '"xxx"', '"124578"', '"sadadaw.wad.com"', '"A song of ice and fire"', '"屈畅"']

    user1 = [1, '"castamere"', '"M"',
             '"13834230484"', '"aaa6953217"', '"xxxx"']
    user2 = [2, '"today_red"', '"F"',
             '"13834230484"', '"aaa6953217"', '"xxxx"']
    sql.Update_table(tabname_book, book1)
    sql.Update_table(tabname_user, user1)
    sql.Update_table(tabname_user, user2)


# preload()
