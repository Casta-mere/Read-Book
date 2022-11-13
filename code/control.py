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

    # 创建新用户
    def new_user(self, name, gender, tele, pw, brief):
        import random
        id = random.randint(0, 10000)
        while(id in self.user_id):
            id = random.randint(0, 10000)
        self.database.Update_user(id, name, gender, tele, pw, brief)
        return id

    # 获取书籍排名，名字，作者
    def get_book_brief_info(self):
        brief_info = self.database.get_specific_data(
            "book", ["id", "name", "author"])
        return brief_info

    # 获取书籍详细信息,用于展示界面
    def get_book_detail_info(self, id):

        detail_info = self.database.get_data_by_attr("book", "id", id)
        return list(detail_info[0])

    # load question from json file
    def load_question(self, filename):
        import json
        with open(filename, encoding="utf-8") as f:
            data = json.load(f)
            for i in data:
                if (i == "0"):
                    continue
                info = []
                try:
                    info.append(f'"{data[i]["Bookid"]}"')
                    info.append(f'"{data[i]["Question"]}"')
                    info.append(f'"{data[i]["Type"]}"')
                    options = data[i]["Options"]
                    num = len(options)
                    info.append(f'"{num}"')
                    count = 0
                    for j in options:
                        info.append(f'"{j}"')
                        count += 1
                    for j in range(count, 4):
                        info.append('""')
                    info.append(f'"{data[i]["Ans"]}"')
                    info.append(f'"{data[i]["Category"]}"')
                    self.database.Update_table("question", info)
                except:
                    print(f"error on {filename}, question {i}")
# print(c.get_user_info_by_id(1))
# print(c.new_user(1, 2, 3, 4, 5))
# with open("book.txt", "w", encoding="utf-8") as f:
#     books=c.get_book_brief_info()
#     for i in books:
#         # print(i[0],i[1])
#         f.write(str(i[0])+" "+str(i[1])+"\n")
# info= c.get_book_detail_info(183)
# print(info)
