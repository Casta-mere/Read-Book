from database import Database_conn as db
# from webcrawer import douban_webcrawer as dw
import control
import json

# databse=db.my_sql("readbook")
dir = "record/database_design/question.json"
dir2 = "record/questions/data/1.json"
mkdir2 = "record/questions/data"
bookherfdir = "code/webcrawer/ans/bookherf.txt"


def mkdir():
    for i in range(2, 201):
        with open(f"{mkdir2}/{i}.json", "w", encoding="utf-8") as f:
            f.write('{    "0": {        "Bookid": 1,        "Question": "",        "Type": 2,        "Options": [            "",            "",            "",            ""        ],        "Ans": "",        "Category": ""    },    "1": {        "Bookid": 1,        "Question": "",        "Type": 2,        "Options": [            "",            "",            "",            ""        ],        "Ans": "",        "Category": ""    },    "2": {        "Bookid": 1,        "Question": "",        "Type": 2,        "Options": [            "",            "",            "",            ""        ],        "Ans": "",        "Category": ""    },    "3": {        "Bookid": 1,        "Question": "",        "Type": 2,        "Options": [            "",            "",            "",            ""        ],        "Ans": "",        "Category": ""    },    "4": {        "Bookid": 1,        "Question": "",        "Type": 2,        "Options": [            "",            "",            "",            ""        ],        "Ans": "",        "Category": ""    },    "5": {        "Bookid": 1,        "Question": "",        "Type": 2,        "Options": [            "",            "",            "",            ""        ],        "Ans": "",        "Category": ""    }}')
            f.close()


def load():
    with open(dir, encoding="utf-8") as f:
        c = control.control()
        data = json.load(f)
        for i in data:
            info = []
            print(data[i]["Bookid"])
            info.append(f'"{data[i]["Bookid"]}"')
            print(data[i]["Question"])
            info.append(f'"{data[i]["Question"]}"')
            print(data[i]["Type"])
            info.append(f'"{data[i]["Type"]}"')
            options = data[i]["Options"]
            num = len(options)
            info.append(f'"{num}"')
            count = 0
            for j in options:
                print("option :", j)
                info.append(f'"{j}"')
                count += 1
            for j in range(count, 4):
                info.append('""')
            print(data[i]["Ans"])
            info.append(f'"{data[i]["Ans"]}"')
            print(data[i]["Category"])
            info.append(f'"{data[i]["Category"]}"')
            c.database.Update_table("question", info)


def test():
    with open(dir, encoding="utf-8") as f:
        data = json.load(f)
        for i in data:
            try:
                print(data[i]["Bookid"])
                print(data[i]["Question"])
                print(data[i]["Type"])
                options = data[i]["Options"]
                for j in options:
                    print("option :", j)
                print(data[i]["Ans"])
                print(data[i]["Category"])
            except:
                print(f"error on {i}")


def get_bookpic():
    with open(bookherfdir, 'r', encoding="utf-8") as f:
        r = f.readline().strip('\n')
        count = 1
        while(r):
            try:
                dw.get_bookpic(count, r)
                print(f"get {count} book pic")
            except:
                print(f"error on {count} book pic")

            count += 1
            r = f.readline().strip('\n')


# c=control.control()
# c.get_user_statistics(1)
# d=db.my_sql("readbook")
# d.Create_Database()

# db.reset_book()
# db.reset_question()
# db.reset_user()

# with open('code/database/book_info.sql', 'r', encoding="utf-8") as f:
#     sql = f.readline().strip('\n')
#     while(sql):
#         d.execute_sql(sql)
#         sql = f.readline().strip('\n')
# mkdir()
# db.reset_question()
# c = control.control()
# for i in range (1, 29):
#     c.load_question(f"../record/questions/data/{i}.json")
# c = control.control()
# c.load_question(dir)
# c.load_question(dir2)
# question=c.get_question_random()
