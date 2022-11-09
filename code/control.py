from database import Database_conn as db
from webcrawer import douban_webcrawer as dw


class control():
    def __init__(self):
        self.database = db.my_sql("readbook")
        self.user_id = self.get_all_user_id()

    def get_all_user_id(self):
        users = self.database.get_data("user")
        exist = []
        for i in users:
            exist.append(i[0])
        return exist

    def get_user_info_by_id(self, id):
        ans = list(self.database.get_data_by_attr("user", 'id', id)[0])
        return ans

    def new_user(self, name, gender, tele, pw, brief):
        import random
        id=random.randint(0,10000)
        while(id in self.user_id):
            id=random.randint(0,10000)
        self.database.Update_user(id,name,gender,tele,pw,brief)
        return id
        

c = control()

# print(c.get_user_info_by_id(1))
print(c.new_user(1, 2, 3, 4, 5))
