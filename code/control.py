from database import Database_conn as db
# from webcrawer import douban_webcrawer as dw


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
        try:
            ans = list(self.database.get_data_by_attr("user", 'id', id)[0])
        except:
            ans = []
        return ans

    def new_user(self, name, gender, tele, pw, brief):
        import random
        id = random.randint(0, 10000)
        while(id in self.user_id):
            id = random.randint(0, 10000)
        self.database.Update_user(id, name, gender, tele, pw, brief)
        return id

    def get_book_brief_info(self):
        brief_info = self.database.get_specific_data(
            "book", ["id", "name", "author"])
        return brief_info

    def get_book_detail_info(self, id):
        detail_info = self.database.get_data_by_attr("book", "id", id)
        return list(detail_info[0])


c = control()

# print(c.get_user_info_by_id(1))
# print(c.new_user(1, 2, 3, 4, 5))
# books=c.get_book_brief_info()
# for i in books:
#     print(i[0],i[1],i[2])
# info= c.get_book_detail_info(183)
# print(info)
