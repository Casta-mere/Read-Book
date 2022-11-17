import pymysql


# Change the following to your own database connection info
host = 'localhost'
user = 'root'
password = ''
# password = '123456'


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

    def Update_user(self, id, name, gender, telephone, password, brief):
        item = []
        item.append(id)
        item.append(f'"{name}"')
        item.append(f'"{gender}"')
        item.append(f'"{telephone}"')
        item.append(f'"{password}"')
        item.append(f'"{brief}"')
        self.Update_table("user", item)


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

